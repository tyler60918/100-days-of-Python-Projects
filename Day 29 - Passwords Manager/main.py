from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_field.delete(0, END)
    password_field.insert(0, password)
    pyperclip.copy(password) # Copies Password to Clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website_name = website_field.get()
    email = email_field.get()
    password = password_field.get()

    if len(website_name) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Error", message="Empty fields are not allowed.")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered:\n Email: {email}\n Password: {password}\n Is it okay to save?")

        if is_ok:
            data = f"{website_name} | {email} | {password}\n"

            with open("data.txt", "a") as data_file:
                data_file.write(data)
            
            website_field.delete(0, END)
            password_field.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_icon = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_icon)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Fields / Entries
website_field = Entry(width=35)
website_field.grid(column=1, row=1, columnspan=2)
website_field.focus()

email_field = Entry(width=35)
email_field.insert(0, "ecreipt@gmail.com")
email_field.grid(column=1, row=2, columnspan=2)

password_field = Entry(width=18)
password_field.grid(column=1, row=3)


# Buttons
gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()