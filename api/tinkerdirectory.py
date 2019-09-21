import tkinter
from tkinter import filedialog



def opendialog():
   root = tkinter.Tk()
   root.withdraw()
   dirname = tkinter.filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
   return dirname
