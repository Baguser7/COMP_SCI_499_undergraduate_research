import video_to_text.video_toAudio as video_converter
import video_to_text.transcribe as transcriber
import video_to_text.clean_up as cleaner
import video_to_text.converter.tiktok_donwloader as td

from difflib import SequenceMatcher
import csv, os, os.path

def iterateVideo(csv_file, column):
    list_links = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        #header = next(reader, None)
        for row in reader:
            link_value = row[column]
            list_links.append(link_value)
        return list_links

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def iterateText(list):
    with open(score_csv, 'w', encoding="utf8", newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["link","base-whisper","tiny-whisper","googleSR","Houndify","base-tiny","base-google","base-houndify"])
        
        for i in list:
            td.get_tiktok_video(i)
            video_converter.convertVideo("temp.mp4", tempAudio)

            a = transcriber.whisper_instance(tempAudio)
            print('-')

            b = transcriber.whisper_instance_tiny(tempAudio)
            print('-')

            c = transcriber.googleSR(tempAudio)
            print('|')

            d = transcriber.houndify(tempAudio)    
            print('|')
            #list_score.append(similar(a, output))
            cleaner.deleteAudio(tempAudio)
            print([i,a,b,c,d,similar(a, b),similar(a, c),similar(a, d)])
            try:
                csv_writer.writerow([i,a,b,c,d,similar(a, b),similar(a, c),similar(a, d)])
            except Exception as e:
                csv_writer.writerow([i,"0","0",c,d,similar("0", "0"),similar("0", c),similar("0", d)])

def check_sentiment(data):
    if (data == 0):
        temp = 'Non Toxic or Negative'
    elif (data == 1):
        temp = 'Negative'
    elif (data == 2):
        temp = 'Toxic'
    else:
        temp = 'Beyond Toxic'
    
    return temp

def get_dataset_dir():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = current_dir.split('\\')
    parent_dir.pop()

    parent_joined_dir = '\\'.join(parent_dir)
    links_csv = f'{parent_joined_dir}\\artificial_intelligence\\dataset\\data_raw\\sheetVideo_lite.csv'
    score_csv = f'{parent_joined_dir}\\artificial_intelligence\\dataset\\data_raw\\score_10.csv'
    return [links_csv, score_csv]

if __name__ == "__main__":
    metadata_csv = "metadata_tiktok.csv"
    browser      = "firefox"
    tempAudio    = "audioTemp.wav"
    list_score   = []

    links = get_dataset_dir()
    links_csv = links[0]
    score_csv = links[-1]

    # list_links = iterateVideo(links_csv, 'Links')

'''

iterateText(list_links)
    
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

iterateVideo(links_csv, 70, 75, "Links")
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
        print(modified_link)
        tiktok_download.download_tiktok(i, metadata_csv, browser)

        if os.path.exists(modified_link):
            #print(f"The file {modified_link} exists.")
            video_toAudio.convertVideo(modified_link, tempAudio)
            output = transcribe.whisper_instance(tempAudio)
            print(output + "\n")
        else:
            print(f"The file {modified_link} does not exist.")

checkText()

video_toAudio.convertVideo("z.mp4", tempAudio)
output = transcribe.whisper_instance(tempAudio)
print(output + "\n")

'''