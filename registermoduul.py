from tkinter import *
logins={}
passwords={} 


def authorisationcheck(ent1,ent2,dopaken):
    if ent1.get() != "" and ent2.get() != "":
        login = str(ent1.get())
        password = str(ent2.get())
        if logins[login]==password and passwords[password] == login:
            dopaken.destroy()
            dopaken=Toplevel()
            lbl4=Label(dopaken,text="Sa edukalt sisestatud",height=2,width=40,font="Arial 24")
            lbl4.pack()
        else:
            ent1.configure(bg="firebrick")
            ent2.configure(bg="firebrick")
    else:
        ent1.configure(bg="firebrick")
        ent2.configure(bg="firebrick")

def registrationcheck(ent1,ent2,dopaken):
    if ent1.get() != "" and ent2.get() != "":
        login = str(ent1.get())
        print(login)
        password = str(ent2.get())
        logins.update({login:password})
        passwords.update({password:login})
        print(logins)
        print(passwords)
        dopaken.destroy()
    else:
        ent1.configure(bg="firebrick")
        ent2.configure(bg="firebrick")


def registreerimine(): 
    dopaken=Toplevel()
    dopaken.geometry("600x600")
    dopaken.title("registreerimine")
    dopaken.configure(bg="darkorange")
    lbl1=Label(dopaken,text="Loo login",fg="white",bg="darkorange",font="Arial 15")
    ent1=Entry(dopaken,fg="cornflowerblue",bg="lightsalmon",width=15,font="Arial 20", justify=CENTER)
    lbl2=Label(dopaken,text="Loo parool",fg="white",bg="darkorange",font="Arial 15")
    ent2=Entry(dopaken,fg="cornflowerblue",bg="lightsalmon",width=15,font="Arial 20", justify=CENTER,show="*")
    Check=Button(dopaken,text="go", font="Arial 24",bg="orange",fg="white",relief=RAISED,command=lambda:registrationcheck(ent1,ent2,dopaken))
    lbl1.pack()
    ent1.pack()
    lbl2.pack()
    ent2.pack()
    Check.pack()
    dopaken.mainloop()

