from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, timer
    window.after_cancel(timer)
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    start_button.config(state="normal")
    reset_button.config(state="disabled")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    start_button.config(state="disabled")
    reset_button.config(state="normal")

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        countdown(long_break_secs)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        countdown(short_break_secs)
    else:
        timer_label.config(text="Work", fg=GREEN)
        countdown(work_secs)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    count_mins = math.floor(count / 60)
    count_seconds = count % 60
    if count_mins < 10:
        count_mins = f"0{count_mins}"
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_seconds}")
    if count >= 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        num_work_sessions = math.floor(reps / 2)
        for _ in range(num_work_sessions):
            marks += "✔"
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0, highlightbackground=YELLOW)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0, highlightbackground=YELLOW, state="disabled")
reset_button.grid(column=2, row=2)

check_label = Label(text="", fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()