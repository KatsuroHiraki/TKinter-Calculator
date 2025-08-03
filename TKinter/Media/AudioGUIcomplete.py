import pygame
import tkinter as tk
from tkinter import *

# Initialize Pygame Mixer once
pygame.mixer.init()

# File path
file_path = "C:/Users/alfya/Desktop/DE ROAD/PythonPractice/TKinter/Media/505song.mp3"

# State tracker
is_paused = False

def play_audio():
    global is_paused
    if is_paused:
        pygame.mixer.music.unpause()
        is_paused = False
    else:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

def pause_audio():
    global is_paused
    pygame.mixer.music.pause()
    is_paused = True

def stop_audio():
    pygame.mixer.music.stop()

def set_volume(val):
    volume = float(val)
    pygame.mixer.music.set_volume(volume)

# GUI Setup
root = tk.Tk()
root.geometry('400x200')
root.title("505 - Arctic Monkeys")

play_btn = Button(root, text="Play", command=play_audio)
play_btn.pack(pady=5)

pause_btn = Button(root, text="Pause", command=pause_audio)
pause_btn.pack(pady=5)

stop_btn = Button(root, text="Stop", command=stop_audio)
stop_btn.pack(pady=5)

volume_label = Label(root, text="Volume")
volume_label.pack()

volume_slider = Scale(root, from_=0, to=1, resolution=0.01, orient=HORIZONTAL, command=set_volume)
volume_slider.set(0.5)
volume_slider.pack()

root.mainloop()
