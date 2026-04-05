from tkinter import *

window= Tk()
window.title("Mile to Kilometers Calculator")
window.config(padx=20,pady=20)

def calculate():
    mile= float(entry.get())
    km= round(mile*1.6)
    output_label.config(text=f"{km}")



entry= Entry(width=15)
entry.grid(column=1,row=0)

miles_label= Label(text="Miles",width=15)
miles_label.grid(column=2,row=0)

equal_to_label= Label(text="Is_Equal_To",width=15)
equal_to_label.grid(column=0,row=2)

output_label= Label(text="0" ,width=15)
output_label.grid(column=1,row=1)


km_label= Label(text="Km",width=15)
km_label.grid(column=2,row=2)

calculate_button= Button(text="Calculate",width=15,command= calculate)
calculate_button.grid(column=1,row=3)





window.mainloop()
