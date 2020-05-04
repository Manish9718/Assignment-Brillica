from tkinter import *

root = Tk()

root.geometry("655x333")


f1 = Frame(root, bg="#0984e3", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")


f2 = Frame(root, borderwidth=8, bg="#00cec9", relief=SUNKEN)
f2.pack(side=TOP, fill="x")


l = Label(f1, text="Project Tkinter - Pycharm",fg="#f1c40f")
l.pack( pady=142)


l = Label(f2, text="Welcome to sublime text", font="Helvetica 16 bold", fg="#f1c40f", pady=22)
l.pack()

root.mainloop()
