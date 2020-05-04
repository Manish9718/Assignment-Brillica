
from tkinter import *
root = Tk()
root.geometry("1000x399")
root.title("Sumit GUI")
root.minsize(400, 300)


# # Important Label Options
# # text - adds the text
# # bg - background
# # fg - foreground
# # font - sets the font
# # 1. font=("comicsansms", 19, "bold")
# # 2. font="Helvetica 19 bold"
#borderwidth = text border width
# # padx - x padding
# # pady - y padding
# # relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE
#
title_label = Label(text="""As with most other modern Tk bindings,
                         \n Tkinter is implemented as a Python wrapper around a complete Tcl interpreter
                         \n embedded in the Python interpreter. \n Tkinter calls are translated into Tcl commands
                         \n which are fed to this embedded interpreter, thus making it possible to mix Python
                         \n and Tcl in a single application.""", bg = 'red',  fg = 'white',
                        padx= 25, pady = 35,font =("comicsansms", 19, "bold"), borderwidth =3,
                        relief = SUNKEN)

#for different colours: https://flatuicolors.com/palette/us
# title_label.pack()

# # Important Pack options
# # anchor = nw
# # side = top, bottom, left, right
# # fill
# # padx
# # pady
#side=BOTTOM
# , fill="x"  : it means when we use fill=tk.x then it will expend upto the extended width of the screen
# fill=Tk."y": 


# title_label.pack(anchor ="n",side = RIGHT,fill= Y)
title_label.pack(side=LEFT, padx=150, pady=150)

root.mainloop()


