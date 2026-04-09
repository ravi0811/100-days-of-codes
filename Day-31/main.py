from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}




#-------------------------Acessing data--------------------------

try:
    data= pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orignal_data= pandas.read_csv("data/french_words.csv")
    to_learn=orignal_data.to_dict(orient="records")
else:
    to_learn= data.to_dict(orient= "records")

word_to_learn=[]
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card= random.choice(to_learn)
    current_card["French"]
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_image)
    flip_timer=window.after(3000,func= flip_card)

def is_known():
    to_learn.remove(current_card)
    data= pandas.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv",index=False)
    next_card()
    
def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image= card_back_image)


#-----------------------------UI Setup------------------------------
window= Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg= BACKGROUND_COLOR)
flip_timer=window.after(3000,func= flip_card)

canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)


#--------------------------Images-------------------------
card_front_image= PhotoImage(file="images/card_front.png")
card_back_image= PhotoImage(file="images/card_back.png")
right_image= PhotoImage(file="images/right.png")
wrong_image= PhotoImage(file="images/wrong.png")

card_background=canvas.create_image(400,263,image=card_front_image)

card_title=canvas.create_text(400,150,text="",font=("Arial",40,"bold"))
card_word= canvas.create_text(400,263,text="",font=("Arial",60,"bold"))


canvas.grid(row=0,column=0,columnspan=2)

#-------------------Button Setup---------------------------
known_button=Button(image= right_image,highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)

unknown_button=Button(image= wrong_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

next_card()

window.mainloop()