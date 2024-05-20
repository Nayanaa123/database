from tkinter import*   
def click(num):
    first_value=str(e1.get())
    e1.delete(0,END)
    e1.insert(0,first_value+str(num))  
def add():
    second_value=str(e1.get())
    global old_value
    old_value=second_value
    global math 
    math="add"
    e1.delete(0,END)
def sub():
    second_value=str(e1.get())
    global old_value
    old_value=second_value
    global math 
    math="sub"
    e1.delete(0,END)
def mul():
    second_value=str(e1.get())
    global old_value
    old_value=second_value
    global math 
    math="mul"
    e1.delete(0,END) 
def div():
    second_value=str(e1.get())
    global old_value
    old_value=second_value
    global math 
    math="div"
    e1.delete(0,END)
def delete():
    second_value=str(e1.get())
    global old_value
    old_value=second_value
    global math 
    math="delete"
    e1.delete(0,END)

      
def equal():
    new_value=str(e1.get())
    e1.delete(0,END)
    if math=="add":
        result=int(new_value)+int(old_value)
        e1.insert(0,result) 
    elif math=="sub":
        result=int(new_value)-int(old_value)
        e1.insert(0,result) 
    elif math=="mul":
        result=int(new_value)*int(old_value)
        e1.insert(0,result) 
    elif math=="div":
        result=int(new_value)/int(old_value)
        e1.insert(0,result)
    else:
        del(result)
        e1.insert(0,result)         
window=Tk()
window.title("calculator")
window.geometry("350x300")
window.resizable(False,False)
window.configure(background="white")
window.attributes("-topmost",True)
window.attributes("-alpha",0.9)
window.iconbitmap("favicon.ico")
e1=Entry()
e1.place(x=20,y=30)                                                                                                                                                                           
btn=Button(text="    1    ", bg="yellow",command=lambda:click(1))
btn.place(x=10,y=100)
btn1=Button(text="    2    ",bg="yellow",command=lambda:click(2))
btn1.place(x=10,y=150)
btn2=Button(text="    3    ",bg="yellow",command=lambda:click(3))
btn2.place(x=10,y=200)
btn3=Button(text="    4    ",bg="yellow",command=lambda:click(4))
btn3.place(x=10,y=250)
btn4=Button(text="    5    ",bg="yellow",command=lambda:click(5))
btn4.place(x=100,y=100)
btn5=Button(text="    6    ",bg="yellow",command=lambda:click(6))
btn5.place(x=100,y=150)
btn6=Button(text="    7    ",bg="yellow",command=lambda:click(7))
btn6.place(x=100,y=200)
btn7=Button(text="    8    ",bg="yellow",command=lambda:click(8))
btn7.place(x=100,y=250)
btn8=Button(text="    9    ",bg="yellow",command=lambda:click(9))
btn8.place(x=190,y=100)
btn9=Button(text="    0    ",bg="yellow",command=lambda:click(0))
btn9.place(x=190,y=150)
btn10=Button(text="    +    ",bg="yellow",command=add)
btn10.place(x=190,y=200)
btn11=Button(text="    -    ",bg="yellow",command=sub)
btn11.place(x=190,y=250)
btn12=Button(text="    *    ",bg="yellow",command=mul)
btn12.place(x=280,y=100)
btn13=Button(text="    /    ",bg="yellow",command=div)
btn13.place(x=280,y=150)
btn14=Button(text="    =    ",bg="yellow",command=equal)                                                                                                                                                                                    
btn14.place(x=280,y=200)
btn14=Button(text="    del    ",bg="yellow",command=delete)                                                                                                                                                                                    
btn14.place(x=280,y=250)


window.mainloop()