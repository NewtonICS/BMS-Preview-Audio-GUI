# Subprocess needed to run commandline args.
import subprocess

# Tkinter imports
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

# Main window initialization.
root = Tk()
root.title("BMS Preview Gen (GUI)")

# Initial window size
# Scalable elements are a pain, so ¯\_(ツ)_/¯
root.geometry("350x100")

# Global folder_selected initialization.
# Contains the folder that will be processed.
folder_selected = None
folderString = StringVar()
folderString.set(" ")
folderLabel = Label(root, textvariable=folderString).grid(row=3, column=0,pady=5,columnspan=4)

# Function to run the commandline args.
def generatePreviews():
    global folder_selected
    global startval
    global endval
    global folderLabel
    if (folder_selected == None):
        folderString.set("Choose a folder first.")
    else:
        foldername = "-path=\"" + str(folder_selected) + "\""
        startname = "-start=\"" + str(spinval.get()) + "\""
        endname = "-end=\"" + str(spinval2.get()) + "\""
        folderFinal = ".\BmsPreviewAudioGenerator.exe -batch " + foldername + " " + startname + " " + endname + " -support_extend_format"
        # print(folderFinal) ***debug only***
        subprocess.run(folderFinal)
        #[".\BmsPreviewAudioGenerator.exe", "-batch", foldername, startname, endname, "-support_extend_format"]

# Function to get the folder info.
def getFolder():
    global folder_selected
    global folderLabel
    folder_selected = filedialog.askdirectory()
    messagebox.showinfo("Folder Info", folder_selected)
    folderString.set(str(folder_selected))
    

# Spinboxes for the start and end times.
spinval = StringVar(root)
spinval2 = StringVar(root)
spinval.set(20000) # Default value.
spinval2.set(45000) # Default value.
startLabel = Label(root, text="Start time(ms): ").grid(row=1, column=0)
startval = ttk.Spinbox(root, from_=1000, to=30000, increment=500, textvariable=spinval, width=7).grid(row=1, column=1, pady=5)
endLabel = Label(root, text="End time(ms): ").grid(row=1, column=2,pady=5)
endval = ttk.Spinbox(root, from_=40000, to=70000, increment=500, textvariable=spinval2, width=7).grid(row=1, column=3,pady=5)

# Buttons for generation and folder selection.
generatorButton = Button(root, text= "Generate Previews", command=generatePreviews).grid(row=2,column=0,padx=5,pady= 5)
folderButton = Button(root, text="Choose Folder", command=getFolder).grid(row=2,column=2,padx=5,pady=5)

# Main program loop.
root.mainloop()
