import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win, bg="white", width=400, height=400)
for i in range (0, 400, 50):
    canvas.create_line((0, i), (400,i), fill="black")
for i in range (0, 400, 50):
    canvas.create_line((i,0), (i,400), fill="black")
for g in range (0, 400, 50):
    canvas.create_oval
canvas.pack()
win.mainloop()