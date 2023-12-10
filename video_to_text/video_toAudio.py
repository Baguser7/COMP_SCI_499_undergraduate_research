import os, os.path
import moviepy.editor as mp 

def convertVideo(videoClip, tempAudio):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    video = mp.VideoFileClip(f'{current_dir}\\video\\{videoClip}') 
  
    # Extract the audio from the video 
    audio_file = video.audio 
    audio_file.write_audiofile(f'{current_dir}\\audio\\{tempAudio}')