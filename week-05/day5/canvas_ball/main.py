from tkinter import *
from ball import Ball

master = Tk()
c = Canvas(master, width = 400, height = 400)
c.pack()

ball = Ball((40, 50), (2, 2), 10)

while True:
    ball.move()
    c.create_oval(ball.get_bbox(), fill='#ffcc00')
    c.after(16)
    c.update()
    c.delete('all')

mainloop()
