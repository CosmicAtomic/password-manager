from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]


    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) ==0 or len(email)==0 or len(password) == 0:
        messagebox.showinfo(title= "Oops", message="Don't leave any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file) #Reading old data
                
        except FileNotFoundError:
            with open("data.json", "w")  as data_file:  
                json.dump(new_data, data_file, indent= 4)
        else: 
            data.update(new_data) #Updating old data with new data

            with open("data.json", "w")  as data_file: 
                json.dump(data, data_file, indent= 4) #Saving updated data    
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
#----------------------------- FIND PASSWORD--------------------------#

def find_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            file = data[website]
    except FileNotFoundError:
        messagebox.showinfo(title= "Error", message= "No Data File Found")
    except KeyError:
        messagebox.showinfo(title= "Error", message= f"No details for the {website} exists")
    else:
        messagebox.showinfo(title= website, message= f"Email: {file["email"]} \nPassword: {file["password"]}")    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx= 30, pady= 30)

canvas = Canvas(width= 200, height= 200)
padlock_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = padlock_img)
canvas.grid(row = 0, column = 1)

website_label = Label(text= "Website: ", font=("Times New Roman", 15))
website_label.grid(row=1,column= 0)

website_input = Entry(width= 25)
website_input.grid(row= 1, column= 1)

search_button = Button(text= "Search", width= 15 ,command= find_password)
search_button.grid(row= 1, column= 2)

email_label = Label(text= "Email/Username: ", font=("Times New Roman", 15))
email_label.grid(row=2,column= 0)

email_input = Entry(width= 45)
email_input.grid(row= 2, column= 1, columnspan= 2)
email_input.insert(0, "" )

password_label = Label(text= "Password: ", font=("Times New Roman", 15))
password_label.grid(row=3,column= 0)

password_input = Entry(width= 25)
password_input.grid(row= 3, column= 1)

generator_button = Button(text= "Generate Password", width = 15, command= generate_password)
generator_button.grid(row = 3, column= 2)

add_password_button =Button(text= "Add",command= save, width = 40)
add_password_button.grid(row=4, column= 1, columnspan= 2)











window.mainloop()
