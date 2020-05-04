#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from pathlib import Path
import tkinter as tk

def png_to_logo(png_file, final_dimensions = [500, 500]):

    im = Image.open(input_file, "r")
    pix_val = list(im.getdata())
    size = im.size
    im.close()

    multiplier = [final_dimensions[0] / size[0], final_dimensions[1] / size[1]]
    commands = ["pu home setpensize " + str(multiplier[1]) + " fd " + str(size[1]*multiplier[1]/2) + " rt 90 bk " + str(size[0]*multiplier[0]/2) + " pd"]
    x = 0
    y = 0

    for pixel in pix_val:
        commands.append("color [" + str(pixel[0]) + " " + str(pixel[1]) + " " + str(pixel[2]) + "] fd " + str(multiplier[0]))
        x += 1
        if x == size[0]:
            x = 0
            y += 1
            commands.append("pu bk " + str(size[0]*multiplier[0]) + " rt 90 fd " + str(multiplier[1]) + " lt 90 pd")

    # result = commands[0] + "\n"
    # for line in range(1, len(commands)):
    #     if commands[line] == commands[line-1]:
    #         i = 0
    #         while

    result = ""
    for line in commands[0:-1]:
        line += "\n"
        result += (line)
    return result

if __name__ == "__main__":
    directory_path = str(Path(__file__).parent.absolute()) + "/"
    input_file = "test.png"
    output_file =  str(input_file.split(".")[0:-1][0]) + ".txt"

    with open(output_file, "w") as fileout:
        fileout.write(png_to_logo(input_file))

    from tkinter import *

    window = Tk()
    window.title("Logo Converter")
    window.geometry('350x200')
    lbl = Label(window, text="CONVERT IMAGE TO LOGO")
    lbl.grid(column=0, row=0)
    btn = Button(window, text="Click Me")
    btn.grid(column=0, row=1)
    window.mainloop()
