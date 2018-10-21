from __future__ import unicode_literals
import youtube_dl
import os
from sys import argv

#Download data and config

download_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'nochechkcertificate': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec':'mp3',
        'preferredquality': '192',
    }], 
}

#Song Directory
if not os.path.exists('Music'):
    os.mkdir('Music')
else:
    os.chdir('Music')

#Download Songs
with youtube_dl.YoutubeDL(download_options) as dl:
    with open('../' + argv[1], 'r')as f:
        for song_url in f:
            dl.download([song_url])
