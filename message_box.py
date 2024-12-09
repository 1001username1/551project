
# Author: Qianyi zhang   qizhang zhu
# Date: 2024.12.1
# Description: just to create a seperate for warning box


import tkinter
from tkinter import messagebox

def show_message(message):
    # create a hide window
    root = tkinter.Tk()
    root.withdraw()  # hide main window

    # pop out message
    messagebox.showinfo("Notification", message)

    # destroy
    root.destroy()
