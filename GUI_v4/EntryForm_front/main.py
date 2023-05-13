#Import evrything from tkinter
from tkinter import *
bg="#333333"
fg="#FFFFFF"
window=Tk()
window.title("TKINTER DATA ENTRY FORM")
window.geometry("500x500")
window.configure(bg=bg)

#Configure frame for App window
frame=Frame(window,bg=bg)
frame.pack()

#Configure Label frames to group different data logic
userLabelFrame=LabelFrame(frame,bg=bg,text="User Information")
userLabelFrame.grid(row=0,column=0)
registrationLabelFrame=LabelFrame(frame,bg=bg)
registrationLabelFrame.grid(row=1,column=0)
t_cLabelFrame=LabelFrame(frame,bg=bg,text="Terms & Conditions")
t_cLabelFrame.grid(row=2,column=0)

#Add WIDGETS to respective Label Frames

#User Information frame WIDGETS
#Labels
firstName_label=Label(userLabelFrame,bg=bg,text="First Name")
firstName_label.grid(row=0,column=0)
lastName_label=Label(userLabelFrame,bg=bg,text="Last Name")
lastName_label.grid(row=0,column=1)
title_label=Label(userLabelFrame,bg=bg,text="Title")
title_label.grid(row=0,column=2)
age_label=Label(userLabelFrame,bg=bg,text="Age")
age_label.grid(row=2,column=0)
nationality_label=Label(userLabelFrame,bg=bg,text="Nationality")
nationality_label.grid(row=2,column=1)

#Entries
firstName_entry=Entry(userLabelFrame,bg="#FFFFFF")
firstName_entry.grid(row=1,column=0)
lastName_entry=Entry(userLabelFrame,bg="#FFFFFF")
lastName_entry.grid(row=1,column=1)

#Registration frame WIDGETS
#Labels
registrationStat_label=Label(registrationLabelFrame,bg=bg,text="Registration Status")
registrationStat_label.grid(row=0,column=0)
courses_label=Label(registrationLabelFrame,bg=bg,text="# Completed Courses")
courses_label.grid(row=0,column=1)
semester_label=Label(registrationLabelFrame,bg=bg,text="# Semesters")
semester_label.grid(row=0,column=2)

#Check Buttons
registration_checkbox=Checkbutton(registrationLabelFrame,bg=bg,text="Currently Registered")
registration_checkbox.grid(row=1,column=0)

#DropDown Buttons
courses_dropdown=""



window.mainloop()