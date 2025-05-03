import pyttsx3
import tkinter as tk
from tkinter import scrolledtext, Scale, ttk

root = tk.Tk()
root.title("Simple Text-to-Speech")
root.geometry("500x350")

engine = pyttsx3.init()

text_label = tk.Label(root, text="Enter text to speak:")
text_label.pack(pady=(10, 5))

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=8)
text_area.pack(padx=10, pady=5)

rate_frame = tk.Frame(root)
rate_frame.pack(fill=tk.X, padx=10, pady=5)
rate_label = tk.Label(rate_frame, text="Rate:")
rate_label.pack(side=tk.LEFT)
rate_var = tk.IntVar(value=180)
rate_scale = Scale(rate_frame, from_=50, to=300, orient=tk.HORIZONTAL, variable=rate_var, length=300)
rate_scale.pack(side=tk.LEFT, padx=5)

def speak():
    text = text_area.get("1.0", tk.END).strip()
    if text:
        engine.setProperty('rate', rate_var.get())
        engine.say(text)
        engine.runAndWait()

def stop():
    engine.stop()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)
speak_button = ttk.Button(button_frame, text="Speak", command=speak)
speak_button.pack(side=tk.LEFT, padx=10)
stop_button = ttk.Button(button_frame, text="Stop", command=stop)
stop_button.pack(side=tk.LEFT, padx=10)

root.mainloop()