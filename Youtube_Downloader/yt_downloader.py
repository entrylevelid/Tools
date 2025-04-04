import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp

def download_video():
    url = url_entry.get()
    folder = filedialog.askdirectory()

    if not url or not folder:
        messagebox.showwarning("Warning", "Please enter a URL and select a folder!")
        return
    
    try:
        ydl_opts = {
            'outtmpl': f"{folder}/%(title)s.%(ext)s",
            'format': 'mp4'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occured: {e}")

root = tk.Tk()
root.title("Youtube Downloader")

tk.Label(root, text="Enter Youtube Video URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_btn = tk.Button(root, text="Download", command=download_video)
download_btn.pack(pady=20)

root.mainloop()