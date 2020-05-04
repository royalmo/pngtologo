#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from pathlib import Path

directory_path = str(Path(__file__).parent.absolute()) + "/"
input_file = "test.png"
output_file =  str(input_file.split(".")[0:-1][0]) + ".txt"
multiplier = 2.5

im = Image.open(input_file, "r")

pix_val = list(im.getdata())
size = im.size
print(size)
im.close()

result = "pu setpensize " + str(multiplier) + " fd " + str(size[1]*multiplier/2) + " rt 90 bk " + str(size[0]*multiplier/2) + " pd\n"
x = 0
y = 0
for pixel in pix_val:
    result += "color [" + str(pixel[0]) + " " + str(pixel[1]) + " " + str(pixel[2]) + "] fd " + str(multiplier) + " "
    x += 1
    if x == size[0]:
        x = 0
        y += 1
        result += "pu bk " + str(size[0]*multiplier) + " rt 90 fd " + str(multiplier) + " lt 90 pd\n"

with open(output_file, "w") as fileout:
    fileout.write(result)
