import tkinter

# When the entry button is pressed, it passed the entryboxtext to the label
def enterToLabel():
    entryBoxText = entryBox.get()
    label.config(text=entryBoxText)
    
# Makes a new window
window = tkinter.Tk()

# Configure the interface foremost
window.geometry("1200x800")
window.configure(bg="black")
window.title("CS Exercise Two")


# Make a button here
entryButton = tkinter.Button(window, text="Press Me", command=enterToLabel)

# Label below here
label = tkinter.Label(window, text="This is the old text")
                      
# Creating an entry box here
entryBox = tkinter.Entry(window)

# Belongs at the end, where all bad things belong
window.mainloop()
