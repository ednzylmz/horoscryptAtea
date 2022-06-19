from functions import *
from captioning import *
from vars import *
from azureadvanced import *

#Download meeting
site_url = 'https://tartuulikool-my.sharepoint.com/:v:/g/personal/karlmv_ut_ee/Eb_w5Gj4N0lIv3sIgmalcjQBWjktodUT3JRiO3GWkRAqCw?e=YfASkt'
mp4 = meeting_downloader(site_url)

mp3 , wav = extract_audio(mp4)
vtt_file = captioner(textkey, textregion , wav)

# summary = summarizer(vtt_file) # for now assume it does work for flask
summary = './artifacts/summary.txt'