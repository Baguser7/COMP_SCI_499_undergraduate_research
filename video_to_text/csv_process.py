import csv

def find(csv_file, find):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Links'] == find:
                # print("link found")
                return row['Sentiment']
            else :
                #DO THE SENTIMENT ANALYSIS,RETURN THE SENTIMENT
                row['Links'] += find
                row['Sentiment'] += THE-SENTIMENT-RESULT
                return THE-SENTIMENT-RESULT