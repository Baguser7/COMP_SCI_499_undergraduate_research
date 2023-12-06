#<install> pip install moviepy
#<install> pip install openai-whisper
#<for conda users> conda install -c conda-forge ffmpeg
#https://www.geeksforgeeks.org/openai-whisper-converting-speech-to-text/
#https://www.geeksforgeeks.org/openai-whisper-converting-speech-to-text/

import whisper
import clean_up
import speech_recognition as sr

def whisper_instance(audio):
    model = whisper.load_model("base")
    transcription = model.transcribe(audio)
    output_file = transcription["text"]
    clean_up.deleteAudio(audio)

    return output_file

def houndify(audio):
    r = sr.Recognizer() 
    with sr.AudioFile(audio) as source: 
        data = r.record(source) 

    text = r.recognize_houndify(data, client_id='74f9EOm76HkxNQ7QZJeZLA==', client_key='zaejC92luOFmDXiTyV9wKfPh89HTajfRNFZaP7JUEOrA3oF3YDiX0J8Lc2ZmbZPxl7rj0cMu28J-4e75lT2UpQ==')
    return text

def googleSR(audio):
    r = sr.Recognizer() 
    with sr.AudioFile(audio) as source: 
        data = r.record(source) 

    text = r.recognize_houndify(data)
    return text



