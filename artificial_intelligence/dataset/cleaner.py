import pandas as pd
import nltk, os, os.path, csv, joblib

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

def read_data(file_path, train_data_path, train100_data_path):
    print('Reading data...')
    df = pd.read_csv(file_path, dtype='unicode')
    df_tuple = list()
    
    # toxic = 2, negative = 1
    for data in df.iterrows():
        text = data[1][1]
        
        if (int(data[1][2]) + int(data[1][3])) >= 1:
            # classify data as toxic
            df_tuple.append([text, 2])
        elif (int(data[1][4]) + int(data[1][5]) + int(data[1][6]) + int(data[1][7])) >= 1:
            # classify data as negative
            df_tuple.append([text, 1])
        else:
            # classify data as non toxic or negative
            df_tuple.append([text, 0])
            
    # save data
    if check_csv(train_data_path):
        write_csv(df_tuple, train_data_path)
    else:
        initiate_csv(train_data_path)
        write_csv(df_tuple, train_data_path)
        
    write_1000csv(df_tuple, train100_data_path)
    
def write_csv(data, train_data_path):
    print('Writing Data...')
    with open(train_data_path,'a') as out:
        csv_out = csv.writer(out)
        for row in data:
            csv_out.writerow(row)

def write_1000csv(data, train1000_data_path):
    if check_csv(train1000_data_path):
        print('Writing 1000 data...')
        counter = 0
        with open(train1000_data_path,'a') as out:
            csv_out = csv.writer(out)
            for row in data:
                csv_out.writerow(row)
                
                counter += 1
                if counter == 1000:
                    break
    else:
        initiate_csv(train1000_data_path)
        write_1000csv(data, train1000_data_path)
        
def write_n_csv(train_data_path, number_of_row):
    initiate_csv(train_data_path)
    if check_csv(train_data_path):
        counter = 0
        df = pd.read_csv('data_training/clean_data.csv')
        with open('data_training/clean_data.csv','a') as out:
            csv_out = csv.writer(out)
            for i, row in df.iterrows():
                print(row['text'])
                csv_out.writerow()
                
                counter += 1
                if counter == number_of_row:
                    break
    else:
        initiate_csv(train_data_path)
        write_n_csv(train_data_path, number_of_row)

def check_csv(train_data_path):
    return os.path.isfile(train_data_path)

def initiate_csv(train_data_path):
    print('Train data is not found, creating a new one.')
    with open(train_data_path,'w') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['text','sentiment'])

def clean_current_dataset(dataset_path):
    df = pd.read_csv(dataset_path)
    df_text = df['text'].astype(str)
    df_class = df['sentiment']
    
    lines_clean = list()
    lines = df_text.values.tolist()
    porter = PorterStemmer()
    wordnet_lemmatizer = WordNetLemmatizer()

    for line in lines:
        tokens = word_tokenize(line)
        tokens = [w.lower() for w in tokens]
        
        #check alphabhet
        tokens = [word for word in tokens if word.isalpha()]
        
        #remove stopwords
        tokens = [word for word in tokens if not word in stopwords.words()]
        
        #stemming
        tokens = [porter.stem(word) for word in tokens]

        #lemmatization
        tokens = [wordnet_lemmatizer.lemmatize(word) for word in tokens]
        
        #print(tokens)
        lines_clean.append(tokens)
        print(tokens)

def init():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    raw_data_dir = f'{current_dir}\\data_raw'
    train_data_dir = f'{current_dir}\\data_training\\clean_data.csv'
    train1000_data_dir = f'{current_dir}\\data_training\\clean_data.csv'
    
    paths = (f'{raw_data_dir}\\dataset-1.csv', f'{raw_data_dir}\\dataset-2.csv')

    # read_data(paths[0], train_data_dir, train1000_data_dir)
    clean_current_dataset(f'{current_dir}\\data_training\\clean_data_main_topics.csv')
    print('\nFinished!')
    
if __name__ == '__main__':
    init()