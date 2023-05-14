#Import evrything from tkinter // import ttk wrapper
from re import I
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#define general Background and Foreground color
bg="grey"
fg="#FFFFFF"


#Define enter data function that will get executed when the button is clicked,
def enterData():
    #User info data
    firstName=firstnameVar.get()
    lastName=lastnameVar.get()
    title=title_combobox.get()
    age=age_spinbox.get()
    nationality=nationality_combobox.get()

    #User Registration info
    registrationStatus=registrationVar.get()
    courses=courses_spinbox.get()
    semesters=semester_spinbox.get()

    #User Terms and Conditions
    tANDc=termsConditionVar.get()

    #Business Logic 1 // All User must agree to Terms and Conditions
    if (tANDc=="Accepted"):
        if firstName and lastName:
            print("First Name: {} Last Name: {} Title: {} Age: {}".format(firstName,lastName,title,age))
            print(registrationStatus)
            messagebox.showinfo(title="Success",message="Successfully Entered your data")
        else:
            messagebox.showwarning(title="Error",message="First Name and Last Name is required")
    else:
        messagebox.showwarning(title="Error", message="Please accept the Terms and Conditions to continue")


window=Tk()
window.title("TKINTER DATA ENTRY FORM")
window.geometry("500x500")
window.configure(bg=bg)

#Configure frame for App window
frame=Frame(window,bg=bg)
frame.pack()

#Configure Label frames to group different data logic
userInfo_labelFrame=LabelFrame(frame,bg=bg,text="User Information")
userInfo_labelFrame.grid(row=0,column=0)
registration_labelFrame=LabelFrame(frame,bg=bg)
registration_labelFrame.grid(row=1,column=0)
termsConditions_labelFrame=LabelFrame(frame,bg=bg,text="Terms & Conditions")
termsConditions_labelFrame.grid(row=2,column=0)


##Add all WIDGETS to respective Label Frames


#User Information L-frame WIDGETS
#Labels
firstName_label=Label(userInfo_labelFrame,bg=bg,text="First Name")
firstName_label.grid(row=0,column=0)
lastName_label=Label(userInfo_labelFrame,bg=bg,text="Last Name")
lastName_label.grid(row=0,column=1)
title_label=Label(userInfo_labelFrame,bg=bg,text="Title")
title_label.grid(row=0,column=2)
age_label=Label(userInfo_labelFrame,bg=bg,text="Age")
age_label.grid(row=2,column=0)
nationality_label=Label(userInfo_labelFrame,bg=bg,text="Nationality")
nationality_label.grid(row=2,column=1)

#Entries
firstnameVar=StringVar()
firstName_entry=Entry(userInfo_labelFrame,textvariable=firstnameVar,bg=bg)
firstName_entry.grid(row=1,column=0)
lastnameVar=StringVar()
lastName_entry=Entry(userInfo_labelFrame,textvariable=lastnameVar,bg=fg,insertbackground=bg,fg=bg)
lastName_entry.grid(row=1,column=1)

#ComboBox // using Themed tkinter(ttk) wrapper
title_combobox=ttk.Combobox(userInfo_labelFrame,background=bg,values=("","Mr.","Mrs.","Ms."))
title_combobox.grid(row=1,column=2)
nationality_combobox=ttk.Combobox(userInfo_labelFrame,background=bg,values="")
nationality_combobox.grid(row=3,column=1)

#SpinBox
age_spinbox=Spinbox(userInfo_labelFrame,bg=bg,from_=18,to=110)
age_spinbox.grid(row=3,column=0)


#Registration L-frame WIDGETS

#Labels
registrationStat_label=Label(registration_labelFrame,bg=bg,text="Registration Status")
registrationStat_label.grid(row=0,column=0)
courses_label=Label(registration_labelFrame,bg=bg,text="# Completed Courses")
courses_label.grid(row=0,column=1)
semester_label=Label(registration_labelFrame,bg=bg,text="# Semesters")
semester_label.grid(row=0,column=2)

#Check Buttons
registrationVar=StringVar(value="Not Registered")
registration_checkbox=Checkbutton(registration_labelFrame,bg=bg,text="Currently Registered",variable=registrationVar,onvalue="Registered",offvalue="Not Registered")
registration_checkbox.grid(row=1,column=0)

#SpinBox
courses_spinbox=Spinbox(registration_labelFrame,bg=bg,from_=0,to='infinity')
courses_spinbox.grid(row=1,column=1)
semester_spinbox=Spinbox(registration_labelFrame,bg=bg,to=8)
semester_spinbox.grid(row=1,column=2)


#Terms & Conditions L-frame WIDGETS
#Check Buttons
termsConditionVar=StringVar(value="Not Accepted")
termsConditions_checkbox=Checkbutton(termsConditions_labelFrame,bg=bg,text="I accept the terms and conditions.",variable=termsConditionVar,onvalue="Accepted",offvalue="Not Accepted")
termsConditions_checkbox.grid(row=0,column=0)

#Add data button frame WIDGET

#Button
enterData_button=Button(frame,text="Enter Data",bg=bg,height=2,command=enterData)

##Add general configuration to the widgets and Frame labels

#Configure addition grid parameters on the Window  Label Frames
for frames in frame.winfo_children():
    frames.grid_configure(padx=20,pady=10,sticky="news")


#Configure addition grid parameters on the Label frame's widgets
for widgets in (userInfo_labelFrame.winfo_children(),registration_labelFrame.winfo_children(),termsConditions_labelFrame.winfo_children()):
    for widget in widgets:
        widget.grid_configure(padx=10,pady=5)


window.mainloop()