import sqlite3


###connect to database
connection=sqlite3.connect("student.db")

## Create a cursor object to insert record, create table
cursor=connection.cursor()

##Create the table
table_info="""
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

## Insert some more records
cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sabba','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Mukesh','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Sahad','Devops','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','Data Science','B',70)''')

## Display all records
print("The inserted records are")
data= cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit the changes in database 
connection.commit()
connection.close()


