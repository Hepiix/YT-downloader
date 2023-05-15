from email.mime import audio
from pytube import YouTube
from moviepy.editor import *

def download_from_yt():
    file1 = open('myfile.txt', 'r')
    Lines = file1.readlines()

    for line in Lines:
        yt = YouTube(line)
        stream = yt.streams.get_audio_only()
        stream.download()
        print(f'Done {stream.title}')


def convert_to_mp3():
    for filename in os.listdir("files"):
        clip = AudioFileClip(f'files/{filename}')
        clip.write_audiofile(f'files/ready/{filename}.mp3')
        print(f'Done {filename}.mp3')


print("1. Download\n2.Convert")
x = input()

if (x == "1"):
    download_from_yt()
else:
    convert_to_mp3()
