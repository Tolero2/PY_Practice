#import everything from tkinter
from tkinter import *
from tkinter.ttk import *
#create Window object
window=Tk()
#All window objects must be declared between those lines (Tk() & mainloop())

#define four labels title Author Year ISBN

l1=Label(window, text= "Title" )
#use grid method to define the row/column number to place the widget.
l1.grid(row=0,column=0)#,columnspan=2,rowspan=2, padx=5,pady=5, sticky="w")

l2=Label(window, text= "Author" )
l2.grid(row=0,column=2)

l3=Label(window, text= "Year" )
l3.grid(row=1,column=0)

l4=Label(window, text= "ISBN" )
l4.grid(row=1,column=2)

#define Entries// text area to receive input and store in a defined variable (StringVar())

titleText=StringVar()
e1=Entry(window,textvariable=titleText)
e1.grid(row=0, column=1)

authorText=StringVar()
e2=Entry(window,textvariable=authorText)
e2.grid(row=0, column=3)

yearText=StringVar()
e3=Entry(window,textvariable=yearText)
e3.grid(row=1, column=1)

isbnText=StringVar()
e4=Entry(window,textvariable=isbnText)
e4.grid(row=1, column=3)

#define ListBox
list1=Listbox(window,height=5,width=30)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

#Attach scrollbar to the list Box
sb1= Scrollbar(window,orient="vertical")
sb1.grid(row=2,column=2,rowspan=6)

#assign the scrollbar to the ListBox specifically
list1.config(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#define buttons
b1=Button(window,text="View All",width=12)
b1.grid(row=2,column=3)

b2=Button(window,text= "Search Entry",width=12)
b2.grid(row=3,column=3)

b3=Button(window,text= "Add Entry",width=12)
b3.grid(row=4,column=3)

b4=Button(window,text= "Update selected",width=12)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected",width=12)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12)
b6.grid(row=7,column=3)

window.mainloop()


#Problem State: Recheck the scrollbar widget, it is implemnted differently.