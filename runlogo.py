"""
This script will take a .txt or maybe a .logo file and will
return a png picture of the result of running that script.
I am making my own language!
"""
from PIL import Image, ImageTk
import numpy as np
import tkinter as tk

class LogoGrid():
    def __init__(self, sizeX, sizeY, color = [255, 255, 255]):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.grid = []
        line = []
        x = 0
        y = 0
        while y < self.sizeY:
            while x < self.sizeX:
                line.append(color)
                x += 1
            self.grid.append(line)
            line = []
            y += 1
            x = 0
    def save(self, file):
        array = np.array(grid.grid, dtype=np.uint8)
        image = Image.fromarray(array)
        image.save(file)
    def getimage(self):
        array = np.array(grid.grid, dtype=np.uint8)
        image = Image.fromarray(array)
        return ImageTk.PhotoImage(image)

class LogoTurtle():
    def __init__(self, position = [0, 0, 0], facing = 90, pendown = 1, visible = 0):
        self.position = position
        self.facing = facing
        self.pendown = pendown
        self.visible = visible

grid = LogoGrid(500, 500)
grid.save('test.png')

root = tk.Tk()
img = grid.getimage()
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()


