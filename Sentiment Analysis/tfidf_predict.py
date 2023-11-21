
"""
Created on 2020-06-16
@author: Dr. Ganjar Alfian
@email: ganjar@dongguk.edu
"""



import joblib
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
    
if __name__ == '__main__':
    #set new un-labelled sentence
    input_data= "shitty"
    transformer = TfidfTransformer()
    #load the vectorizer 
    loaded_vec = CountVectorizer(decode_error="replace",vocabulary=joblib.load(open(r".\COMP_SCI_499_undergraduate_research\Sentiment Analysis\vectorizer.model", "rb")))
    tfidf = transformer.fit_transform(loaded_vec.fit_transform(np.array([input_data])))
    #load the model
    filename = r".\COMP_SCI_499_undergraduate_research\Sentiment Analysis\mlp_tfidf.model"
    loaded_model= joblib.load(filename)
    #make new prediction
    result = loaded_model.predict(tfidf)
    print(result)

    for i in result:
        print(i)
        int_result = int(i)
        if(int_result==0):
            decision='Neutral'
        elif(int_result==1):
            decision='Negative'
        else:
            decision='Positive'
        print('The sentence is ', decision)
