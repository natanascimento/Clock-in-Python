#Copyright (c) 2019 Natan Nascimento Oliveira Matos <natanascimentom@outlook.com>
#Clock using Tkinter 

from tkinter import *
from time import strftime

#For make the clock function
def clock():
    def clock_main():
        main_structure["text"] = strftime("%H:%M:%S")
    def counter():
        clock_main()
        root.after(1000,counter)
    counter()

#Interface structure
root = Tk()
#Structure for plot the clock on GUI
main_structure = Label(root, text = "--:--:--")
main_structure["font"] = ("Dubai Medium", "25", "bold", "roman")
main_structure.pack()

#For enable the clock 
clock()

#For scale the interface ("LxA+E+T")
root.geometry("150x50+50+50")
#To insert the title in the GUI
root.title("Clock")
#If haven't "mainloop", in this code, the program stop in the clock function, and not would tell the seconds
root.mainloop()