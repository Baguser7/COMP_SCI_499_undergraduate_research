import os

def deleteAudio(audio):
    if os.path.exists(audio):
        os.remove(audio)
    else:
        print("The file does not exist")