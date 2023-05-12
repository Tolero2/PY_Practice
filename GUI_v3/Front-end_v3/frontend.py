#import everything from tkinter
from datetime import date
import datetime
from tkinter import *
from tkinter import messagebox
#from tkinter.ttk import *

#create Window object
window=Tk()
#All window objects must be declared between those lines (Tk() & mainloop())

#define window scope/logic
window.title("Pratice Login window")
window.geometry("340x440")
window.configure(bg= "violet")

#Message inbox takes the return arg and parse in into built-in window to categorize and display the value.


def login():
    sampleUser= "sample"
    samplePass="sample"
    if (usernameVar.get()== sampleUser and passwordVar.get()==samplePass):
        messagebox.showinfo(title="Success",message="Successfully logged in!!!")
        logStash=f'Success on Login \n Time:  \n User: {sampleUser}'
        print(logStash)

    else:
        messagebox.showerror(title="Error",message="Not logged in Da pa da!!!")
        logStash=f'Error on Login \n Time:   \n User: {usernameVar.get()}'
     


#Create frame to box all widget and grid manager into the pack class. this particularly enable the pack INTERACTIVE WINDOW feature on the app.
frame=Frame(bg="violet")

#Creating all WIDGETS types
#Labels WIDGET
login_label=Label(frame,text="Login",bg="violet",fg="dark blue",font=("Arial",30))
username_label=Label(frame,text="Username",bg="violet",fg="black",font=("Arial",16))
password_label=Label(frame,text ="Password",bg="violet",fg="black",font=("Arial",16))

#Entries WIDGET
usernameVar=StringVar()
username_entry=Entry(frame,textvariable=usernameVar,bg="violet")

passwordVar=StringVar()
password_entry=Entry(frame,textvariable=passwordVar, show="*",bg="violet")

#Button WIDGET
login_button=Button(frame,text="LOGIN",fg="dark blue",bg="violet",font=("Arial",16),command=login)

#Placing WIDGETS of all types on the frame screen (window)
login_label.grid(row=0,column=0,columnspan=2,sticky="news",pady=60)
username_label.grid(row=1,column=0)
password_label.grid(row=2,column=0)
username_entry.grid(row=1,column=1,pady=30)
password_entry.grid(row=2,column=1,pady=30)
login_button.grid(row=4,column=1,pady=20)

#Pack the framed window(screen) as one bundle onto the main Window screen to make  it interactive
frame.pack()


window.mainloop()
print(usernameVar.get())
print(passwordVar.get())
