from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubbleSort


root = Tk()
root.title("Visualizing Sorting Algorithms")
root.maxsize(900, 600)
root.config(bg = "black")


# variable
selected_alg = StringVar()
data = []


def drawData(data, colorList):
    canvas.delete("all")
    c_height = 380
    c_width = 550
    x_width = c_width / (len(data) + 1)
    offset =30
    spacing = 10
    normalizedData = [i/max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill = colorList[i])
        canvas.create_text(x0 + 2, y0, anchor = SW, text = str(data[i]))
    root.update_idletasks()

def generate():
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal + 1))
    
    drawData(data, ["red" for i in range(len(data))])


def startAlgorithm():
    global data
    bubbleSort(data, drawData, speedScale.get())


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

speedScale = Scale(UI_frame, from_ = 0.1, to = 2.0, length = 200, digits = 2, resolution = 0.2, orient = HORIZONTAL)
speedScale.grid(row = 0, column = 2, padx = 5, pady = 5)
Button(UI_frame, text = "Start", command = startAlgorithm, bg = "red").grid(row = 0, column = 3, padx = 5, pady = 5)


# Row 1
sizeEntry = Scale(UI_frame, from_ = 5, to = 40, resolution = 1, orient = HORIZONTAL, label = "Data Size")
sizeEntry.grid(row = 1, column = 0, padx = 5, pady = 5)

minEntry = Scale(UI_frame, from_ = 0, to = 10, resolution = 1, orient = HORIZONTAL, label = "Min Size")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_ = 10, to = 100, resolution = 1, orient = HORIZONTAL, label = "Max Size")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text = "Generate", command = generate, bg = "white").grid(row = 1, column = 3, padx = 5, pady = 5)



root.mainloop()