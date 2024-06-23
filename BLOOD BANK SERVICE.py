#BLOOD BANK SERVICE

#MYSQL CONNECTION
import mysql.connector as con
mycon=con.connect(host='localhost',user='root',password='******',database='STUDENT')
#mycursor=mycon.cursor()
print("hello")
mycon.close()

#GUI WITH TKINTER
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import os
window=Tk()
window.title("PRANAM BLOOD HELP SERVICE")
window.geometry('1350x550')


#FUNCTIONS
def choice():
    global A
    A=loginas.get()
    if loginas.get()=='DONOR':
        Donor()
    elif loginas.get()=='RECEIVER':
        Receiver()
        

def Donor():
    for widget in f2.winfo_children():
        widget.destroy()
    for widget in f3.winfo_children():
        widget.destroy()
    Label(f2,text="DONOR",font=("Courier New",20,"bold"),bg="cyan").grid()
    global dnrid
    Label(f2,text="DONOR ID").grid(padx=10,pady=10,row=1,column=0)
    dnrid=Entry(f2)
    dnrid.grid(padx=10,pady=10,row=1,column=1)
    global dnrname
    Label(f2,text="NAME").grid(padx=10,pady=10,row=2,column=0)
    dnrname=Entry(f2)
    dnrname.grid(padx=10,pady=10,row=2,column=1)
    global dnrbg
    Label(f2,text="BLOOD GROUP").grid(padx=10,pady=10,row=3,column=0)
    dnrbg=ttk.Combobox(f2)
    dnrbg['values']=('','A+VE','A-VE','B+VE','B-VE','AB+VE','AB-VE','O+VE','O-VE')
    dnrbg.current(0)
    dnrbg.grid(padx=10,pady=10,row=3,column=1)
    global dnrage
    Label(f2,text="AGE").grid(padx=10,pady=10,row=4,column=0)
    dnrage=Entry(f2)
    dnrage.grid(padx=10,pady=10,row=4,column=1)
    global dnrnum
    Label(f2,text="PHONE NUMBER").grid(padx=10,pady=10,row=5,column=0)
    dnrnum=Entry(f2)
    dnrnum.grid(padx=10,pady=10,row=5,column=1)
    global dnradr
    Label(f2,text="ADHAR NUMBER").grid(padx=10,pady=10,row=6,column=0)
    dnradr=Entry(f2)
    dnradr.grid(padx=10,pady=10,row=6,column=1)
    global dnrloc
    Label(f2,text="LOCATION").grid(padx=10,pady=10,row=7,column=0)
    dnrloc=Entry(f2)
    dnrloc.grid(padx=10,pady=10,row=7,column=1)
    global dnrelg
    Label(f2,text="MEDICALLY HEALTHY?").grid(padx=10,pady=10,row=15,column=0)
    dnrelg=ttk.Combobox(f2)
    dnrelg['values']=('','YES','NO')
    dnrelg.current(0)
    dnrelg.grid(row=15,column=1)
    global dnravl 
    Label(f2,text="SHOW AS AVAILABLE?").grid(padx=10,pady=10,row=16,column=0)
    dnravl=ttk.Combobox(f2)
    dnravl['values']=('','YES','NO')
    dnravl.current(0)
    dnravl.grid(row=16,column=1)
    view=Button(f2,text="VIEW",command=Display).grid(padx=10,pady=10,row=18,column=0)
    delete=Button(f2,text='DELETE',command=Delete).grid(padx=10,pady=10,row=18,column=1)
    update=Button(f2,text='UPDATE',command=Update).grid(padx=10,pady=10,row=19,column=0)
    add=Button(f2,text='ADD',command=AddRecord).grid(padx=10,pady=10,row=19,column=1)
    viewall=Button(f2,text='VIEW ALL',command=ViewAll).grid(padx=10,pady=10,row=20,column=0)
    

