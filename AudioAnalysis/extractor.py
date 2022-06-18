import sys
from moviepy.editor import *
from pydub import AudioSegment
import wave

file = "test_01-20220618_140133-Meeting Recording.mp4"
video = VideoFileClip(file) # 2.
audio = video.audio # 3.
audio.write_audiofile("output.mp3") # 4.

sound = AudioSegment.from_mp3("output.mp3")

src = sound
dst = "output.wav"
# sound._data is a bytestring
raw_data = sound._data
sound.export(dst, format="wav")

print(raw_data)