from tkinter import *

master = Tk()
w = Canvas(master, bg='white', width = 400, height = 400)
w.pack()

x = 0
y = 400
n = 30
size = 400 / n

for i in range(0, n):
    # w.create_line(x, 0, 0, y, fill = "#DB2B22")
    w.create_line(x, 0, 0, y, fill = "#DB2B22")
    x += size
    y -= size

mainloop()