def Receiver():
    for widget in f2.winfo_children():
        widget.destroy()
    for widget in f3.winfo_children():
        widget.destroy()
    Label(f2,text="RECEIVER",font=("Courier New",20,"bold"),bg="cyan").grid(column=1)
    global rid
    Label(f2,text="RECEIVER ID").grid(padx=10,pady=10,row=1,column=0)
    rid=Entry(f2)
    rid.grid(padx=10,pady=10,row=1,column=1)
    global rname
    Label(f2,text="ENTER NAME").grid(padx=10,pady=10,row=2,column=0)
    rname=Entry(f2)
    rname.grid(padx=10,pady=10,row=2,column=1)
    global rbg
    Label(f2,text="BLOOD GROUP").grid(padx=10,pady=10,row=3,column=0)
    rbg=ttk.Combobox(f2)
    rbg['values']=('','A+VE','A-VE','B+VE','B-VE','AB+VE','AB-VE','O+VE','O-VE')
    rbg.current(0)
    rbg.grid(padx=10,pady=10,row=3,column=1)
    global rage
    Label(f2,text="AGE").grid(padx=10,pady=10,row=4,column=0)
    rage=Entry(f2)
    rage.grid(padx=10,pady=10,row=4,column=1)
    global rnum
    Label(f2,text="PHONE NUMBER").grid(padx=10,pady=10,row=5,column=0)
    rnum=Entry(f2)
    rnum.grid(padx=10,pady=10,row=5,column=1)
    view=Button(f2,text="VIEW",command=Display).grid(padx=10,pady=10,row=18,column=0)
    delete=Button(f2,text='DELETE',command=Delete).grid(padx=10,pady=10,row=18,column=1)
    update=Button(f2,text='UPDATE',command=Update).grid(padx=10,pady=10,row=19,column=0)
    add=Button(f2,text='ADD',command=AddRecord).grid(padx=10,pady=10,row=19,column=1)
    search=Button(f2,text='SEARCH FOR DONORS',command=Search).grid(padx=10,pady=10,row=20,column=0)


def Display():
    for widget in f3.winfo_children():
        widget.destroy()
    if A=='DONOR':
        y=dnrid.get()
    else:
        y=rid.get()
    if bool(y)!=False:
        qry="SELECT * FROM {} WHERE {}_ID={}".format(A,A,y)
        mycursor.execute(qry)
        mydata=mycursor.fetchall()
        if mydata!=[]:
            Show(mydata)
        else:
            Label(f3,text='SEARCH UNSUCCESSFUL!\nNO SUCH {} FOUND.'.format(A),font=("Courier New",15,"bold"),bg="white").grid()
    else :
        Label(f3,text='ENTER A VALID ID TO DISPLAY YOUR DETAILS',font=("Courier New",15,"bold"),bg="white").grid()


def Update():
    for widget in f3.winfo_children():
        widget.destroy()
    qry="UPDATE {} SET ".format(A)
    if A=="DONOR":
        LST=["DONOR_NAME='{}'".format(dnrname.get()),"BLOOD_GROUP='{}'".format(dnrbg.get()),"AGE='{}'".format(dnrage.get()),"PHONE_NUMBER='{}'".format(dnrnum.get()),"ADHAR_NUMBER='{}'".format(dnradr.get()),"CURRENT_LOCATION='{}'".format(dnrloc.get()),"ELIGIBLE='{}'".format(dnrelg.get()),"AVAILABLE='{}' ".format(dnravl.get())]
        l=[]
        if dnrid.get()!='' and Look(dnrid.get()):
            for i in range(8):
                if "''" not in LST[i]:
                    l.append(LST[i])
            if l==[]:
                Label(f3,text="ENTER DETAILS TO UPDATE",font=("Courier New",15,"bold"),bg="white").grid()
            else:
                for i in range(len(l)):
                    if l[i]==l[-1]:
                        qry+=l[i]+"WHERE DONOR_ID='{}'".format(dnrid.get())
                    else:
                        qry+=l[i]+","
                mycursor.execute(qry)
                mycon.commit()
                Label(f3,text="ACCOUNT DETAILS UPDATED",font=("Courier New",15,"bold"),bg="white").grid()
        else:
            Label(f3,text='ENTER VALID ID TO UPDATE',font=("Courier New",15,"bold"),bg="white").grid()
    else:
        LST=["RECEIVER_NAME='{}'".format(rname.get()),"BLOOD_GROUP='{}'".format(rbg.get()),"AGE='{}'".format(rage.get()),"PHONE_NUMBER='{}'".format(rnum.get())]
        l=[]
        if rid.get()!='' and Look(rid.get())==True:
            for i in range(4):
                if "''" not in LST[i]:
                    l.append(LST[i])
            if l==[]:
                Label(f3,text="ENTER DETAILS TO UPDATE",font=("Courier New",15,"bold"),bg="white").grid()
            else:
                for i in range(len(l)):
                    if l[i]==l[-1]:
                        qry+=l[i]+"WHERE RECEIVER_ID='{}'".format(rid.get())
                    else:
                        qry+=l[i]+","
                mycursor.execute(qry)
                mycon.commit()
                Label(f3,text="ACCOUNT DETAILS UPDATED",font=("Courier New",15,"bold"),bg="white").grid()
        else:
            Label(f3,text='ENTER VALID ID TO UPDATE',font=("Courier New",15,"bold"),bg="white").grid()


