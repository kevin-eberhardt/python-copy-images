from tkinter import filedialog
from tkinter import *
import os

def get_dir(directory, name):
    flist = os.listdir(directory)
    if(name == "source"):
        print("Im Source-Ordner:")
    elif (name == "dest"):
        print("Im Destination-Ordner:")
    else:
        print("Select folder")
    for element in flist:
        print(element)

def browse_source():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global source_path
    filename = filedialog.askdirectory()
    get_dir(filename, "source")
    source_path.set(filename)
    print(filename)

def browse_destination():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global destination_path
    filename = filedialog.askdirectory()
    get_dir(filename, "dest")
    destination_path.set(filename)
    print(filename)

def make_label(input):
    label = Label(master=root, text=input)
    return label

root = Tk()
s = Label(master=root, text="Select source:")
s.grid(row=0, column=1)
d = Label(master=root, text="Select destination:")
d.grid(row=1, column=1)
destination_path = StringVar()
source_path = StringVar()
source_lbl = Label(master=root,textvariable=source_path)
destination_lbl = Label(master=root,textvariable=destination_path)
button1 = Button(text="Browse", command=browse_source)
button1.grid(row=0, column=3, columnspan=2)
button2 = Button(text="Browse", command=browse_destination)
button2.grid(row=1, column=3, columnspan=2)
a1 = Label(master=root, text="Source:")
a1.grid(row=2, column=1)
source_lbl.grid(row=2, column=2)
b = Label(master=root, text="Destination:")
b.grid(row=3, column=1)
destination_lbl.grid(row=3, column=2)
mainloop()