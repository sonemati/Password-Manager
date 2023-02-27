from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]

    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]

    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    passwrd_entry.delete(0, END)
    passwrd_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if len(web_entry.get()) == 0 or len(usrname_entry.get()) == 0 or len(passwrd_entry.get()) == 0:
        messagebox.showerror(title="ERROR", message="A field was left empty!")

    else:

        is_ok = messagebox.askokcancel(title=web_entry.get().title(), message=f"Email: {usrname_entry.get()}\nPassword: "
                                                              f"{passwrd_entry.get()}\nIs it correct?")
        if is_ok:
            new_data = {web_entry.get().title() : {"email" : usrname_entry.get(), "password" : passwrd_entry.get()}}
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

            web_entry.delete(0, END)
            usrname_entry.delete(0, END)
            passwrd_entry.delete(0, END)


def search():
    if len(web_entry.get()) == 0:
        messagebox.showerror(title="ERROR", message="Please enter a website!")
    else:
        website = web_entry.get().title()
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
            if website in data:
                info = data[website]
                messagebox.showinfo(title=website, message=f"Email: {info['email']}\nPassword: {info['password']}")
            else:
                messagebox.showinfo(title=website, message="No passwords saved for this website!")
        except FileNotFoundError:
            messagebox.showerror(title="ERROR", message="No passwords saved yet!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

web = Label(text="Website:", bg="white", font=("Arial", 12))
web.grid(row=1, column=0)

usrname = Label(text="Email/Username:", bg="white", font=("Arial", 12))
usrname.grid(row=2, column=0)

passwrd = Label(text="Password:", bg="white", font=("Arial", 12))
passwrd.grid(row=3, column=0)

web_entry = Entry(width=22)
web_entry.grid(row=1, column=1)
web_entry.focus()
web_entry.insert(END, "WEBSITE")

usrname_entry = Entry(width=40)
usrname_entry.grid(row=2, column=1, columnspan=2)
usrname_entry.insert(END, "USERNAME")

passwrd_entry = Entry(width=22)
passwrd_entry.grid(row=3, column=1)
passwrd_entry.insert(END, "********")

gen_pass = Button(text="Generate Password", font=("Arial", 8), command=generate)
gen_pass.grid(row=3, column=2)

add_btn = Button(text="Add", width=43, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

search_btn = Button(text="Search", width=13, command=search)
search_btn.grid(row=1, column=2)


window.mainloop()
