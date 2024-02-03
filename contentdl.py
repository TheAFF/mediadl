import os
import tkinter as tk
from tkinter import Entry, Label, Button, StringVar
import subprocess

def create_folders():
    folders = ["downloads", "downloads/videos", "downloads/audio"]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

def download_video():
    url = url_entry.get()
    try:
        subprocess.run([
            "yt-dlp.exe", 
            "--output", 
            "./downloads/videos/%(title)s.%(ext)s", 
            url
        ])
        status_var.set("Video Download Complete!")
    except Exception as e:
        status_var.set(f"Error: {str(e)}")

def download_audio():
    url = url_entry.get()
    try:
        subprocess.run([
            "yt-dlp.exe",
            "-x",
            "--audio-format", "mp3",
            "--embed-thumbnail",
            "--add-metadata",
            "--output", "./downloads/audio/%(title)s.%(ext)s",
            url
        ])
        status_var.set("Audio Download Complete!")
    except Exception as e:
        status_var.set(f"Error: {str(e)}")

#checks if downloads folder is present
create_folders()

#UI
app = tk.Tk()
app.title("Media Downloader")

url_label = Label(app, text="Enter URL:")
url_label.pack(pady=10)

url_entry = Entry(app, width=40)
url_entry.pack(pady=20)

download_video_button = Button(app, text="Download Video", command=download_video)
download_video_button.pack(pady=10)

download_audio_button = Button(app, text="Download Audio", command=download_audio)
download_audio_button.pack(pady=10)

status_var = StringVar()
status_label = Label(app, textvariable=status_var)
status_label.pack(pady=10)

app.geometry("300x250")

app.mainloop()