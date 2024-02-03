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
    if not url:
        status_var.set("Input valid URL!")
        return
    try:
        subprocess.run([
            "yt-dlp.exe", 
            "-f", 
            "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best", 
            "--output", 
            "./downloads/videos/%(title)s.%(ext)s", 
            url
        ])
        status_var.set("Video Download Complete!")
    except Exception as e:
        status_var.set(f"Error: {str(e)}")

    url_entry.delete(0, 'end')

def download_audio():
    url = url_entry.get()
    if not url:
        status_var.set("Input valid URL!")
        return
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
        
    url_entry.delete(0, 'end')

def open_directory():
    downloads_directory = os.path.join(os.getcwd(), "downloads")
    try:
        subprocess.Popen(["explorer", downloads_directory], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        status_var.set("File Explorer Opened!")
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

open_directory_button = Button(app, text="Open Downloads Folder", command=open_directory)
open_directory_button.pack(pady=10)

status_var = StringVar()
status_label = Label(app, textvariable=status_var)
status_label.pack(pady=10)

app.geometry("350x300")

app.mainloop()
