import sqlite3

#connection establishment
def sqlcon():
    global sqliteConnection,cur
    sqliteConnection=sqlite3.connect("sql.db")
    cur=sqliteConnection.cursor()
    
#table creation
def sqlcreate():
    query="create table Movies(name varchar(45),actor varchar(50),actress varchar(50),director varchar(50),year Integer);"
    cur.execute(query)
    
#table insertion
def sqlinsert():
    query1="Insert into Movies values('Rajakumara','Puneeth Rajkumar','Priya Anand','Santosh','2017');"
    query2="Insert into Movies values('kgf2','Yash','Sreenidhi','Prashanth Neel','2022');"
    query3="Insert into Movies values('Infinity War','Robert','Natasha','Anthony Russo','2018');"
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    sqliteConnection.commit()
    
#queries
def sqlselect():
    sqliteConnection=sqlite3.connect("sql.db")
    cur=sqliteConnection.cursor()
    query1="select * from Movies;"
    query2="select * from Movies where actor='Robert';"
    cur.execute(query1)
    result=cur.fetchall()   
    cur.execute(query2)
    result2=cur.fetchall()   
    print(result)
    print("\n")
    print(result2)
    
#function calls
sqlcon()
sqlcreate()
sqlinsert()
sqlselect()
