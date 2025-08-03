import cv2
import tkinter as tk
from PIL import Image, ImageTk

def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (400, 300))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(frame))
        video_label.config(image=img)
        video_label.image = img
        video_label.after(15, update_frame)  # 60 FPS = ~15 ms

cap = cv2.VideoCapture('C:/Users/alfya/Desktop/DE ROAD/PythonPractice/TKinter/Media/NiceMeme.mp4')

root = tk.Tk()
root.geometry("400x300")
video_label = tk.Label(root)
video_label.pack()

update_frame()
root.mainloop()

cap.release()
