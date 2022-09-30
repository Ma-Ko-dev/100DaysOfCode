from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import string
import pyperclip

# Constants
LOGO = "images/logo.png"
PW_FILE = "data/data.txt"
DEFAULT_USER = "Gariot"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pw_gen():
    """Generates a password by randomly choose letters, numbers and symbols by a random amount. Displays the generated
       Password in "entry_password" and also copy's it to your clipboard when generated. Takes no Arguments and returns
       nothing."""

    password_letters = [choice(string.ascii_letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(string.punctuation) for _ in range(randint(4, 6))]
    password_numbers = [choice(string.digits) for _ in range(randint(4, 6))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    """Saves all password credentials to a file named in PW_FILE. Will check for empty textfields and lets the User
       doublecheck their inputs. Clears the textfields after successfull saving. Takes no argument and returns
       nothing."""
    if len(entry_password.get()) == 0 or len(entry_username.get()) == 0 or len(entry_website.get()) == 0:
        messagebox.showinfo(title="Information", message="All fields are required!")
    else:
        is_okay = messagebox.askokcancel(title=entry_website.get(),
                                         message=f"These are the details you entered:\n\n"
                                                 f"Email: {entry_username.get()}\n"
                                                 f"Password: {entry_password.get()}\n\n"
                                                 f"Is it okay to save?")
        if is_okay:
            with open(PW_FILE, mode="a") as file:
                file.write(f"{entry_website.get()} | {entry_username.get()} | {entry_password.get()}\n")
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.config(padx=25, pady=25)

# logo canvas
logo = PhotoImage(file=LOGO)
canvas = Canvas(root, width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# label
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
label_username = Label(text="Email/Username:")
label_username.grid(row=2, column=0)
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

# entry
entry_website = Entry()
entry_website.focus()
entry_website.grid(row=1, column=1, columnspan=2, sticky="EW")
entry_username = Entry()
entry_username.insert(0, DEFAULT_USER)
entry_username.grid(row=2, column=1, columnspan=2, sticky="EW")
entry_password = Entry()
entry_password.grid(row=3, column=1, sticky="EW")

# button
button_password = Button(text="Generate Password", command=pw_gen)
button_password.grid(row=3, column=2, sticky="EW")
button_add = Button(text="Add", command=save_password)
button_add.grid(row=4, column=1, columnspan=2, sticky="EW")

root.mainloop()
