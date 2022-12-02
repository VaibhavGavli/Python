import mysql.connector
db=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root"
   )
cursor=db.cursor()
cursor.execute("create database pythontest3")
cursor.execute("show databases")

for i in cursor:
    print(i)
cursor.close()
db.close()
#-------------------------------------
1.
db=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="pythontest3"
   )
cursor=db.cursor()
cursor.execute("create table student(roll_no int auto_increment primary key,name varchar(30),marks int(10))")
cursor.execute("show tables")

for i in cursor:
    print(i)
    
cursor.close()

#------------------------------------
2.
cursor=db.cursor()
sql="Insert into student(name,marks) values(%s,%s)"
val=[]
for i in range(0,3):
     name=input("Enter name")
     marks=input("Enter the marks")
     val.append((name,marks))
     
cursor.executemany(sql,val)
db.commit()
print(cursor.rowcount,"record inserted")
     
cursor.close() 
#----------------------------------------------
3.
db=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="pythontest3"
   )
cursor=db.cursor()
sql="update student set name=%s where marks=%s"
val=("Vikrant","20")
cursor.execute(sql,val)
db.commit()
print(cursor.rowcount,"records upated")

#------------------------------------------------
4.
cursor.execute("Select * from student")
lst=cursor.fetchall()
print(lst)
#----------------------------------------------------
5.
cursor.execute("Select * from student where marks > 80")
lst=cursor.fetchall()
print(lst)

#---------------------------------------------------
6.
cursor.execute("Select * from student where name like 'v%'")
lst=cursor.fetchall()
print(lst)

#---------------------------------------------------
7.
db=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="pythontest3"
   )
cursor=db.cursor()
sql="delete from student where name=%s"
val=("Vikrant",)
cursor.execute(sql,val)
db.commit()
print(cursor.rowcount,"record updated")










