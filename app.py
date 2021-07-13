import tkinter as tk
import time
from tkinter import *
from tkinter import filedialog

from data import * 

def get_column_name():
    global c_name
    c_name = player_name.get()
    column_label = Label(root, text=f'{c_name} is the column header, thanks!', bg='#ffbf00')
    column_label.pack()


#Browse File Functions using imported filedialog module
def browseFiles():
    #Sets the acceptable filetypes to CSV and Excel Files
    filetypes = (
        ("Excel Files", "*.xlsx*"),
        )
    #Opens up the file dialog menu in which the user can only choose an Excel file
    filename = filedialog.askopenfilename(title = "Select a file", filetypes = filetypes)
    
    #Uses Pandas and OpenPYXL
    x = False
    try:
        x = clean(filename, c_name)
    except NameError:
        error = Label(root, text = "Please enter column name before choosing file!", width = 100, height = 10, fg = "white", bg = "black", font = ("Arial"))
        error.pack()
    
    #Changes label that has been packed into window to new message of "File Opened" after user chooses a file

    if x == True:
        label.configure(text="File has successfully been opened!")

        graph_button = Button(
            root,
            text="Click for Graph of possible typos!", 
            padx=10, 
            pady=25,
            command = show_graph
        ).pack()

#Creating Window

if __name__ == '__main__':
    root = Tk()
    root.title("Automating Email Typo Detection Tool")
    root.geometry("1024x768")
    root.config(background = "white")

    #Creating Label
    label = Label(root, text = "Automating Email Typo Detection", width = 100, height = 10, fg = "white", bg = "black", font = ("Arial", 24))
    #Packing Label into Window
    label.pack()

    #Creating Type-In Thing

    player_name = Entry(root)
    player_name.pack(pady=30)


    #Creating column name button
    column_name = Button(
        root,
        text="Enter (Please ensure that the column name is correct (case sensitive + spelled correctly)!", 
        padx=10, 
        pady=5,
        command=get_column_name
    ).pack()

    #Creating File Browser Button
    button_browse = Button(root, 
                    text = "Choose File", 
                    command = browseFiles, 
                    height = 5, 
                    width = 10)

    #Packing File Browser Button into Window
    button_browse.pack(side=tk.LEFT, padx=5, pady=5)

    #Creating Exit Button
    button_escape = Button(root, 
                        text = "Exit", 
                        command = exit, 
                        height = 5, 
                        width = 10)

    #Packing Exit Button into Window
    button_escape.pack(side=tk.RIGHT, padx=5, pady=5)

    #Ends Window Loop
    root.mainloop()