def autoriseerimine():
    dopaken=Toplevel()
    dopaken.geometry("600x600")
    dopaken.title("autoriseerimine")
    lbl1=Label(dopaken,text="Sisesta login")
    ent1=Entry(dopaken,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    lbl2=Label(dopaken,text="Sisesta parool")
    ent2=Entry(dopaken,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    Check=Button(dopaken,text="go", font="Arial 24",relief=RAISED,command=lambda:authorisationcheck(ent1,ent2,dopaken))
    lbl1.pack()
    ent1.pack()
    lbl2.pack()
    ent2.pack()
    Check.pack()
    dopaken.mainloop()

def muuda():
    dopaken=Toplevel()
    dopaken.geometry("600x600")
    dopaken.title("Login voi Parooli muutmine")
    lbl1=Label(dopaken,text="Mida te tahaksite muuta?",font="Arial 24")
    Lobtn=Button(dopaken, text="Login", font="Arial 24",relief=RAISED,command=lambda:lchange(dopaken))
    Pabtn=Button(dopaken, text="Parooli", font="Arial 24",relief=RAISED,command=lambda:pchange(dopaken))
    lbl1.pack()
    Lobtn.pack()
    Pabtn.pack()

def lchange(dopaken):
    dopaken.destroy()
    dopaken2=Toplevel()
    dopaken2.geometry("600x600")
    lbl1=Label(dopaken2,text="Kirjuta vana sisselogimine",font="Arial 24")
    ent1=Entry(dopaken2,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    lbl3=Label(dopaken2,text="Kirjutage oma parool",font="Arial 24")
    ent3=Entry(dopaken2,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    lbl2=Label(dopaken2,text="Kirjutage uus Login",font="Arial 24")
    ent2=Entry(dopaken2,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    chng=Button(dopaken2, text="Muuda", font="Arial 24",relief=RAISED,command=lambda:checkl(ent1,ent3,ent2,dopaken2))
    lbl1.pack()
    ent1.pack()
    lbl3.pack()
    ent3.pack()
    lbl2.pack()
    ent2.pack()
    chng.pack()
def checkl(ent1,ent3,ent2,dopaken2):
    if ent1.get() != "" and ent2.get() != "":
        yourpass=ent3.get()
        oldlogin=ent1.get()
        changelogin=ent2.get()
        if oldlogin in logins and yourpass in passwords and passwords[yourpass]==oldlogin:
            oldpass=logins[oldlogin]
            passwords[oldpass] = changelogin
            logins[changelogin]=logins.pop(oldlogin)
            print(logins)
            print(passwords)
            dopaken2.destroy()
        else:
            ent1.configure(bg="firebrick")
            ent2.configure(bg="firebrick")
            ent3.configure(bg="firebrick")
    else:
        ent1.configure(bg="firebrick")
        ent2.configure(bg="firebrick")
        ent3.configure(bg="firebrick")


def pchange(dopaken):
    dopaken.destroy()
    dopaken2=Toplevel()
    dopaken2.geometry("600x600")
    lbl3=Label(dopaken2,text="Kirjutage oma Login",font="Arial 24")
    ent3=Entry(dopaken2,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    lbl1=Label(dopaken2,text="Kirjutage vana parool",font="Arial 24")
    ent1=Entry(dopaken2,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    lbl2=Label(dopaken2,text="Kirjutage uus parool",font="Arial 24")
    ent2=Entry(dopaken2,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    chng=Button(dopaken2, text="Muuda", font="Arial 24",relief=RAISED,command=lambda:checkp(ent1,ent2,ent3,dopaken2))
    lbl3.pack()
    ent3.pack()
    lbl1.pack()
    ent1.pack()
    lbl2.pack()
    ent2.pack()
    chng.pack()
def checkp(ent1,ent2,ent3,dopaken2):
    if ent1.get() != "" and ent2.get() != "" and ent3 != "":
        yourlogin=ent3.get()
        oldpassword=ent1.get()
        changepassword=ent2.get()
        if oldpassword in passwords and yourlogin in logins and logins[yourlogin] == oldpassword :
            oldlogin=passwords[oldpassword]
            logins[oldlogin] = changepassword
            passwords[changepassword]=passwords.pop(oldpassword)
            print(logins)
            print(passwords)
            dopaken2.destroy()
        else:
            ent1.configure(bg="firebrick")
            ent2.configure(bg="firebrick")
            ent3.configure(bg="firebrick")
    else:
        ent1.configure(bg="firebrick")
        ent2.configure(bg="firebrick")
        ent3.configure(bg="firebrick")

def help():
    dopaken=Toplevel()
    dopaken.geometry("600x600")
    dopaken.title("Unustanud parooli taastamine")
    lbl1=Label(dopaken,text="Kirjutage oma Login",font="Arial 24")
    ent3=Entry(dopaken,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    chck=Button(dopaken, text="näita parooli", font="Arial 24",relief=RAISED,command=lambda:showpassword(ent3,dopaken))
    lbl1.pack()
    ent3.pack()
    chck.pack()

def showpassword(ent3,dopaken):
    yourlogin=ent3.get()
    dopaken.destroy()
    dopaken2=Toplevel()
    dopaken2.geometry("600x600")
    lbl2=Label(dopaken2,text="Teie parool:",font="Arial 24")
    lbl3=Label(dopaken2,font="Arial 30")
    if yourlogin in logins:
        yourpassword=logins[yourlogin]
        lbl3.configure(text=yourpassword)
        lbl2.pack()
        lbl3.pack()
    else:
        lbl3.configure(bg="firebrick")
        lbl3.configure(text="Vale Login")
        lbl2.pack()
        lbl3.pack()

