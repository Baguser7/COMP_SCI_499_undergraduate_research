import pandas as pd
import numpy as np
import urllib.request as request_api
import os.path, joblib, json, os, csv

from profanity_check import predict
from flask import Flask, redirect, url_for, request, render_template
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

import video_to_text.converter.tiktok_donwloader as converter
import video_to_text.video_toAudio as video_converter
import video_to_text.transcribe as transcriber
import video_to_text.process as processor
import artificial_intelligence.main_topic as topic

app = Flask(__name__)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # get links from user
    links = request.args.get('links') 

    # get current directory
    current_dir = os.path.dirname(os.path.realpath(__file__))
    predict_his_dir = f'{current_dir}\\artificial_intelligence\\dataset\\data_raw\\histories.csv' 
    
    # download tiktok videos from a link
    converter.get_tiktok_video(links)

    # convert video to text
    video_converter.convertVideo("temp.mp4", "temp.wav")
    text = transcriber.whisper_instance()

    # make predictions
    transformer    = TfidfTransformer()
    vectorizer_dir = f'{current_dir}\\artificial_intelligence\\sentiment_models\\vectorizer.model'
    loaded_vec     = CountVectorizer(decode_error="replace",vocabulary=joblib.load(open(vectorizer_dir, "rb")))
    tfidf          = transformer.fit_transform(loaded_vec.fit_transform(np.array([text])))

    model_dir      = f'{current_dir}\\artificial_intelligence\\sentiment_models\\new_model.model'
    loaded_model   = joblib.load(model_dir)
    result         = loaded_model.predict(tfidf)

    decision = processor.check_sentiment(int(result[0]))

    # analyze main topic with spacy
    keywords_spacy = result[0] + topic.get_keywords_with_spacy(text)

    # analyze keywords with rake
    keywords_rake = result[0] + topic.get_keywords(text)

    # analyze main topic with LDA
    main_topic_lda = result[0] + topic.get_main_topic(text)    

    # record data
    if (converter.check_file(predict_his_dir) == False):
        with open(predict_his_dir,'w',encoding="utf8",newline='') as out:
            csv_out = csv.writer(out)
            csv_out.writerow(['tiktok_links','text','sentiment', 'keywords_rake', 'keywords_spacy', 'main_topic_lda'])
            csv_out.writerow([links, text, decision, processor.check_sentiment(keywords_spacy), processor.check_sentiment(keywords_rake), processor.check_sentiment(main_topic_lda)])
    else:
        df = pd.read_csv(predict_his_dir, usecols=['tiktok_links'])
        if links in df.values:
            with open(predict_his_dir,'a',encoding="utf8",newline='') as out:
                csv_out = csv.writer(out)
                csv_out.writerow([links, text, decision, processor.check_sentiment(keywords_spacy), processor.check_sentiment(keywords_rake), processor.check_sentiment(main_topic_lda)])

    # return data in form of JSON
    dictionary     = { 'status': 'success', 'prediction': decision }
    jsonDataOutput = json.dumps(dictionary)
    print(decision)
    return jsonDataOutput

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='5000')

    '''
    # this is a test code, use only when testing

    app.run(host='127.0.0.1', port='5000')
    app.run()
    serve(app, host='127.0.0.1', port=5000)
    
    link = 'https://www.tiktok.com/@littlegirlmovies/video/7310590241470008607?is_from_webapp=1&sender_device=pc'
    predict(link)

    links_csv = r'COMP_SCI_499_undergraduate_research\artificial_intelligence\dataset\data_raw\sheetVideo_lite.csv'
    list_links = process.iterateVideo(links_csv, 'Links')
    counter = 0
    for i in list_links:
        predict(i)
        print("_")

    '''

