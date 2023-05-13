#import everything from tkinter
from tkinter import *
import pyshorteners

#create Window object
window=Tk()
#All window objects must be declared between those lines (Tk() & mainloop())

#define window scope/logic
window.title("URL SHORTENER (tinyurl())")
window.geometry("340x200")
window.configure(bg= "#FFFFFF")

#Message inbox takes the return arg and parse in into built-in window to categorize and display the value.

#define the function for the button // implement the URL shortener logic using the (pyshorteners package) and inserting it into an output widget(ie. listbox)
def shortenUrl():
    shortenInstance=pyshorteners.Shortener()
    shorten_url=shortenInstance.tinyurl.short(enterUrlVar.get())
    OutputUrl_entry.insert(0,shorten_url)
    logStash=f'Log: \n Time: \n URL: {shorten_url}'
    print(logStash)


#Create frame to box all widget and grid manager into the pack class. this particularly enable the pack INTERACTIVE WINDOW feature on the app.
frame=Frame(bg="#FFFFFF")
frame.config(height=200,width=300)
#Creating all WIDGETS types
#Labels WIDGET
enterUrl_label=Label(frame,text="Enter URL to shorten",bg="#FFFFFF",fg="dark blue",font=("Arial",20))
outputUrl_label=Label(frame,text="Output shortened URL",bg="#FFFFFF",fg="dark blue",font=("Arial",20))

#Entries WIDGET
enterUrlVar=StringVar()
enterUrl_entry=Entry(frame,textvariable=enterUrlVar,fg="#FFFFFF")

OutputUrl_entry=Listbox(frame,fg="#FFFFFF",height=1)

#Button WIDGET
shortenUrl_button=Button(frame,text="Shorten URL",fg="dark blue",bg="#FFFFFF",font=("Arial",16),command=shortenUrl)

#Placing WIDGETS of all types on the frame screen (window)
enterUrl_label.grid(row=0,column=0)
enterUrl_entry.grid(row=1,column=0)
outputUrl_label.grid(row=2,column=0)
OutputUrl_entry.grid(row=3,column=0,pady=5)
shortenUrl_button.grid(row=4,column=0,pady=20)

#Pack the framed window(screen) as one bundle onto the main Window screen to make  it interactive
frame.pack()


window.mainloop()

