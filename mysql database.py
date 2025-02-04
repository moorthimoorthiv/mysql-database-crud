from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="registration")

def insert():
    name = input("Enter Name : ")
    age = input("Enter Age : ")
    address = input("Enter Address : ")
    contact = input("Enter Contact : ")
    mail = input("Enter Mail : ")

    res = con.cursor()
    sql = "insert into data (name,age,address,contact,mail) values (%s,%s,%s,%s,%s)"
    res.execute(sql,(name,age,address,contact,mail))
    con.commit()
    print("\n")
    print("Record Insert Successfully...!!!")

def select():
    res = con.cursor()
    sql = "SELECT * from data"
    res.execute(sql)
    result = res.fetchall()
    print("\n")
    print(tabulate(result, headers=["ID", "NAME", "AGE", "ADDRESS", "CONTACT", "MAIL"]))

def update():
    print("1.Name")
    print("2.Age")
    print("3.Address")
    print("4.Contact")
    print("5.Mail")
    option = int(input("\nwhich field you want to update?:"))
    if option == 1:
        pid = input("Enter Your ID:")
        name = input("Enter Your Name:")
        cur = con.cursor()
        sql = "UPDATE data set name=%s where pid=%s"
        cur.execute(sql, (name,pid))
        con.commit()
        select()
        print("\n")
        print("Update Successfully...!!!")
    elif option == 2:
        pid = input("Enter Your ID:")
        age = input("Enter Your Age:")
        cur = con.cursor()
        sql = "UPDATE data set age=%s where pid=%s"
        cur.execute(sql, (age, pid))
        con.commit()
        select()
        print("\n")
        print("Update Successfully...!!!")
    elif option == 3:
        pid = input("Enter Your ID:")
        address = input("Enter Your Adddress:")
        cur = con.cursor()
        sql = "UPDATE data set address=%s where pid=%s"
        cur.execute(sql, (address, pid))
        con.commit()
        select()
        print("\n")
        print("Update Successfully...!!!")
    elif option == 4:
        pid = input("Enter Your ID:")
        contact = input("Enter Your Contact:")
        cur = con.cursor()
        sql = "UPDATE data set contact=%s where pid=%s"
        cur.execute(sql, (contact, pid))
        con.commit()
        select()
        print("\n")
        print("Update Successfully...!!!")
    elif option == 5:
        pid = input("Enter Your ID:")
        mail = input("Enter Your Mail:")
        cur = con.cursor()
        sql = "UPDATE data set mail=%s where pid=%s"
        cur.execute(sql, (mail, pid))
        con.commit()
        select()
        print("\n")
        print("Update Successfully...!!!")
    else:
        print("Invalid")

def delete():
    pid = input("Enter Your ID:")
    res = con.cursor()
    sql = "delete from data where pid=%s"
    res.execute(sql,(pid,))
    con.commit()
    print("\n")
    print("Record Deleted Successfully...!!!")

def quit():
    print("Exit")

while True:
    print("\n")
    print("1.Insert Record")
    print("2.Select Record")
    print("3.Update Record")
    print("4.Delete Record")
    print("5.Exit")
    print("\n")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        insert()
    if choice == 2:
        select()
    if choice == 3:
        update()
    if choice == 4:
        delete()
    if choice == 5:
        quit()
    #else:
        #print("Invalid Option...!!!")

