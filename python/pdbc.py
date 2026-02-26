# import mysql.connector

# sql = "CREATE DATABASE db_pdbc"

# con = mysql.connector.connect(
#     user='root',
#     host='localhost',
#     password='varsh789'
# )

# cursor = con.cursor()
# cursor.execute(sql)

# con.close()
# print("Database created successfully")




# import mysql.connector

# sql = "CREATE TABLE employee(emp_id int, emp_name varchar(50), emp_salary float)"

# con = mysql.connector.connect(
#     user='root',
#     host='localhost',
#     password='varsh789',
#     database='db_pdbc'
# )

# cursor = con.cursor()
# cursor.execute(sql)

# con.close()
# print("employee table  created successfully")



# import mysql.connector

# sql = "INSERT INTO employee values(101,'Sai',80000)"

# con = mysql.connector.connect(
#     user='root',
#     host='localhost',
#     password='varsh789',
#     database='db_pdbc'
# )

# cursor = con.cursor()
# cursor.execute(sql)
# con.commit()
# con.close()



# import mysql.connector

# sql = "insert into employee values(%s,%s,%s)"

# con = mysql.connector.connect(
#     user='root',
#     host='localhost',
#     password='varsh789',
#     database='db_pdbc'
# )

# cursor = con.cursor()
# m_r=[(102,'kumar',34000),
#      (103,'ravi',89000),
#      (104,'ram',56000),
#      (105,'keerthi',76000)]
# cursor.executemany(sql,m_r)
# con.commit()
# con.close()
# print("inserted many rows")



# import mysql.connector

# sql = "insert into employee values(%s,'%s',%s)"

# con = mysql.connector.connect(
#     user='root',
#     host='localhost',
#     password='varsh789',
#     database='db_pdbc'
# )

# cursor = con.cursor()
# n=int(input('no of employee: '))
# for x in range(n):
#     emp_id=int(input('enter employee id:  '))
#     emp_name=input('enter employee name:  ')
#     emp_salary=int(input('enter employee salary:  '))

# cursor.execute(sql%(emp_id,emp_name,emp_salary))
# con.commit()
# con.close()
# print("inserted  rows using for loop")


# while loop to insert multiple rows


# import mysql.connector

# sql = "insert into employee values(%s,'%s',%s)"

# con = mysql.connector.connect(
#     user='root',
#     host='localhost',
#     password='varsh789',
#     database='db_pdbc'
# )

# cursor = con.cursor()

# while True:
#     emp_id=int(input('enter employee id:  '))
#     emp_name=input('enter employee name:  ')
#     emp_salary=int(input('enter employee salary:  '))

#     cursor.execute(sql%(emp_id,emp_name,emp_salary))
#     con.commit()

#     cont = input("Do you want to add another employee? (y/n): ").lower()
#     if cont != 'y':
#         print("Finished inserting employees.")
#         break

# 'delete'
# import mysql.connector
# sql = "delete from employee where emp_id=101"
# con = mysql.connector.connect(
#     user='root',
#     host='localhost',   
#     password='varsh789',
#     database='db_pdbc'
# )
# cursor = con.cursor()
# cursor.execute(sql)
# con.commit()
# # con.close()

# 'update'
# import mysql.connector
# sql = "update employee set emp_salary=90000 where emp_id=102"
# con = mysql.connector.connect(
#     user='root',
#     host='localhost',
#     password='varsh789',
#     database='db_pdbc'
# )
# cursor = con.cursor()
# cursor.execute(sql)
# con.commit()
# con.close()


'read'

import mysql.connector
sql = "select * from employee"
con = mysql.connector.connect(
    user='root',
    host='localhost',

    password='varsh789',
    database='db_pdbc'  
)
cursor = con.cursor()   
cursor.execute(sql)
data = cursor.fetchall()    
for row in data:
    print(row)
con.close()

'we have fetchone fetchmany(2) fetch all'

