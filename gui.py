from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Visualizing Sorting Algorithms")
root.maxsize(900, 600)
root.config(bg = "black")

def generate():
    pass

# variable
selected_alg = StringVar()

# frame
UI_frame = Frame(root, width = 600, height = 200, bg="grey")
UI_frame.grid(row = 0, column = 0, padx = 10, pady = 5)

# canvas
canvas = Canvas(root, width = 600, height = 380, bg = "white")
canvas.grid(row = 1, column = 0, padx = 10, pady = 5)

# UI
# Row 0
Label(UI_frame, text = "Algorithm", bg = "grey").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)
algMenu = ttk.Combobox(UI_frame, textvariable = selected_alg, values = ["Bubble Sort", "Merge Sort"])
algMenu.grid(row = 0, column = 1, padx = 10, pady = 5)
algMenu.current(0) # default
Button(UI_frame, text = "Generate", command = generate, bg = "red").grid(row = 0, column = 2, padx = 5, pady = 5)


root.mainloop()