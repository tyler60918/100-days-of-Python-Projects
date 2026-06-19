from tkinter import *

def button_clicked():
    label["text"] = input.get()
    print("I got clicked")

window = Tk()
window.title("My first GUI Program")
window.minsize(width=1000, height=700)
window.config(padx=20, pady=20)

# Label
label = Label(text="I am a label", font=("Arial", 24, "bold"))
# label.pack(side="top") # Adds the label to the window
# label.place(x=100, y=150) # Adds the label to a specific coordinate location on the window
label.grid(column=0, row=0) # Adds the label to a specific row and column on a grid relative to other components

# Two ways to change values later
label["text"] = "New Text"
label.config(text="New Text", padx=20, pady=20)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New button", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)





window.mainloop()