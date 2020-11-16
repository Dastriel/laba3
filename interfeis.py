from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")
 
message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")

def recycle():
    result = message.get()
    mass = result.split()
    output = mass[0], mass[1][0]+"."+mass[2][0]+"."
    messagebox.showinfo("GUI Python", output)
 
message_button = Button(text="Click Me", command=recycle)
message_button.place(relx=.5, rely=.5, anchor="c")

root.mainloop()
