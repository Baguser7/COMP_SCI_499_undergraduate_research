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

import converter.tiktok_donwloader as converter
import artificial_intelligence.main_topic as topic

app = Flask(__name__)

@app.route('/predict/<links>', methods=["POST"])
def predict(links):
    # get current directory
    current_dir = os.path.dirname(os.path.realpath(__file__))
    predict_his_dir = f'{current_dir}\\data_raw\\histories.csv'

    # download tiktok videos from a link
    converter.get_tiktok_video(links)

    # convert video to text
    text = 'text goes here'

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
    if (converter.check_file(predict_his_dir)):
        with open(predict_his_dir,'w') as out:
            csv_out = csv.writer(out)
            csv_out.writerow(['tiktok_links','text','sentiment', 'keywoards_rake', 'keywords_spacy', 'main_topic_lda'])
            csv_out.writerow(links, text, decision, keywords_spacy, keywoards_rake, main_topic_lda)
    else:
        with open(predict_his_dir,'w') as out:
            csv_out = csv.writer(out)
            csv_out.writerow(links, text, decision, keywords_spacy, keywoards_rake, main_topic_lda)
    
    dictionary     = { 'status': 'success', 'prediction': decision }
    jsonDataOutput = json.dumps(dictionary)
    return jsonDataOutput


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='5000')
    #app.run()
    #serve(app, host='127.0.0.1', port=5000)