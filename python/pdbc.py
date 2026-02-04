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



import mysql.connector

sql = "insert into employee values(%s,'%s',%s)"

con = mysql.connector.connect(
    user='root',
    host='localhost',
    password='varsh789',
    database='db_pdbc'
)

cursor = con.cursor()
n=int(input('no of employee: '))
for x in range(n):
    emp_id=int(input('enter employee id:  '))
    emp_name=input('enter employee name:  ')
    emp_salary=int(input('enter employee salary:  '))

cursor.execute(sql%(emp_id,emp_name,emp_salary))
con.commit()
con.close()
print("inserted  rows using for loop")


