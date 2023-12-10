#<install> pip install moviepy
#<install> pip install openai-whisper
#<for conda users> conda install -c conda-forge ffmpeg
#https://www.geeksforgeeks.org/openai-whisper-converting-speech-to-text/
#https://www.geeksforgeeks.org/openai-whisper-converting-speech-to-text/

import os, os.path
import whisper
import speech_recognition as sr

def whisper_instance():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    audio_dir = f'{current_dir}\\audio\\temp.wav'

    model = whisper.load_model("base")
    transcription = model.transcribe(audio_dir, language="en")
    output_file = transcription["text"]
    
    return output_file

def whisper_instance_tiny(audio):
    model = whisper.load_model("tiny")
    transcription = model.transcribe(audio, language="en")
    output_file = transcription["text"]
    return output_file

def houndify(audio):
    r = sr.Recognizer() 
    with sr.AudioFile(audio) as source: 
        data = r.record(source) 
    try:
        text = r.recognize_houndify(data, client_id='2Iz2Gs8xNg2zbHz2oxlvgA==', client_key='hv4Zpo4CsghKe13pBacwGI12bIwqGCjiVw6E4e5mTIQbgAq5rKsvDlJesnZdFJhUM-39UDwJjqQimdu52mSKTQ==')
    except Exception as e:
        text = '0'
    return text

def googleSR(audio):
    r = sr.Recognizer() 
    with sr.AudioFile(audio) as source: 
        try:
            data = r.record(source) 
            text = r.recognize_google(data,language="en-US")
        except Exception as e:
            text = "0"
    return text

def init():
    return

if __name__ == '__main__':
    init()