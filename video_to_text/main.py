import video_toAudio
import transcribe

tempAudio = "audioTemp.mp3"
video = r"COMP_SCI_499_undergraduate_research\video_to_text\Video\2_vsauce.mp4"
video_toAudio.convertVideo(video, tempAudio)

output = transcribe.whisper_instance(tempAudio)
print(output)