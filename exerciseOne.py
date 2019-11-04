import tkinter

window = tkinter.Tk() # Makes a new window

# Congifure the interface
window.geometry("1200x800")
window.configure(bg="blue")
window.title("CS Exercise One")


# Make a button
button = tkinter.Button(window, text="Kill me", command=window.destroy)

# Place the button in the window
button.grid(row=10, column=8)

# Make a label
helloLabel = tkinter.Label(window, text="Hello! This is my program")
helloLabel.grid(row=4, column=8)

# Belongs at the end, where all bad things belong
window.mainloop()
