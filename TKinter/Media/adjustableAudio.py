import pygame
import tkinter as tk
from tkinter import *

def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/alfya/Desktop/DE ROAD/PythonPractice/TKinter/Media/505song.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

def stop_audio():
    pygame.mixer.music.stop()


root = tk.Tk()
root.geometry('500x300')
root.title("505 - Arctic Monkeys")

play_button = Button(root, text = "Play", command = play_audio)
play_button.pack(side = "left", padx = 20)

stop_button = Button(root, text = "Stop", command = stop_audio)
stop_button.pack(side = "left", padx = 20)

root.mainloop()
