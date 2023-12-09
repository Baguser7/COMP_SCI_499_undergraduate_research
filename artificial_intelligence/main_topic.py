import string, spacy, nltk, os, os.path

from gensim import corpora
from gensim.models import LdaModel
from rake_nltk import Rake
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from profanity_check import predict

def get_keywords_with_spacy(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    named_entities = [ent.text for ent in doc.ents]

    return checker(named_entities)

def get_keywords(text):
    r = Rake()
    r.extract_keywords_from_text(text)
    keywords = r.get_ranked_phrases()

    return checker(keywords)

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    
    tokens = [token for token in tokens if token not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return tokens

def get_main_topic(text):
    processed_tokens = preprocess_text(text)
    dictionary = corpora.Dictionary([processed_tokens])
    corpus = [dictionary.doc2bow(processed_tokens)]
    lda_model = LdaModel(corpus, num_topics=1, id2word=dictionary)

    main_topic = lda_model.print_topics(num_words=5)

    main_topic_list = main_topic[0][-1]
    topic_data = main_topic_list.split('"')
    clean_topics = []
    for i in range(1, len(topic_data), 2):
        clean_topics.append(topic_data[i])

    return checker(clean_topics)

def clean_data(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = ''.join([i for i in text if not i.isdigit()])

    tokens = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.lower() not in stop_words]

    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]

    cleaned_text = ' '.join(tokens)

    return cleaned_text

def profanity_check(text):
    return predict([text])[0]

def checker(data):
    for keyword in data:
        print(keyword)
        prediction = profanity_check(keyword)
        if prediction == 1:
            return prediction
    return 0