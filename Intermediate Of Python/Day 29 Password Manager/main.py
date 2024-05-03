from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# #Password Generator Project
def generate_pass():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    letter = [choice(letters) for _ in range(randint(8, 10))]
    number = [choice(numbers) for _ in range(randint(2, 4))]
    symbol = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letter + number + symbol
    shuffle(password_list)
    password = "".join(password_list)
    pass_inp.insert(0, password)
    pyperclip.copy(text=password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = web_inp.get()
    mail = email_inp.get()
    password = pass_inp.get()
    new_data = {
        website: {
            "email": mail,
            "password": password
        }
    }
    if website == "" or password == "": #  mail == "" or
        messagebox.showwarning(title="Missing Details", message="Please enter all Details !!!")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {mail}\nPassword: "
        #                                               f"{password}\nIs it ok to save ?")
        # if is_ok:
        try:
            with open("passwords.json", mode="r") as f:
                # f.write(f"Website: {website} | Email/UserName: {mail} | Password: {password}\n")
                # Reading Data from file
                json_data = json.load(f)
                # Updating Data with new_data
                json_data.update(new_data)
                # print(json_data)
        except FileNotFoundError:
            with open("passwords.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("passwords.json", mode="w") as f:
                json.dump(json_data, f, indent=4)
        finally:
                web_inp.delete(0, END)
                pass_inp.delete(0, END)

# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_web():
    web_to_ser = web_inp.get()
    if len(web_to_ser) > 0:
        try:
            with open("passwords.json", mode="r") as file:
                file_data = json.load(file)
                messagebox.showinfo(title=f"Website: {web_to_ser} ",
                                    message=f"Email: {file_data[web_to_ser]['email']}\n"
                                    f"Password: {file_data[web_to_ser]['password']}")
        except FileNotFoundError:
            print("Sorry Create File First!!!!")
            messagebox.showinfo(title="Error", message="No data file found.")
        except KeyError:
            messagebox.showerror(title="Error Message", message=f"Sorry {web_to_ser} this website is not saved yet.")
        finally:
            web_inp.delete(0, END)
    else:
        messagebox.showinfo(title="Missing Details !", message="Please Provide Website Name")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(200, 200)
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website : ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username : ")
email_label.grid(row=2, column=0)
pass_label = Label(text="Password : ")
pass_label.grid(row=3, column=0)

# Entries
web_inp = Entry(width=28, borderwidth=2)
web_inp.grid(row=1, column=1, columnspan=1)
web_inp.focus()
email_inp = Entry(width=46, borderwidth=2)
email_inp.grid(row=2, column=1, columnspan=2)
email_inp.insert(0, "aakashpavar87@gmail.com")
pass_inp = Entry(width=28, borderwidth=2)
pass_inp.grid(row=3, column=1, columnspan=1)

# Buttons
gen_pass = Button(text="Generate Password", command=generate_pass)
gen_pass.grid(row=3, column=2)
add_btn = Button(text="Add", width=40, command=save_pass)
add_btn.grid(row=4, column=1, columnspan=2)
search_btn = Button(text="Search Web", width=15, command=search_web, bg="blue", fg="white")
search_btn.grid(row=1, column=2)
window.mainloop()
