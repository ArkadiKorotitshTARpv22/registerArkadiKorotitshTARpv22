from tkinter import *
from registermoduul import *
logins={}
passwords={} 
aken=Tk() 
aken.geometry("600x750")
aken.title("Register") 
aken.iconbitmap("icon.ico")
aken.configure(bg="darkorange")
def end():
    aken.destroy() 


        



btn1=Button(aken, text="registreerimine", font="Arial 24",fg="white",bg="orange",relief=RAISED,command=registreerimine)
btn2=Button(aken, text="autoriseerimine", font="Arial 24",relief=RAISED,command=autoriseerimine)
btn3=Button(aken, text="nime voi parooli muutmine", font="Arial 24",relief=RAISED,command=muuda)
btn4=Button(aken, text="unustanud parooli taastamine", font="Arial 24",relief=RAISED,command=help)
btn5=Button(aken, text="lopetamine", font="Arial 24",relief=RAISED,command=end)



ob=[btn1,btn2,btn3,btn4,btn5]
for i in range(len(ob)):
    ob[i].pack()
aken.mainloop()