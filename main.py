from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ----------------------------Search Functionality ------------------------------ #
def search():
    website=website_entry.get()
    try:
        with open("data.json", 'r') as file:
            data=json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data Found")

    else:
        if website in data:
            username=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title="Credentials",message=f"Username: {username} \npassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No Data Found for website {website}")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }
    if len(website) < 1 or len(password) < 1:
        messagebox.showinfo(title="warning!", message="Field should not be empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Email:{username}\nPassword:{password}\n\n Is it ok to save?")

        if is_ok:
            try:
                with open("data.json", 'r') as file:
                    # write a data in Json
                    # json.dump(new_data, file, indent=3)

                    # Read a data from Json,it will written as a python dictionary:
                    # data=json.load(file)

                    # Reading old date
                    data=json.load(file)
                    #updating new data with old data
                    data.update(new_data)
            except:
                with open("data.json","w") as file:
                    json.dump(new_data,file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    # writing a data to a Json file
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=22)
website_entry.focus()
website_entry.grid(row=1, column=1)

username_label = Label(text="Username/Email:")
username_label.grid(row=2, column=0)

username_entry = Entry(width=40)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "raghuvaranvit@gmail.com")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(width=34, text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button=Button(text="Search",width=12,command=search)
search_button.grid(row=1, column=2)
window.mainloop()
