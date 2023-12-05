#<install> pip install moviepy
#<install> pip install SpeechRecognition
#https://www.geeksforgeeks.org/extract-speech-text-from-video-in-python/


import moviepy.editor as mp 
import speech_recognition as sr 
import get_data
  
# Load the video 
#video = mp.VideoFileClip(r"COMP_SCI_499_undergraduate_research\Video to Text\Video\2_9gag.mp4")
url = 'https://vm.tiktok.com/ZT85rcSLS/'
local = 'toxic1.mp4'
get_data.download_file(url,local)
video = mp.VideoFileClip("toxic1.mp4")
  
# Extract the audio from the video 
audio_file = video.audio 
source = audio_file.write_audiofile("1.wav")
  
# Initialize recognizer 
r = sr.Recognizer() 
  
# Load the audio file 
with sr.AudioFile("1.wav") as source: 
    data = r.record(source) 
  
# Convert speech to text 
text = r.recognize_houndify(data, client_id='74f9EOm76HkxNQ7QZJeZLA==', client_key='zaejC92luOFmDXiTyV9wKfPh89HTajfRNFZaP7JUEOrA3oF3YDiX0J8Lc2ZmbZPxl7rj0cMu28J-4e75lT2UpQ==')
  
# Print the text 
print("\nThe resultant text from video is: \n") 
print(text) 