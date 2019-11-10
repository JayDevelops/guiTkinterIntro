import tkinter as tk

root = tk.Tk()

v = tk.IntVar()

tk.Label(root, text="Hello",justify = tk.LEFT, padx = 20).pack()
Radio_button1 = tk.Radiobutton(root, text="Radiobutton 1", padx = 20, variable=v, value=1).pack(anchor=tk.W)
Radio_button2 = tk.Radiobutton(root, text="Radiobutton 2", padx = 20, variable = v, value=2).pack(anchor=tk.W)
Radio_button3 = tk.Radiobutton(root, text="Radiobutton 3", padx = 20, variable=v, value=3).pack(anchor=tk.W)

label_1 = tk.Label(root, text="-----------------------")
label_1.pack()

checkbutton_widget = tk.Checkbutton(root, text="Checkbutton 1")
checkbutton_widget.pack()

checkbutton_widget = tk.Checkbutton(root, text="Checkbutton 1")
checkbutton_widget.pack()

checkbutton_widget = tk.Checkbutton(root, text="Checkbutton 1")
checkbutton_widget.pack()

label_1 = tk.Label(root, text="")
label_1.pack()

root.mainloop()
