import random
import string
from tkinter import *

def generate_password():
    try:
        pass_length = int(length_entry.get())
        if pass_length <= 0:
            result_label.config(text="Please enter a positive length.")
            return
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return

    values = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(values) for _ in range(pass_length))
    result.config(text=f"Your random password is: {password}")

win = Tk()
win.title("Password Generator")
win.geometry("400x400")
win.configure(bg="white")

length = Label(win, text="Enter password length:", bg="white", font=("Helvetica", 12))
length.pack(pady=10)

length_entry = Entry(win, font=("Helvetica", 12))
length_entry.pack(pady=5)

generate_button = Button(win, text="Generate Password", command=generate_password, bg="lightgrey", font=("Helvetica", 12))
generate_button.pack(pady=15)

result = Label(win, text="", bg="white", font=("Helvetica", 12))
result.pack(pady=10)

win.mainloop()