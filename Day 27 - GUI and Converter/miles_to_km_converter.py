from tkinter import *

KM_PER_MILE = 1.60934

def convert():
    miles = float(miles_field.get())
    km = round(miles * KM_PER_MILE, 2)
    km_value_label.config(text=f"{km}")

window = Tk()
window.title("Mi to Km Converter")
window.minsize(width=100, height=50)
window.config(padx=20, pady=20)

miles_field = Entry(width=8)
miles_field.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

km_value_label = Label(text="0")
km_value_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_buttton = Button(text="Calculate", command=convert)
calculate_buttton.grid(column=1, row=2)

window.mainloop()