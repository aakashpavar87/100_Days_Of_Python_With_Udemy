from tkinter import *

window = Tk()
window.title("My Grid")
window.minsize(width=500, height=500)
# Label
label = Label(text="Name :")
label.grid(column=0, row=0)

# Button
butt = Button(text="Click Me!")
butt.grid(column=1, row=1)

# New Button
butt2 = Button(text="Another Button")
butt2.grid(column=2, row=0)

# Text Box
my_input = Entry(width=20)
my_input.grid(column=3, row=2)
window.mainloop()
