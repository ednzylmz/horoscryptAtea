import sys
from moviepy.editor import *
from pydub import AudioSegment
import wave
import requests

def extract_audio(file = "./artifacts/input.mp4" , output_mp3 = "./artifacts/input.mp3", output_wav = "./artifacts/input.wav"):

  video = VideoFileClip(file) # 2.
  audio = video.audio # 3.
  audio.write_audiofile(output_mp3) # 4.

  sound = AudioSegment.from_mp3("./artifacts/input.mp3") # 5.

  src = sound
  dst = output_wav
  # sound._data is a bytestring
  raw_data = sound._data
  sound.export(dst, format="wav")

  print(raw_data)
  return(output_mp3, output_wav)


def meeting_downloader(site_url , output_file = './artifacts/input.mp4' ):
    URL = site_url + '&download=1'

    resp = requests.get(URL) # making requests to server

    with open(output_file, "wb") as f: # opening a file handler to create new file 
        f.write(resp.content) 
    return(output_file)