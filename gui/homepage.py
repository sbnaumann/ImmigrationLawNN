from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Title')
root.geometry("400x400")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, 'end')
    myLabel.pack(pady=10)

e = Entry(root, width=50, font=('Helvetica', 30))
e.pack(padx=10, pady=10)

button = ttk.Button(root, text="Click Me")
button.pack()

myButton = Button(root, text="enter your name please", command=myClick)
myButton.pack(pady=10)

root.mainloop()
