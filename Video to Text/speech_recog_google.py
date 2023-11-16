#<install> pip install moviepy
#<install> pip install SpeechRecognition
#https://www.geeksforgeeks.org/extract-speech-text-from-video-in-python/


import moviepy.editor as mp 
import speech_recognition as sr 
  
# Load the video 
video = mp.VideoFileClip(r"Video to Text\jp.mp4") 
  
# Extract the audio from the video 
audio_file = video.audio 
source = audio_file.write_audiofile("1.wav")
  
# Initialize recognizer 
r = sr.Recognizer() 
  
# Load the audio file 
with sr.AudioFile("1.wav") as source: 
    data = r.record(source) 
  
# Convert speech to text 
text = r.recognize_ibm(data)
  
# Print the text 
print("\nThe resultant text from video is: \n") 
print(text) 