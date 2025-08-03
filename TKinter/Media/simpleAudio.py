#pip install pygame

import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("C:/Users/alfya/Desktop/DE ROAD/PythonPractice/TKinter/Media/505song.mp3")
pygame.mixer.music.play()


print("Press Enter to stop the music...")
input()  # Wait for user to press Enter
pygame.mixer.music.stop()

