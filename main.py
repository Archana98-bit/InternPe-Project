from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()          #creating tkinter window
root.title('Clock')

def time() :
    string = strftime('%H: %M: %S %p')
    label.config(text = string)  #display time on the label
    label.after(1000, time)

label = Label(root, font=('calibri', 40, 'bold'), background='blue', foreground='white')  #styling the label widget

label.pack(anchor = 'center')   #placing clock at the center of the tkinter window
time()

mainloop()
