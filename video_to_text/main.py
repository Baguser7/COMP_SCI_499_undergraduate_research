import video_toAudio
import transcribe
import tiktok_download
import csv
import os
from difflib import SequenceMatcher

links_csv = r'COMP_SCI_499_undergraduate_research\sentiment_analysis\create_model\data_cleaning\raw_data\sheetVideo.csv'
tiktok_link = 'https://vm.tiktok.com/ZT85rTC8R/'
metadata_csv = "metadata_tiktok.csv"
browser = "firefox"
tempAudio = "audioTemp.wav"
list_links = []

def iterateVideo(csv_file, number, column):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)

        for _ in range(number):
            try:
                row = next(reader)
                link_value = row[column]
                list_links.append(link_value)
            except StopIteration:
                # Handle the case where there are fewer rows than expected
                print("Reached the end of the file.")
                break

iterateVideo(links_csv, 5, 'Links')
print(list_links)

def catch_videoName(link):
    if "video" in link:
        result_list = link.split(".com/")
        modified_list = result_list[1].split('?')
        modified_string = modified_list[0]
        for char in '/':
            modified_string = modified_string.replace(char, '_')
        return modified_string + ".mp4"
    else:
        result_list = link.split(".com/")
        modified_string = result_list[1]
        for char in '/':
            modified_string = modified_string.replace(char, '_')
        return modified_string + ".mp4"

def checkText():
    for i in list_links:
        modified_link = catch_videoName(i)
        tiktok_download.download_tiktok(i, metadata_csv, browser)

        if os.path.exists(modified_link):
            print(f"The file {modified_link} exists.")
            video_toAudio.convertVideo(modified_link, tempAudio)
            output = transcribe.whisper_instance(tempAudio)
            print(output + "\n")
        else:
            print(f"The file {modified_link} does not exist.")

checkText()

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def find(csv_file, find):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Links'] == find:
                print("link found")
                return row['Sentiment']
            else :
                print('sentiment added')
                #DO THE SENTIMENT ANALYSIS,RETURN THE SENTIMENT
                with open(csv_file, 'a', newline='') as append_file:
                    writer = csv.writer(append_file)
                    writer.writerow([find, sentiment_result])

                return THE-SENTIMENT-RESULT


