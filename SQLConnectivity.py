import sqlite3
import choice

db = sqlite3.connect("Vivek.db")
cr = db.cursor()  #cr is a receptionist which connects with database
#cr.execute("create table if not exists student(UNAME TEXT,PASSWORD TEXT)")
# uname = input("Enter User Name: ")
# upass = input("Enter Password: ")
# cr.execute("insert into student values('"+uname.title()+"','"+upass.title()+"')")
# a = input("Enter Your Name")

n_choice = input("Enter Your Choice:"
          "1. Create"
          "2. Insert"
          "3. Update"
          "4. Search"
          "5. Delete")

if(n_choice == '1'):
    cr.execute("create table if not exists student(UNAME TEXT,PASSWORD TEXT)")
    a = input("Enter Your Name")
    b = input("Enter User Password")
elif(n_choice=='2'):
    a = input("Enter Your Name")
    b = input("Enter User Password")

    rows = cr.execute("select * from student where uname = '" + a.title().strip() + "'")
    if(rows.fetchone()):
        print("All Ready Present")
    else:
        cr.execute("insert into student values('"+a.title().strip()+"','"+b.title().strip()+"')")

elif(n_choice=='3'):
    name = input("Enter User Name")
    newpass = input("Enter New Password:")
    cr.execute("update student set  UPASS ='"+newpass+"' where UNAME='"+name+"'")

elif(n_choice==4):
    a = input("Enter Your Name")
    rows = cr.execute("select * from student where uname = '"+a.title().strip()+"'")
    for row in rows:
        print(row[0], row[1])

elif(n_choice==5):
    a = input("Enter Your Name")
    cr.execute("delete from student where uname ='"+a.title().strip()+"'")
db.commit()
db.close()

