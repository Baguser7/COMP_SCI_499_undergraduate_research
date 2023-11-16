#<install> pip install moviepy
#<install> pip install openai-whisper
#<for conda users> conda install -c conda-forge ffmpeg
#https://www.geeksforgeeks.org/openai-whisper-converting-speech-to-text/
#https://www.geeksforgeeks.org/openai-whisper-converting-speech-to-text/

import moviepy.editor as mp 
import whisper
import sys

video = mp.VideoFileClip(r"H:\Team_Undergraduate Research\COMP_SCI_499_undergraduate_research\Video to Text\2_9gag.mp4") 
  
# Extract the audio from the video 
audio_file = video.audio 
audio_file.write_audiofile("2_9gag.mp3")

model = whisper.load_model("base")
transcription = model.transcribe("2_9gag.mp3")

# Specify the file name you want to write to
output_file = "2_gag.txt"

# Open the file in write mode and redirect the output to it
with open(output_file, "w") as file:
    sys.stdout = file  # Redirect standard output to the file

    print(transcription["text"])

# Reset standard output to the console
sys.stdout = sys.__stdout__