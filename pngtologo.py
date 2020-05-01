#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image

input_file = "test.png"
output_file = "test.txt"

im = Image.open(input_file, "r")

pix_val = list(im.getdata())
size = im.size
im.close()
for pixel in range(20):
    print (pix_val[pixel])

print (im.size)
