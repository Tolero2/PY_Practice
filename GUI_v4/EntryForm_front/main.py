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
user_labelFrame=LabelFrame(frame,bg=bg,text="User Information")
user_labelFrame.grid(row=0,column=0,sticky="news")
registration_labelFrame=LabelFrame(frame,bg=bg)
registration_labelFrame.grid(row=1,column=0,sticky="news",pady=15)
termsConditions_labelFrame=LabelFrame(frame,bg=bg,text="Terms & Conditions")
termsConditions_labelFrame.grid(row=2,column=0,sticky="news")

#Add WIDGETS to respective Label Frames

#User Information frame WIDGETS
#Labels
firstName_label=Label(user_labelFrame,bg=bg,text="First Name")
firstName_label.grid(row=0,column=0)
lastName_label=Label(user_labelFrame,bg=bg,text="Last Name")
lastName_label.grid(row=0,column=1)
title_label=Label(user_labelFrame,bg=bg,text="Title")
title_label.grid(row=0,column=2)
age_label=Label(user_labelFrame,bg=bg,text="Age")
age_label.grid(row=2,column=0)
nationality_label=Label(user_labelFrame,bg=bg,text="Nationality")
nationality_label.grid(row=2,column=1)

#Entries
firstName_entry=Entry(user_labelFrame,bg=bg)
firstName_entry.grid(row=1,column=0)
lastName_entry=Entry(user_labelFrame,bg=fg,insertbackground=bg,fg=bg)
lastName_entry.grid(row=1,column=1)

#Registration frame WIDGETS
#Labels
registrationStat_label=Label(registration_labelFrame,bg=bg,text="Registration Status")
registrationStat_label.grid(row=0,column=0)
courses_label=Label(registration_labelFrame,bg=bg,text="# Completed Courses")
courses_label.grid(row=0,column=1)
semester_label=Label(registration_labelFrame,bg=bg,text="# Semesters")
semester_label.grid(row=0,column=2)

#Check Buttons
registration_checkbox=Checkbutton(registration_labelFrame,bg=bg,text="Currently Registered")
registration_checkbox.grid(row=1,column=0)

#DropDown Buttons
courses_dropdown=""

#Terms & Conditions frame WIDGETS
#Check Buttons
termsConditions_checkbox=Checkbutton(termsConditions_labelFrame,bg=bg,text="I accept the terms and conditions.")
termsConditions_checkbox.grid(row=0,column=0)



window.mainloop()