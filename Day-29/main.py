from tkinter import *
from tkinter import messagebox
from random import shuffle,randint,choice
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list.extend([choice(letters) for char in range(randint(8, 10))])
    password_list.extend([choice(symbols) for char in range(randint(2, 4))])
    password_list.extend([choice(numbers) for char in range(randint(2, 4))])

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_txt():

    website= website_entry.get()
    email_username=email_Username_entry.get()
    password=password_entry.get()

    if len(website)==0 or len(email_username)==0 or len(password)==0:

        messagebox.showwarning(title="Oops",message="Please don't leave any fields empty!")
    
    else:
        
        is_ok= messagebox.askokcancel(title=website, message= f"These are the details entered: \nEmail: {email_username}\nPassword: {password}\n Is it ok to save?")
        if is_ok:
            with open ("info.txt","a") as file:
                file.write(f"{website} | {email_username} | {password}\n")

            website_entry.delete(0,END)
            password_entry.delete(0,END)
            website_entry.focus()
    

# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas= Canvas(width=200,height=200)
logo_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)



#----------------Labels----------------

website_label= Label(text="website:")
website_label.grid(column=0, row=1)

email_Username_label= Label(text="Email/Username:")
email_Username_label.grid(column=0,row=2)

password_label= Label(text="Password:")
password_label.grid(column=0,row=3)


#--------------------Buttons----------------------------
generate_password_button=Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2,row=3)

add_button= Button(text="Add",width=36,command=add_to_txt)
add_button.grid(column=1,row=4,columnspan=2)



#----------------------Entries------------------------
email_Username_entry= Entry(width=35)
email_Username_entry.grid(column=1,row=2,columnspan=2)
email_Username_entry.insert(0,"dummy@gmail.com")

website_entry= Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

password_entry= Entry(width=21)
password_entry.grid(column=1,row=3)








window.mainloop()