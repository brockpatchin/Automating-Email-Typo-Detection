import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title("Automating Email Typo Detection Tool")

window.geometry("1024x768")

greeting = tk.Label(
    text = "Hello! Welcome to the Automating Email Typo Detection Tool!",
    font=("Arial", 16)
)

greeting.pack()

file = filedialog.askopenfile(parent=window, mode='rb', title = 'Choose a file')
if file != None:
    data = file.read()

    readFile = tk.Label(text = "Your File has been read!", font=("Arial", 16))

    readFile.pack(anchor = 'center')

    file.close()




window.mainloop()