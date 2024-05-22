import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="",database="info")
cur=con.cursor()
if con:
    

from tkinter import *
window = Tk()
window.title("personal info")
window.geometry("300x300")
window.resizable(False,False)
window.configure(background="red")
window.attributes("-topmost",True)
window.attributes("-alpha",0.9)
window.iconbitmap("favicon.ico")
lbl=Label(text=" NAME ")
lbl.place(x=10,y=20)
e1=Entry()
e1.place(x=100,y=20)
lbl1=Label(text=" ADDRESS ")
lbl1.place(x=10,y=60)
e2=Entry()
e2.place(x=100,y=60)
lbl3=Label(text=" PHONE ")
lbl3.place(x=10,y=100)
e3=Entry()
e3.place(x=100,y=100)
btn=Button(text="SAVE")
btn.place(x=60,y=150)

window.mainloop()