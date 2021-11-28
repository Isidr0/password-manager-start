from tkinter import *
# messagebox is another module of code that is not imported with all classes and constants using *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # pick a random letter/number/symbol for the amount of times in the random range.
    pw_letters = [choice(letters) for _ in range(randint(8, 10))]
    pw_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pw_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pw_letters + pw_symbols + pw_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# save information into data.txt file. append to file with each add button press. separate with pipe.
# wipe website and password text entry.


def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # if website or password field empty trigger messagebox that says "please don't leave any fields empty!"
    # do not continue.
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                               f"\nPassword: {password} \nIs it okay to save?")
        if is_okay:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                print(len(website))






# ---------------------------- UI SETUP ------------------------------- #

# Window setup
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Logo image 1, 0
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Website label 0, 1
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1, sticky="e")

# Email/username label 0, 2
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2, sticky="e")

# Password label 0, 3
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3, sticky="e")

# Website  input 1-2, 1 (35 width)
website_entry = Entry()
website_entry.insert(END, string="www.google.com")
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")
website_entry.focus()

# Email input 1-2, 2 (35 width)
email_entry = Entry()
email_entry.insert(END, string="rtwatson86@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")


# Password input  1, 3 (21 width)
password_entry = Entry()
password_entry.insert(END, string="******")
password_entry.grid(column=1, row=3, sticky="ew")

# Generate Password button 2, 3
pw_button = Button(text="Generate password", command=generate_password)
pw_button.grid(column=2, row=3)

# Add button 1 - 2, 4 (width 36)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")



window.mainloop()



