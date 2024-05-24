import mysql.connector
from tkinter import *
import tkinter.messagebox as message
conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="infoo")
cur=conn.cursor()
def save():
    n=e1.get()
    p=e2.get()
    a=e3.get()
    if n=="" or p=="" or a=="":
        message.showinfo("insert data","please fill fields")
    cur.execute("INSERT INTO PERSONALINFO VALUE('%s','%s','%s');"%(n,p,a))   
    conn.commit()
    print("save data succesfuly")
def delete():
    n=e1.get()
    if n=="":
        message.showinfo("insert data","please fill name fields")
    cur.execute("delete from personalinfo where name='%s'"%(n))
    conn.commit()
    print("deleted succesfully")

def select():
    n=e1.get()        
def select():      
    n=e1.get()
    p=e2.get()
    a=e3.get()      
    if n=="":
       message.showinfo("select data","please select from fields")
    cur.execute("select *from personalionfo where name='%s'"%(n))
    result=cur.fetchall()    
    for a in result:        
       e2.insert(0,a[1])
       e3.insert(0,a[2])

    else:
         message.showinfo("user doesnt exist","please re check")                        
         cur.execute("INSERT INTO PERSONALINFO VALUE('%s','%s','%s');"%(n,p,a))   
         conn.commit()
         print("selected succesfully")           

def update():
    n=e1.get()
    p=e2.get()
    a=e3.get()  
    if conn:
        message.showinfo("update data","please update fields")    
    cur.execute("update kinter1 set phone='%s',address='%s' where name='%s'"%(p,a,n))   
    conn.commit()
    print("database updated succesfully")      

    a=e3.get()

    cur.execute("select *from kinter1 where name='%s'"%(n))
    result=cur.fetchall()  
    if result:
         message.showinfo("update data","please update fields")    
         cur.execute("update personalinfo set phone='%s',address='%s' where name='%s'"%(p,a,n))   
         conn.commit()
         print("database updated succesfully")

    else:       

         message.showinfo("user cant be updated","please re check")
         cur.execute("INSERT INTO personalinfo VALUE('%s','%s','%s');"%(n,p,a))  
         conn.commit()
         print("added succesfully")       

window=Tk()
window.title("welcome")
window.geometry("220x300")
window.resizable(False,False)
window.configure(background="#50252d")
window.attributes("-topmost",True)
window.attributes("-alpha",0.9)
window.iconbitmap("favicon.ico")
lbl1=Label(text=" name:-  ")
lbl1.place(x=20,y=30)
lbl2=Label(text="address:-")
lbl2.place(x=20,y=50)
lbl3=Label(text=" phone:- ")
lbl3.place(x=20,y=70)
e1=Entry()
e1.place(x=80,y=30)
e2=Entry()
e2.place(x=80,y=50)
e3=Entry()
e3.place(x=80,y=70)
btn1=Button(text="  save  ",command=save)
btn1.place(x=85,y=100)   
btn2=Button(text=" delete ",command=delete)
btn2.place(x=125,y=100) 
btn3=Button(text=" select ",command=select)
btn3.place(x=150,y=130)
btn4=Button(text=" update ",command=update)
btn4.place(x=95,y=140)
window.mainloop() 