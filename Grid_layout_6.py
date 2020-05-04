
from tkinter import *

def getvals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")


root = Tk()
root.geometry("655x333")

user = Label(root, text="Username")
password = Label(root, text="Password")
# user.pack()
# password.pack()
user.grid()
password.grid()

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()


# # Entry Widgets of Tk class
#
userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)
#
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)
#
Button(text="Submit", command=getvals).grid()


root.mainloop()

or


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
