from tkinter import *
import time
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
reps= 1

timer= None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
     window.after_cancel(timer)
     timer_label.config(text= "Timer")
     canvas.itemconfig(timer_text,text="00:00")
     global reps
     reps=1
     tick_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    
    short_break_sec= SHORT_BREAK_MIN*60
    work_sec=WORK_MIN*60
    long_break_sec= LONG_BREAK_MIN*60

    
         

    if reps%8==0:
         count_down(long_break_sec)
         timer_label.config(text="Long Break",fg=RED)
         

    elif reps%2==0:
         count_down(short_break_sec)
         timer_label.config(text="Short Break",fg=RED)

    else:
        count_down(work_sec)
        timer_label.config(text="Work",fg=GREEN)
         
    reps+=1
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min= math.floor(count/60)
    count_sec= count%60
    if count_sec<10 and count_sec !=0:
            count_sec=f"0{count_sec}"
    if count_sec == 0:
        count_sec= "00"
    
    canvas.itemconfig(timer_text,text= f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
         start_timer()
         marks=""
         work_sessions= math.floor(reps/2)
         for n in range(work_sessions):
              marks+="✓"
         tick_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg= YELLOW)

canvas= Canvas(width= 200, height=224 ,bg= YELLOW ,highlightthickness=0)
tomato_image=PhotoImage(file="tomato.png")
canvas.create_image(102,112,image=tomato_image)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

timer_label= Label(text="Timer",bg= YELLOW,fg=GREEN,font=("Arial",50,"bold"))
timer_label.grid(column=1,row=0)

start_button= Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)

reset_button= Button(text="Reset",command=reset_timer)
reset_button.grid(column=2,row=2)

tick_label= Label(bg=YELLOW,fg=GREEN,font=("Arial",24,"bold"))
tick_label.grid(column=1,row=3)



window.mainloop()

