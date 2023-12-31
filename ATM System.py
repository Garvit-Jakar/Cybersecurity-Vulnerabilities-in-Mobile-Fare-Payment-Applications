from tkinter import *
from tkinter import messagebox
import sqlite3
from twilio.rest import Client
from random import randint
from twilio.base.exceptions import TwilioRestException 
client = Client("ACe45746ea9f7616cb24a8a465199526fb", "85b5425c3f2f06123a2383df3cfd7080")

conn=sqlite3.connect('./database.db')
c=conn.cursor()
flag=False


def Submit():
    accno=T1.get()
    atm=T2.get()
    if T3.get()=="" or int(T3.get())!=otp:
        flag=False
        messagebox.showinfo("Error","Invalid OTP")
        T3.delete('0',END)
        T3.focus_force()
    else:
        flag=True
        messagebox.showinfo("Congratulations!","You've Logged in")
        r=Toplevel()
    def Withdraw():
        r1=Toplevel()
        def Check1():
                if T3.get()=="":
                    messagebox.showinfo("Error!","Enter an Amount!")
                    T3.focus_force()
                elif(int(T3.get())>=balance[0] or int(T3.get())>20000):
                        messagebox.showinfo("Error!","Withdraw Amount Exceeds Allowance")
                        T3.delete('0',END)
                        T3.focus_force()
                else:
                        bal=list(balance)
                        bal[0]=bal[0]-int(T3.get())
                        c.execute("UPDATE Database SET balance=(?) WHERE accno=(?) ",(bal[0],accno))
                        conn.commit()
                        messagebox.showinfo("Succesfull!","Rs"+T3.get()+" is Withdrawn\nNew Balance: Rs"+str(bal[0]))
                        T3.delete('0',END)
                        L4['text']=bal[0]
                        r1.destroy()
                conn.commit()
        r1.configure(background="#566d79")
        r1.title("Withdraw")
        L1=Label(r1,text="Withdraw Menu",bg="darkblue",fg="orange",font=(None,25),padx=50)
        L1.place(x=60,y=50)
        L2=Label(r1,text="Current Balance(Rs):",font=(None,14),bg="#41525b")
        L2.place(x=82,y=120)
        c.execute("SELECT balance FROM Database WHERE accno=(?)",(accno,))
        balance=c.fetchone() 
        L4=Label(r1,text=balance,font=(None,14),bg="#41525b",fg="#ff0000")
        L4.place(x=267,y=120)
        L3=Label(r1,text="Enter amount to \nbe Withdrawn:",font=(None,13),bg="#41525b")
        L3.place(x=85,y=170)
        T3=Entry(r1)
        T3.place(x=225,y=190)
        T3.focus_force()
        B1=Button(r1,text="Withdraw",font=(None,16),command=Check1)
        B1.place(x=170,y=230)
        B2=Button(r1,text="Exit",command=r1.destroy,padx=7,bg="darkred",fg="yellow")
        B2.place(x=410,y=0)
        r1.resizable(False,False)
        r1.geometry("450x300+70+10")
        conn.commit()
        
    def Deposit():
        r2=Toplevel()
        def Check2():
                if T3.get()=="":
                        messagebox.showinfo("Error!","Enter a valid amount")
                        T3.focus_force()
                else:
                        bal=list(balance)
                        bal[0]=bal[0]+int(T3.get())
                        c.execute("UPDATE Database SET balance=(?) WHERE accno=(?) ",(bal[0],accno))
                        conn.commit()
                        messagebox.showinfo("Succesfull!","Rs"+T3.get()+" is Deposited\nNew Balance: Rs"+str(bal[0]))
                        T3.delete('0',END)
                        L4['text']=bal[0]
                        r2.destroy()
                conn.commit()
        r2.configure(background="#566d79")
        r2.title("Deposit")
        L1=Label(r2,text="Deposit Menu",bg="darkblue",fg="orange",font=(None,25),padx=70)
        L1.place(x=60,y=50)
        L2=Label(r2,text="Current Balance(Rs):",font=(None,14),bg="#41525b")
        L2.place(x=82,y=120)
        c.execute("SELECT balance FROM Database WHERE accno=(?)",(accno,))
        balance=c.fetchone() 
        L4=Label(r2,text=balance,font=(None,14),bg="#41525b",fg="#ff0000")
        L4.place(x=267,y=120)
        L3=Label(r2,text="Enter amount to \nbe Deposited:",font=(None,13),bg="#41525b")
        L3.place(x=85,y=170)
        T3=Entry(r2)
        T3.place(x=225,y=190)
        T3.focus_force()
        B1=Button(r2,text="Deposit",font=(None,16),command=Check2)
        B1.place(x=170,y=230)
        B2=Button(r2,text="Exit",command=r2.destroy,padx=7,bg="darkred",fg="yellow")
        B2.place(x=410,y=0)
        r2.resizable(False,False)
        r2.geometry("450x300+70+10")
    if flag==True:
            r.focus_force()
            r.configure(background="#647f8d")
            r.title("Main Menu")
            B1 = Button(r,text="Withdraw",bg="#0b0",font=(None,15),padx=2,command=Withdraw)
            B1.place(x=30,y=30)
            B2 = Button(r,text="Deposit",bg="#0b0",font=(None,15),padx=7,command=Deposit)
            B2.place(x=150,y=30)
            B4=Button(r,text="Exit",command=r.destroy,padx=7,bg="darkred",fg="yellow")
            B4.place(x=260,y=0)
            r.resizable(False,False)
            T1.delete('0',END)
            T2.delete('0',END)
            T3.insert(0,"XXXXXXXXXXXXXXXXX")
            T3.configure(state="disable",show="")
            r.geometry("300x100+10+350")
