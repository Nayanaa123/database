import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="",database="rrr")
cur=con.cursor()
n=int(input("select (1 create,2 add,3 update,4del,5 sel)"))
if n==1:
    m=input("enter a table name")
    if con:
        cur.execute("create table %s(name char(10),maths int,phy int,cs int)"%m)
        print("table created")
elif n==2:
    m=input("enter a table name")
    name=input("enter a name")
    maths=int(input("enter a maths mark"))
    phy=int(input("enter a phy mark"))
    cs=int(input("enter a cs mark")) 
    if con:
        cur.execute("insert into %s value('%s',%s,%s,%s)"%(m,name,maths,phy,cs))  
        con.commit()
        print("%s added succesefully"%name)
elif n==3:
    m=input("enter a table name")
    name1=input("enter a name to be changed")
    name2=input("enter a nmme to be subsituted")
    if con:
        cur.execute("update %s set name='%s' where name='%s'"%(m,name2,name1)) 
        con.commit()
        print("database updated succesfully")
elif n==4:
      m=input("enter a table name")
      name=input("enter a name") 
      if con:
          cur.execute("delete from %s where name='%s'"%(m,name))
          con.commit()
          print(" deleted succesfully")
else:
    m=input("enter a table name")
    name=input("enter a name")
    if con:
        cur.execute("select* from %s where name='%s'"%(m,name))
        result=cur.fetchall()
        for i in result:
            print("name :",i[0])
            print("maths :",i[1])
            print("phy :",i[2])
            print("cs :",i[3])