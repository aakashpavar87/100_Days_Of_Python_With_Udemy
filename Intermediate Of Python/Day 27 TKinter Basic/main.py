from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="First Label", font=["Courier", 24, "bold"])
my_label.pack()

# Input Text Field
inp = Entry()
inp["width"] = 10

# Button


def button_clicked():
    my_label["text"] = inp.get()
    print("Clicked on Button")


button = Button(text="Click Me!", fg="crimson", command=button_clicked)
button.pack()

inp.pack()


window.mainloop()
