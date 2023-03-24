from tkinter import *
from registermoduul import *
logins={}
passwords={} 
aken=Tk() 
aken.geometry("500x425")
aken.title("Register") 
aken.iconbitmap("135620.ico")
aken.configure(bg="darkorange")
def end():
    aken.destroy() 


        



btn1=Button(aken, text="registreerimine", font="Arial 24",fg="orange4",bg="orange",relief=RAISED,command=registreerimine)
btn2=Button(aken, text="autoriseerimine", font="Arial 24",fg="orange4",bg="orange",relief=RAISED,command=autoriseerimine)
btn3=Button(aken, text="nime voi parooli muutmine", font="Arial 24",fg="orange4",bg="orange",relief=RAISED,command=muuda)
btn4=Button(aken, text="unustanud parooli taastamine", font="Arial 24",fg="orange4",bg="orange",relief=RAISED,command=help)
btn5=Button(aken, text="lopetamine", font="Arial 24",fg="limegreen",bg="green4",relief=RAISED,command=end)



btn5.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
ob=[btn1,btn2,btn3,btn4]
for i in range(len(ob)):
    ob[i].pack()
aken.mainloop()