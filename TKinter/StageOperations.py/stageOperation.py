import tkinter as tk                  # Import the base Tkinter module
from tkinter import messagebox        # For the confirmation dialog box
from PIL import Image, ImageTk        # To handle .png images for window icon

# Function to handle the close button (X on window)
def on_closing():
    # Show confirmation dialog before exiting
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()  # Close the application

# Function to center the window on screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()    # Get screen width
    screen_height = window.winfo_screenheight()  # Get screen height
    x = (screen_width - width) // 2              # Calculate x position
    y = (screen_height - height) // 2            # Calculate y position
    window.geometry(f"{width}x{height}+{x}+{y}") # Set geometry with offset

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Stage Operation Example")

# Center the window with a size of 600x400
center_window(root, 600, 400)

# Make the window non-resizable (fixed size)
root.resizable(False, False)

# Load a .png image to use as the window icon
icon_img = ImageTk.PhotoImage(file="C:/Users/alfya/Desktop/DE ROAD/PythonPractice/TKinter/Media/test2.png")  # Replace with your icon path
root.iconphoto(False, icon_img)  # Set the window icon

# Set custom behavior when user clicks the close (X) button
root.protocol("WM_DELETE_WINDOW", on_closing)

# Add an Exit button that also closes the window
tk.Button(root, text="Exit", command=root.destroy).pack(pady=20)

# Start the Tkinter main event loop
root.mainloop()
