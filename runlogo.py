"""
This script will take a .txt or maybe a .logo file and will
return a png picture of the result of running that script.
I am making my own language!
"""
# class turtle - direction, position, pupd
# class pixelgrid - size, fill


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
            y += 1
            x = 0
        

