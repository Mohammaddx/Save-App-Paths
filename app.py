import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title("Save Files Path")

apps = []

if os.path.isfile("savePaths.txt"):
    with open("savePaths.txt", "r") as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        apps = [x for x in tempApps if x.strip()]

## Functions
def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    fileName = filedialog.askopenfilename(initialdir = "/", title = "Select File",
                                          filetypes = (("executables", "*.exe"), ("all files", "*.*")))

    apps.append(fileName)
    print(fileName)

    for app in apps:
        label = tk.Label(frame, text = app, bg = "gray")
        label.pack()

def runApp():
    for app in apps:
        os.startfile(app)

###Canvas attributes

canvas = tk.Canvas(root, height = 400, width = 600, bg = "#263D42")
canvas.pack()

## Frame attribute
frame = tk.Frame(root, bg="#fff")
frame.place(relwidth = 0.8, relheight = 0.6, relx = 0.1, rely = 0.2)

### Buttons
openFileBtn = tk.Button(root, text = "Open File", padx = 10,
                        pady = 5, fg = "white", bg = "#263D42", command = addApp)
openFileBtn.pack()

runAppBtn = tk.Button(root, text = "Run App", padx = 10,
                        pady = 5, fg = "white", bg = "#263D42", command = runApp)
runAppBtn.pack()

for app in apps:
    label = tk.Label(frame, text = app)
    label.pack()

root.mainloop()

with open("savePaths.txt", "w") as f:
    for app in apps:
        f.write(app + ",")