import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5    # 25
SHORT_BREAK_MIN = 1     # 5
LONG_BREAK_MIN = 1   # 20
RIGHT = "✔"
my_timer = None
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    global my_timer
    window.after_cancel(my_timer)
    timer.config(text="Timer", fg=GREEN, bg=YELLOW)
    tick_label.config(text="")
    canvas.itemconfig(text_canvas, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60

    # if 1st/3rd/5th/7th reps
    if reps in [1, 3, 5, 7]:
        timer.config(text="Work", fg=RED)
        counter(work_sec)
    # if 8th reps
    elif reps == 8:
        timer.config(text="Break", fg=GREEN)
        counter(long_break_sec)
    # if 2nd/4th/6th
    else:
        timer.config(text="Break", fg=PINK)
        counter(short_break_sec)
    # counter(1 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"
    # Python Dynamic Typing Counting For Clock Format 00:00
    if count >= 0:
        canvas.itemconfig(text_canvas, text=f"{count_min}:{count_sec}")
        global my_timer
        my_timer = window.after(1000, counter, count - 1)
    else:
        start_timer()
        global reps
        if reps % 2 == 0:
            # Tick Mark
            repeater = reps // 2
            tick_label.config(text=f"{RIGHT*repeater}", fg=GREEN, bg=YELLOW)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=50, pady=50, bg=YELLOW)
window.title("Pomodoro")

# Heading Label
timer = Label(text="Timer", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
timer.grid(row=0, column=1)

# Canvas
tmt_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tmt_img)
text_canvas = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Start Button
start = Button(text="Start", fg=PINK, bg=YELLOW, command=start_timer)
start.grid(row=2, column=0)

# Reset Button
reset = Button(text="Reset", fg=RED, bg=YELLOW, command=reset_timer)
reset.grid(row=2, column=2)

# Tick Mark
tick_label = Label(text="", fg=GREEN)
tick_label.grid(row=3, column=1)


window.mainloop()
