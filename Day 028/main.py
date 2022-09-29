import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
IMAGE = "images/tomato.png"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    root.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_headline.config(text="Timer")
    label_check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        countdown(long_break_sec)
        label_headline.config(text="Break", fg=RED)
    elif reps % 2 > 0:
        countdown(work_sec)
        label_headline.config(text="Work", fg=GREEN)
    else:
        countdown(short_break_sec)
        label_headline.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = root.after(1000, countdown, count - 1)
    else:
        start_timer()
        check = ""
        for _ in range(0, math.floor(reps/2)):
            check += "✔"
        label_check.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Pomodoro")
root.config(padx=100, pady=50, bg=YELLOW)

label_headline = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
label_headline.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=IMAGE)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

button_start = Button(text="Start", command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(row=2, column=2)

label_check = Label(bg=YELLOW, fg=GREEN)
label_check.grid(row=3, column=1)

root.mainloop()
