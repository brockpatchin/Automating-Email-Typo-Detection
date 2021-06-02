import tkinter as tk
from tkinter import *
from tkinter import filedialog

from data import clean

#Browse File Functions using imported filedialog module
def browseFiles():
    #Sets the acceptable filetypes to CSV and Excel Files
    filetypes = (
        ("Excel Files", "*.xlsx*"), 
        ("CSV Files", "*.csv*")
        )
    #Opens up the file dialog menu in which the user can only choose an Excel or a CSV File
    filename = filedialog.askopenfilename(title = "Select a file", filetypes = filetypes)
    
    
    #Gets Actual Name of File
    x = filename.split("/")
    realFileName = x[len(x) - 1]

    #Uses Pandas and OpenPYXL

    #Changes label that has been packed into window to new message of "File Opened" after user chooses a file
    label.configure(text="File has successfully been opened!")

#Creating Window
window = Tk()
window.title("Automating Email Typo Detection Tool")
window.geometry("1024x768")
window.config(background = "white")

#Creating Label
label = Label(window, text = "Automating Email Typo Detection", width = 256, height = 16, fg = "black", font = ("Arial", 24))

#Packing Label into Window
label.pack()


#Creating File Browser Button
button_browse = Button(window, text = "Choose File", command = browseFiles)

#Packing File Browser Button into Window
button_browse.pack()

#Creating Exit Button
button_escape = Button(window, text = "Exit", command = exit)

#Packing Exit Button into Window
button_escape.pack()

#Ends Window Loop
window.mainloop()