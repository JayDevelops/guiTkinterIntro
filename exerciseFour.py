import tkinter as tk

root = tk.Tk()

v = tk.IntVar()

def RB1():
    label_1.configure(text = "Radio Button 1")

def RB2():
    label_1.configure(text = "Radio Button 2")

def RB3():
    label_1.configure(text = "Radio Button 3")

tk.Label(root, text="", justify = tk.LEFT, padx = 20).pack()
Radio_button1 = tk.Radiobutton(root, text="Radiobutton 1", command=RB1, padx = 20, variable=v, value=1).pack(anchor=tk.W)

Radio_button2 = tk.Radiobutton(root, text="Radiobutton 2", command=RB2, padx = 20, variable=v,value=2).pack(anchor=tk.W)
Radio_button3 = tk.Radiobutton(root,text="Radiobutton 3",command=RB3, padx = 20, variable=v, value=3).pack(anchor=tk.W)

label_1 = tk.Label(root, text="Click a radio button")
label_1.pack()

def CB1():
    label_2.configure(text = "True-False-False")

def CB2():
    label_2.configure(text = "")

def CB3():
    label_2.configure(text ="")


checkbutton_widget1 = tk.Checkbutton(root, text="Checkbutton 1")
checkbutton_widget1.pack()

checkbutton_widget2 = tk.Checkbutton(root, text="Checkbutton 2")
checkbutton_widget2.pack()

checkbutton_widget3 = tk.Checkbutton(root, text="Checkbutton 3")
checkbutton_widget3.pack()

label_2 = tk.Label(root, text="")
label_2.pack()

button_1 = tk.Button(root, text="push", command=CB1)
button_1.pack()





root.mainloop()
