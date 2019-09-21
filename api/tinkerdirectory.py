import tkinter
from tkinter import filedialog
import os

def opendialog():
   root = tkinter.Tk()
   root.withdraw()
   currdir = os.getcwd()
   dirname = tkinter.filedialog.askdirectory(parent=root,initialdir=currdir,title='Please select a directory')
   return dirname
