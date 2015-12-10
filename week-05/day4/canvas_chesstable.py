from tkinter import *
import math

master = Tk()
w = Canvas(master, bg='#fff', width = 400, height = 400)
w.pack()

size = 30
horiz = 6
vert = 8
row = 0
col = 0

for i in range(1, horiz * vert + 1):
    row = math.ceil(i / horiz)
    col = i - horiz * (row - 1)

    color = "#ECF0F1"
    if (row + col) % 2 == 0:
        color = "#DB2B22"

    offsetX = (col - 1) * size
    offsetY = (row - 1) * size
    w.create_rectangle(offsetX, offsetY, offsetX + size, offsetY + size, fill = color)

mainloop()
