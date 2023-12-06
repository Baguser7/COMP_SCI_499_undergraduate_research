import video_toAudio
import transcribe

tempAudio = "audioTemp.mp3"
video = r"COMP_SCI_499_undergraduate_research\Video to Text\Video\2_vsauce.mp4"
video_toAudio.convertVideo(video, tempAudio)

output = transcribe.whisper(tempAudio)
print(output)