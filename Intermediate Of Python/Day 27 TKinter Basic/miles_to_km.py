from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=150)
window.config(padx=20, pady=20)


def miles_to_km():
    miles = float(my_inp.get())
    km = miles * 1.609
    mile.config(text=f"{int(round(km, 0))}")


# Entry
my_inp = Entry(width=10)
my_inp.grid(row=0, column=1)

# is Convert Text
text = Label(text="is equal to")
text.grid(row=1, column=0)

# Miles Converted
mile = Label(text="0")
mile.grid(row=1, column=1)

# Button
btn = Button(text="Convert", command=miles_to_km)
btn.grid(row=2, column=1)

# Miles Label
mile_label = Label(text="Miles")
mile_label.grid(row=0, column=2)

# KM Label
km_label = Label(text="KM")
km_label.grid(row=1, column=2)
window.mainloop()
