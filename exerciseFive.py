import tkinter

# When the certain button is clicked, output into the reset label
def whenOneIsPressed():
    outputLabel.config(text="One")

def whenTwoIsPressed():
    outputLabel.config(text="One")

def whenThreeIsPressed():
    outputLabel.config(text="One")

def whenFourIsPressed():
    outputLabel.config(text="One")

def resetPressed():
    outputLabel.config(text="Label has reset")


# Makes a new window for the Interface
window = tkinter.Tk()
window.title("Reset Button GUI")
window.config(background="blue")

outputLabel = tkinter.Label(window, text="Output Text")
outputLabel.grid(column=0, row=0, padx=2, pady=2)

# Labels one up to four, two by two
labelOne = tkinter.Button(window, text="ONE", bg="#e8e8e8", command=whenOneIsPressed, width=10, height=3)
labelTwo = tkinter.Button(window, text="TWO", bg="#e8e8e8", command=whenTwoIsPressed, width=10, height=3)
labelThree = tkinter.Button(window, text="THREE", bg="#e8e8e8", command=whenThreeIsPressed, width=10, height=3)
labelFour = tkinter.Button(window, text="FOUR", bg="#e8e8e8", command=whenFourIsPressed, width=10, height=3)

# Big red reset button here
labelReset = tkinter.Button(window, text="RESET", highlightbackground="red", bg="red", command=resetPressed, width=12, height=7)


# Putting into grid columns and rows for label one to four, with padding
labelOne.grid(column=0, row=1, padx=2, pady=2)
labelTwo.grid(column=1, row=1, padx=2, pady=2)
labelThree.grid(column=0, row=2, padx=2, pady=2)
labelFour.grid(column=1, row=2, padx=2, pady=2)

# Putting into grid columns and rows for the reset button, with padding
labelReset.grid(column=3, row=2, padx=2, pady=2)

# Runs the program on a mainloop
window.mainloop()