def AddRecord():
    for widget in f3.winfo_children():
        widget.destroy()
    global lst
    if A=="DONOR":
        lst=[dnrid.get(),dnrname.get(),dnrbg.get(),dnrage.get(),dnrnum.get(),dnradr.get(),dnrloc.get(),dnrelg.get(),dnravl.get()]
        idcheck(lst)
        if Look(lst[0])==False:
            for i in range(8):
                if lst[i]=='':
                    Label(f3,text="ENTER ALL THE REQUIRED DETAILS",font=("Courier New",15,"bold"),bg="white").grid()
                    break
            else:
                qry="INSERT INTO DONOR VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8])
                mycursor.execute(qry)
                mycon.commit()
                Label(f3,text="NEW DONOR DETAILS ADDED\nYOUR DONOR ID IS : {}".format(lst[0]),font=("Courier New",15,"bold"),bg="white").grid()
        else:
            Label(f3,text="THE ENTERED ID ALREADY EXIST.\nTRY ANOTHER ID OR LEAVE IT BLANK",font=("Courier New",15,"bold"),bg="white").grid()
    else:
        lst=[rid.get(),rname.get(),rbg.get(),rage.get(),rnum.get()]
        idcheck(lst)
        if Look(lst[0])==False:
            for i in range(5):
                 if lst[i]=='':
                    Label(f3,text="ENTER ALL THE REQUIRED DETAILS",font=("Courier New",15,"bold"),bg="white").grid()
                    break
            else:
                qry="INSERT INTO RECEIVER VALUES('{}','{}','{}','{}','{}')".format(lst[0],lst[1],lst[2],lst[3],lst[4])
                mycursor.execute(qry)
                mycon.commit()
                Label(f3,text="NEW RECEIVER DETAILS ADDED\nYOUR RECEIVER ID IS : {}".format(lst[0]),font=("Courier New",15,"bold"),bg="white").grid()
        else:
             Label(f3,text="THE ENTERED ID ALREADY EXIST.\nTRY ANOTHER ID OR LEAVE IT BLANK.",font=("Courier New",15,"bold"),bg="white").grid()



def ViewAll():
    for widget in f3.winfo_children():
        widget.destroy()
    qry="SELECT * FROM {}".format(A)
    mycursor.execute(qry)
    mydata=mycursor.fetchall()
    if mydata!=[]:
        Show(mydata)
    else:
        Label(f3,text="NO RECORDS PRESENT!",font=("Courier New",15,"bold"),bg="white").grid()


def Delete():
    for widget in f3.winfo_children():
        widget.destroy()
    if A=='DONOR':
        y=dnrid.get()
        
    else:
        y=rid.get()
    Look(y)
    if bool(y)==True and Look(y):
        qry="DELETE FROM {} WHERE {}_ID='{}'".format(A,A,y)
        mycursor.execute(qry)
        mycon.commit()
        Label(f3,text="THE DATA OF THE RECORD WITH GIVEN ID HAS BEEN DELETED.",font=("Courier New",15,"bold"),bg="white").grid()
    else:
        Label(f3,text='ENTER VALID ID TO DELETE',font=("Courier New",15,"bold"),bg="white").grid()
        

def Search():
    for widget in f3.winfo_children():
        widget.destroy()
    if A=="RECEIVER":
        if Look(rid.get()):
            q="SELECT BLOOD_GROUP FROM RECEIVER WHERE RECEIVER_ID='{}'".format(rid.get())
            mycursor.execute(q)
            x=mycursor.fetchone()[0]
        else:
            Label(f3,text="ENTER VALID ID TO SEARCH",font=("Courier New",15,"bold"),bg="white").grid()
            x=''
    else:
        x=blgrp.get()
    while bool(x):
        qry="SELECT * FROM DONOR WHERE BLOOD_GROUP='{}'".format(x)
        mycursor.execute(qry)
        mydata=mycursor.fetchall()
        if mydata!=[]:
            Show(mydata)
        else:
            Label(f3,text='SORRY!\nNO MATCHING DONORS FOUND',font=("Courier New",15,"bold"),bg="white").grid()
        break


def Exit():
    res=tkinter.messagebox.askquestion(message="DO YOU WANT TO EXIT?")
    if res=='yes':
        window.destroy()
        mycon.close()

