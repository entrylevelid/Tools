import time
import threading
import tkinter as tk
from plyer import notification

def show_notification(msg):
    notification.notify(title="Reminder", message=msg, timeout=10)

def set_reminder():
    try:
        sec = int(entry_time.get())
        msg = entry_message.get().strip()
        if sec <= 0 or not msg:
            return
        threading.Thread(target=lambda: (time.sleep(sec), show_notification(msg)), daemon=True).start()
    except ValueError:
        pass

root = tk.Tk()
root.title("Reminder")
root.geometry("250x120")

tk.Label(root, text="Time (seconds):").pack()
entry_time = tk.Entry(root)
entry_time.pack()

tk.Label(root, text="Message:").pack()
entry_message = tk.Entry(root)
entry_message.pack()

tk.Button(root, text="Set Reminder", command=set_reminder).pack()
root.mainloop()