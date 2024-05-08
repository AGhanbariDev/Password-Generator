"""
Useful websites:
https://web.archive.org/web/20190427180831/http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
https://realpython.com/python-gui-tkinter/#working-with-widgets
"""

# Importing
import random
from tkinter import *
import tkinter.font as TkFont
import time
import pyperclip

# Required Variables
window = Tk()
style = TkFont.Font(family="Helvetica",size=(12),weight="bold")
style_two = TkFont.Font(family="Helvetica",size=(20))
swidth = 400
sheight = 300


# Inital Setup
window.title("Password Generator")
window.geometry(f"{swidth}x{sheight}")
window.resizable(False, False)
window.iconbitmap('C:\\Users\\aydip\\Password Generator\\lock.ico')
# window.overrideredirect(True) # Removes title bar

# Commands and functions
def reset():
    pyperclip.copy('')
    reset_msg = Label(font = style, fg = "green", text="Password has been succesfully reset.")
    reset_msg.place(x=53, y=125)
    window.update()
    time.sleep(1.5)
    reset_msg.destroy()

def create_password(): 
    password = [] 
    if (chars.get()).isdigit():
        get_char_num = int(chars.get())
        if get_char_num < 20 and get_char_num > 0:
            characters = "a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 , . / ; ' [ ] \\ - = ` ~ ! @ # $ % ^ & * ( ) _ + { } | : \" > ? <"
            characters = characters.split()

            for i in range(get_char_num):
                password.append(characters[random.randint(0, len(characters) - 1)])

            password = "".join(password)

            # Copy to clipboard
            pyperclip.copy(f'{password}')

            confirm = Label(font = style, fg = "green", text="Password has been copied to clipboard!")
            confirm.place(x=42.5, y=125)

            window.update()
            time.sleep(1.5)
            confirm.destroy()
        
        # Shows "Number is too high. Please try again."
        else:
            too_high = Label(font = style, fg = "red", text="Number is too high. Please try again.")
            too_high.place(x=55, y=125)
            window.update()
            time.sleep(1.5)
            too_high.destroy()

        chars.delete(0, int(chars.get())-1)

    # Shows "Invalid request. Please try again.""
    else:
        not_str = Label(font = style, fg = "red", text="Invalid request. Please try again.")
        not_str.place(x=76, y=125)
        window.update()
        time.sleep(1.5)
        not_str.destroy()
        chars.delete(0, len(chars.get()))

# Big title on screen
title = Label(font=style, fg="black", text="Enter the number of characters you wish to have.")
title.pack(pady=3)

warning = Label(font=style, fg="black", text="(Max is 20)")
warning.place(x=155, y=75)

chars = Entry(font=style_two, width=10, relief="flat")
chars.place(x=122.5, y=35)

password_button = Button(text="New Password", command=create_password, font=style, bg="#008000", fg="white", width=30, height=2, activebackground="#006400", activeforeground="white", relief="flat", bd=0)
password_button.place(x=47, y= 180)

reset_button = Button(text="Reset", command=reset, font=style, bg="#FF0000", fg="white", width=30, height=2, activebackground="#CC0000", activeforeground="white", relief="flat", bd=0)
reset_button.place(x=47, y= 240)



# End of Setup
window.mainloop()