def Emergency():
    for widget in f2.winfo_children():
        widget.destroy()
    for widget in f3.winfo_children():
        widget.destroy()
    global A
    A='DONORS'
    Label(f2,text="EMERGENCY SEARCH",font=("Courier New",15,"bold"),bg="blue",fg="white").place(x=75,y=5)
    global blgrp
    Label(f2,text="CHOOSE BLOOD GROUP").grid(padx=10,pady=50,row=4,column=0)
    blgrp=ttk.Combobox(f2)
    blgrp['values']=('A+VE','A-VE','B+VE','B-VE','AB+VE','AB-VE','O+VE','O-VE')
    blgrp.current(0)
    blgrp.grid(row=4,column=1,padx=20,pady=50)
    emesearch=Button(f2,text="IMMEDIATE SEARCH",command=Search)
    emesearch.place(x=100,y=100)


def Show(mydata):
    t=("-"*12,"-"*12,"-"*12,"-"*12,"-"*12)
    T=("ID  ","NAME","BLOOD GROUP","AGE","PHONE NO.")
    if len(mydata[0])==9:
        c=Canvas(f3)
        c.pack(side="top",fill="both",expand=1)
        s=ttk.Scrollbar(f3,orient="horizontal",command=c.xview)
        s.pack(side="bottom",fill="x")
        c.configure(xscrollcommand=s.set)
        c.bind('<Configure>',lambda e: c.configure(scrollregion=c.bbox('all')))
        ff=Frame(c)
        c.create_window((0,10),window=ff,anchor="sw")
        t+=("-"*12,"-"*12,"-"*12,"-"*12)
        T+=("ADHAR NO.","PLACE","ELIGIBLE","AVAILABLE")
    mydata.insert(0,t)
    mydata.insert(1,T)
    mydata.insert(2,t)
    mydata.insert(len(mydata),t)
    n=0
    if len(mydata[0])>8:
        Label(ff,text="{}".format(A),font=("Courier New",20,"bold")).grid(row=0,column=1,pady=10)
    if len(mydata[0])<9:
        Label(f3,text="{}".format(A),font=("Courier New",20,"bold"),bg="white").grid(row=0,column=1,pady=10)
    for s in mydata:
        s=list(s)
        for i in range(len(s)):
            m=s[i]
            m=list(m)
            for x in range(14):
                if x>len(m):
                    m.append(' ')
            h='|'
            if m[5]=='-':
                h='+'
            m.append(h)
            m=''.join(m)
            s[i]=m
        s.insert(0,h)
        n+=1
        for m in range(len(s)):
            if len(mydata[0])>8:
                Label(ff,text=s[m],font=("Courier New",12,"bold")).grid(row=n,column=m)
            if len(mydata[0])<9:
                Label(f3,text=s[m],font=("Courier New",12,"bold"),bg="white",fg="black").grid(row=n,column=m)


def Look(y):
    qry="SELECT * FROM {} WHERE {}_ID='{}'".format(A,A,y)
    mycursor.execute(qry)
    mydata=mycursor.fetchall()
    return bool(mydata)


def idcheck(lst):
    if lst[0]=='':
        qry="SELECT MAX({}_ID) FROM {}".format(A,A)
        mycursor.execute(qry)
        mydata=mycursor.fetchone()
        lst[0]=str(int(mydata[0])+1)
        


#FRAMES     
f1=Frame(window,borderwidth=2,relief='solid',bg='pink')
f1.pack(side='left',fill="both")
f2=Frame(window,borderwidth=2,relief='solid',bg="cyan")
f2.pack(side='left',fill="both")
f3=Frame(window,borderwidth=2,relief="solid",bg="white")
f3.pack(side="right",expand=True,fill="both")

#PICTURES
image=Image.open("blood_logo1.png")
image=image.resize((150,150),Image.ANTIALIAS)
img=ImageTk.PhotoImage(image)
panel=Label(f1,image=img,bg="pink")
panel.place(x=30,y=250)



#MENU LOOK
Label(f1,text="WELCOME",font=("Courier New",20,"bold"),bg="pink",fg="black").grid(column=1)
Label(f1,text="LOGIN AS").grid(padx=10,row=2)
loginas=ttk.Combobox(f1)
loginas['values']=('DONOR','RECEIVER')
loginas.current(0)
loginas.grid(row=2,column=1,padx=13,pady=15)
go=Button(f1,text='DONE',command=choice)
go.grid(column=1)
emergency=Button(f1,text="EMERGENCY",font=("Ariel",10,"bold"),bg="red",fg="white",command=Emergency)
emergency.place(x=50,y=150)
ext=Button(f1,text="EXIT",command=Exit,bg="white",fg='red').place(x=80,y=200)
Label(f2,text=" "*100,bg="cyan").grid()



#window.mainloop()
#mycon.close()
