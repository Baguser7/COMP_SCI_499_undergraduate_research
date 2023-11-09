#<install> pip install moviepy
#<install> pip install SpeechRecognition
#https://www.geeksforgeeks.org/extract-speech-text-from-video-in-python/


import moviepy.editor as mp 
import speech_recognition as sr 
  
# Load the video 
video = mp.VideoFileClip("2_9gag.mp4") 
  
# Extract the audio from the video 
audio_file = video.audio 
audio_file.write_audiofile("2_9gag.wav") 
  
# Initialize recognizer 
r = sr.Recognizer() 
  
# Load the audio file 
with sr.AudioFile("2_9gag.wav") as source: 
    data = r.record(source) 
  
# Convert speech to text 
text = r.recognize_google(data) 
  
# Print the text 
print("\nThe resultant text from video is: \n") 
print(text) 