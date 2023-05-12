#import everything from tkinter
from tkinter import *
#from tkinter.ttk import *

#create Window object
window=Tk()
#All window objects must be declared between those lines (Tk() & mainloop())

#define window scope/logic
window.title("Pratice Login window")
window.geometry("340x440")
window.configure(bg= "violet")

def login():
    return print(usernameVar.get(),password_entry.get())

#Create frame to box all widget and grid manager into the pack class. this particularly enable the pack INTERACTIVE WINDOW feature on the app.
frame=Frame(bg="violet")

#creating WIDGETS
#Labels
login_label=Label(frame,text="Login",bg="violet",fg="dark blue",font=("Arial",20))
username_label=Label(frame,text="Username",bg="violet",fg="black",font=("Arial",16))
password_label=Label(frame,text ="Password",bg="violet",fg="black",font=("Arial",16))

#Entries
usernameVar=StringVar()
username_entry=Entry(frame,textvariable=usernameVar,bg="violet")

passwordVar=StringVar()
password_entry=Entry(frame,textvariable=passwordVar, show="*",bg="violet")

#Button
login_button=Button(frame,text="LOGIN",fg="dark blue",bg="violet",font=("Arial",16),command=login)

#Placing WIDGETS on the screen
login_label.grid(row=0,column=0,columnspan=2,pady=60)
username_label.grid(row=1,column=0)
password_label.grid(row=2,column=0)
username_entry.grid(row=1,column=1,pady=30)
password_entry.grid(row=2,column=1,pady=30)
login_button.grid(row=4,column=1,pady=20)

frame.pack()

window.mainloop()
print(username_entry)
print(passwordVar)