def Generate():
    accno=T1.get()
    atm=T2.get()
    c.execute("SELECT * FROM Database WHERE accno=(?) AND atm=(?)",(accno,atm))
    if(c.fetchall()):
        global otp
        otp=randint(1000,9999)
        try:
            client.messages.create(to="+919928226225",from_="+14027366805",body=otp)
        except TwilioRestException as err:
            print(err)
        messagebox.showinfo("Disclaimer","A 4-digit OTP has been sent to your Registered no.")
        T3.configure(state="normal",show="#")
        T3.delete('0',END)
        T3.focus_force()
        B2.configure(state="normal")
    else:
        messagebox.showinfo("Error","Invalid Account Number or PIN")
        T1.delete('0',END)
        T2.delete('0',END)
        T1.focus_force()

root=Tk()
root.title("Mobile Banking")
root.configure(background="#94a8b2")
L3=Label(root,text="Enter Credentials",font=(None,25),bg="navyblue",fg="white",padx=80)
L3.place(x=120,y=25)
L1 = Label(root,text="Account No.: ",bg="#94a8b2")
L1.place(x=180,y=90)
T1 = Entry(root)
T1.place(x=260,y=90)
T1.focus_force()
L2 = Label(root,text="ATM Pin :",bg="#94a8b2")
L2.place(x=200,y=130)
T2 = Entry(root,show="*")
T2.place(x=260,y=130)
B1 = Button(root,text="Generate OTP",bg="#6f6",command=Generate)
B1.place(x=400,y=130)
L3 = Label(root,text="Enter OTP :",bg="#94a8b2")
L3.place(x=193,y=170)
T3 = Entry(root)
T3.place(x=260,y=170)
T3.insert(0,"XXXXXXXXXXXXXXXXX")
T3.configure(state="disable")
B2 = Button(root,text="  Submit  ",command=Submit,bg="#6f6",state="disable")
B2.place(x=285,y=210)
B3=Button(root,text="Exit",command=root.destroy,padx=7,bg="darkred",fg="yellow")
B3.place(x=560,y=0)
root.resizable(False,False)
root.geometry("600x300+10+10")
root.mainloop()