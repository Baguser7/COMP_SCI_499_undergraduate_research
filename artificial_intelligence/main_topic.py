import string, spacy, nltk, os, os.path

from gensim import corpora
from gensim.models import LdaModel
from rake_nltk import Rake
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

def get_keywords_with_spacy(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    named_entities = [(ent.text, ent.label_) for ent in doc.ents]

    return named_entities

def get_keywords(text):
    r = Rake()
    r.extract_keywords_from_text(text)
    keywords = r.get_ranked_phrases()

    return keywords

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

    return main_topic

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

    return text
