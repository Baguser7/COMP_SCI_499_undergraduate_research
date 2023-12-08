import pandas as pd
import numpy as np
import urllib.request as request_api
import os.path 
import joblib
import json
import os
import csv

from flask import Flask, redirect, url_for, request, render_template
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

from video_to_text.converter import tiktok_donwloader as converter
from video_to_text import video_toAudio
from video_to_text import transcribe
from video_to_text import process
import artificial_intelligence.main_topic as topic

links_csv = r'COMP_SCI_499_undergraduate_research\artificial_intelligence\dataset\data_raw\sheetVideo_lite.csv'
app = Flask(__name__)

@app.route('/predict', methods=["POST"])
def predict(links):
    # get links from user
    # links = request.args.get('links') 

    # get current directory
    current_dir = os.path.dirname(os.path.realpath(__file__))
    predict_his_dir = f'{current_dir}\\artificial_intelligence\\dataset\\data_raw\\histories.csv' 

    # download tiktok videos from a link
    converter.get_tiktok_video(links)

    # convert video to text
    video_toAudio.convertVideo("temp.mp4", "temp.wav")
    text = transcribe.whisper_instance("temp.wav")

    # make predictions
    transformer    = TfidfTransformer()
    vectorizer_dir = f'{current_dir}\\artificial_intelligence\\sentiment_models\\vectorizer.model'
    loaded_vec     = CountVectorizer(decode_error="replace",vocabulary=joblib.load(open(vectorizer_dir, "rb")))
    tfidf          = transformer.fit_transform(loaded_vec.fit_transform(np.array([text])))

    model_dir      = f'{current_dir}\\artificial_intelligence\\sentiment_models\\new_model.model'
    loaded_model   = joblib.load(model_dir)
    result         = loaded_model.predict(tfidf)

    for i in result:
        int_result = int(i)
        if (int_result == 0):
            decision = 'Non Toxic or Negative'
        elif (int_result == 1):
            decision = 'Negative'
        elif (int_result == 2):
            decision = 'Toxic'
        else:
            decision = 'Cannot Predict'
    
    # analyze main topic with spacy
    keywoards_rake = topic.get_keywords_with_spacy(text)

    # analyze keywords with rake
    keywords_spacy = topic.get_keywords(text)

    # analyze main topic with LDA
    main_topic_lda = topic.get_main_topic(text)

    # record data
    if (converter.check_file(predict_his_dir) == False):
        with open(predict_his_dir,'w',encoding="utf8",newline='') as out:
            csv_out = csv.writer(out)
            csv_out.writerow(['tiktok_links','text','sentiment', 'keywords_rake', 'keywords_spacy', 'main_topic_lda'])
            csv_out.writerow([links, text, decision, keywords_spacy, keywoards_rake, main_topic_lda])
    else:
        df = pd.read_csv(predict_his_dir, usecols=['tiktok_links'])
        if links in df.values:
            with open(predict_his_dir,'a',encoding="utf8",newline='') as out:
                csv_out = csv.writer(out)
                csv_out.writerow([links, text, decision, keywords_spacy, keywoards_rake, main_topic_lda])

    
    dictionary     = { 'status': 'success', 'prediction': decision }
    jsonDataOutput = json.dumps(dictionary)
    return jsonDataOutput


# if __name__ == "__main__":
#     app.run(host='127.0.0.1', port='5000')
#     #app.run()
#     #serve(app, host='127.0.0.1', port=5000)

list_links = process.iterateVideo(links_csv, 'Links')
counter = 0
for i in list_links:
    predict(i)
    print("_")