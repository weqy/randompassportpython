import tkinter as tk
from datetime import datetime
from datetime import date
import random
from tkinter import *

root = tk.Tk()
canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Passport Generator')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)


def randomIdentity():
    nameChoose = ['Bernhard Dermott', 'Beyoncé Knowles', 'Steve Harrington', 'Joe Ivarson', 'John Doe', 'Jane Doe',
                  'Jim Hopper', 'Joyce Byers', 'Mike Wheeler', 'Lucas Sinclair', 'Maxine Mayfield', 'Erica Sinclair']
    purpose = ['Tourism', 'Business', 'Study', 'Other']
    placeChoose = ['India', 'Ukraine', 'France', 'Spain', 'Germany', 'China']
    documentChoose = ['Passport', 'Passport Card', 'Foreign Passport']

    monthChoose = list(range(1, 13))
    dayChoose = list(range(1, 30))
    yearChoose = list(range(1960, 2000))

    monthBirth = random.choice(monthChoose)
    dayBirth = random.choice(dayChoose)
    yearBirth = random.choice(yearChoose)

    name = random.choice(nameChoose)
    visitPurpose = random.choice(purpose)
    placeBirth = random.choice(placeChoose)
    documentType = random.choice(documentChoose)

    def age(birthdate):
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

    ageResult = (age(date(yearBirth, monthBirth, dayBirth)))

    canvas1.delete("all")  # to clear the tk window
    label1 = tk.Label(root, text='Passport Generator')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(200, 25, window=label1)

    canvas1.create_window(200, 80, window=button1)  # to create the new button after clear tk window

    myDocument = tk.Label(root, text=documentType, font=('helvetica', 10), anchor='w', width=15)
    canvas1.create_window(180, 130, window=myDocument)

    myName = tk.Label(root, text=name, font=('helvetica', 10), anchor='w', width=15)
    canvas1.create_window(180, 150, window=myName)

    myDOB = tk.Label(root, text=str(monthBirth) + '/' + str(dayBirth) + '/' + str(yearBirth), font=('helvetica', 10),
                     anchor='w', width=15)
    canvas1.create_window(180, 170, window=myDOB)

    myAge = tk.Label(root, text=str(ageResult), font=('helvetica', 10), anchor='w', width=15)
    canvas1.create_window(180, 190, window=myAge)

    myPOB = tk.Label(root, text=str(placeBirth), font=('helvetica', 10), anchor='w', width=15)
    canvas1.create_window(180, 210, window=myPOB)

    myPurpose = tk.Label(root, text=visitPurpose, font=('helvetica', 10), anchor='w', width=15)
    canvas1.create_window(180, 230, window=myPurpose)

    sampleText = tk.Label(root, text='Document', font=('helvetica', 10), anchor='w', width=11)
    canvas1.create_window(60, 130, window=sampleText)

    sampleText2 = tk.Label(root, text='Name', font=('helvetica', 10), anchor='w', width=11)
    canvas1.create_window(60, 150, window=sampleText2)

    sampleText3 = tk.Label(root, text='DOB', font=('helvetica', 10), anchor='w', width=11)
    canvas1.create_window(60, 170, window=sampleText3)

    sampleText4 = tk.Label(root, text='Age', font=('helvetica', 10), anchor='w', width=11)
    canvas1.create_window(60, 190, window=sampleText4)

    sampleText5 = tk.Label(root, text='POB', font=('helvetica', 10), anchor='w', width=11)
    canvas1.create_window(60, 210, window=sampleText5)

    sampleText6 = tk.Label(root, text='Purpose of visit', font=('helvetica', 10), anchor='w', width=11)
    canvas1.create_window(60, 230, window=sampleText6)


button1 = tk.Button(text='Generate Passport', command=randomIdentity, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))

canvas1.create_window(200, 80, window=button1)

root.mainloop()
