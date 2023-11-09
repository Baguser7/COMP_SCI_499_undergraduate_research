#<install> pip install moviepy
#<install> pip install openai-whisper
#<for conda users> conda install -c conda-forge ffmpeg
#https://www.geeksforgeeks.org/openai-whisper-converting-speech-to-text/
#https://www.geeksforgeeks.org/openai-whisper-converting-speech-to-text/

import moviepy.editor as mp 
import whisper

video = mp.VideoFileClip("2_9gag.mp4") 
  
# Extract the audio from the video 
audio_file = video.audio 
audio_file.write_audiofile("2_9gag.mp3")

model = whisper.load_model("base")
transcription = model.transcribe("2_9gag.mp3")

print(transcription["text"])