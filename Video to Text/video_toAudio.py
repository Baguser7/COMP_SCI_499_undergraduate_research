import moviepy.editor as mp 

def convertVideo(videoClip,tempAudio):
    video = mp.VideoFileClip(videoClip) 
  
# Extract the audio from the video 
    audio_file = video.audio 
    audio_file.write_audiofile(tempAudio)