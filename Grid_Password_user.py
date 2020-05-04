
from tkinter import *

root=Tk()

root.geometry("180x80")

def getval():
    print("User value : %s"%uservalue.get())
    print("User value : %s"%passvalue.get())

user=Label(root,text="user").grid()
password=Label(root,text="Password").grid()

uservalue=StringVar()
passvalue=StringVar()

userinput=Entry(root,textvariable=uservalue).grid(row=0,column=1)
passinput=Entry(root,textvariable=passvalue).grid(row=1,column=1)

Button(root,text="Submit",command=getval).grid()
root.mainloop()