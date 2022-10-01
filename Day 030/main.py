from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import string
import pyperclip
import json

# Constants
LOGO = "images/logo.png"
PW_FILE = "data/data.json"
DEFAULT_USER = "Gariot"


# ----------------------------- SEARCH FUNCTION --------------------------------- #
def search_entry():
    website = entry_website.get()

    try:
        with open(PW_FILE, mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No Data File Found!")
    else:
        if website in data:
            username = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(f"Info for: {website}", f"Website: {website}\nUsername: {username}\n"
                                                        f"Password: {password}\n\nPassword was copied to clipboard.")
            pyperclip.copy(password)
        else:
            messagebox.showinfo("No details", "No details for the website exists.")


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
    """Saves all password credentials to a file named in PW_FILE. Will check for empty textfields Clears the
       textfields after successfull saving. Takes no argument and returns nothing."""
    new_data = {
        entry_website.get(): {
            "email": entry_username.get(),
            "password": entry_password.get()
        }
    }

    if len(entry_password.get()) == 0 or len(entry_username.get()) == 0 or len(entry_website.get()) == 0:
        messagebox.showinfo(title="Information", message="All fields are required!")
    else:
        try:
            with open(PW_FILE, mode="r") as file:
                # reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open(PW_FILE, mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open(PW_FILE, mode="w") as file:
                # saving updated data
                json.dump(data, file, indent=4)
        finally:
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
entry_website.grid(row=1, column=1, sticky="EW")
entry_username = Entry()
entry_username.insert(0, DEFAULT_USER)
entry_username.grid(row=2, column=1, columnspan=2, sticky="EW")
entry_password = Entry()
entry_password.grid(row=3, column=1, sticky="EW")

# button
button_search = Button(text="Search", command=search_entry)
button_search.grid(row=1, column=2, padx=3, sticky="EW")
button_password = Button(text="Generate Password", command=pw_gen)
button_password.grid(row=3, column=2, padx=3, sticky="EW")
button_add = Button(text="Add", command=save_password)
button_add.grid(row=4, column=1, columnspan=2, sticky="EW")

root.mainloop()
