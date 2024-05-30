import tkinter

screen = tkinter.Tk()
screen.title("Pomodoro Timer")
screen.geometry("500x500")

bg = tkinter.PhotoImage(file="tomato.gif")

label_img = tkinter.Label(screen, image=bg)
label_img.place(x=0, y=0, relwidth=1, relheight=1)

timer_text = tkinter.Label(text="Timer", font=("Courier", 40, "normal"), fg='#9bdeac')
timer_text.place(x=150, y=50)

timer = tkinter.Label(text="00:00", font=("Courier", 24, "normal"), fg="#fff", bg="#f26849")
timer.place(x=200, y=250)

min = 4
sec = 60
running = False

def start_count():
    global sec
    global min
    global flag
    if min == 0 and sec == 0:
        return
    sec -= 1
    if sec == 0 and min != 0:
        sec = 60
        min -= 1
    timer.config(text=f"{min:02}:{sec:02}")
    if flag:
        screen.after(1000, start_count)

def choose():
    global sec
    global min
    global flag
    if not flag:
        flag = True
        start_count()
        start_button.config(text="Stop")
    else:
        flag = False
        start_button.config(text="Start")

def reset_count():
    global sec
    global min
    sec = 60
    min = 4
    flag = False
    timer.config(text="00:00")

start_button = tkinter.Button(text="Start", font=("Courier", 12, "normal"), padx=10, command=choose)
start_button.place(x=100, y=400)

reset_button = tkinter.Button(text="Reset", font=("Courier", 12, "normal"), padx=10, command=reset_count)
reset_button.place(x=300, y=400)

screen.mainloop()
