#https://computingforgeeks.com/install-mariadb-10-on-ubuntu-18-04-and-centos-7/
#apt update
#sudo apt install libmariadb3 libmariadb-dev
#pip3 install mariadb
#pip install mysql-connector-python

import mysql
from datetime import date,datetime,timedelta
import mysql.connector as mariadb

GRANT ALL PRIVILEGES ON cursoplatzi.* TO 'alice'@'localhost' IDENTIFIED BY  'clave';

mariadb_connection = mariadb.connect(user='alice', password='secreto', database='cursoplatzi')


mariadb_connection.close()

#quiery
SELECT author_id,name,nationality FROM authors AS a WHERE nationality IN ('USA','MEX') Limit 10 ;

query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")
"""
hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)
cursor.execute(query, (hire_start, hire_end))"""
query = ("SELECT author_id,name,nationality FROM authors AS a WHERE nationality IN (%s,%s) Limit %s")
uno='USA'
dos='MEX'
tres=10
cursor=mariadb_connection.cursor()
cursor.execute(query, (uno,dos,tres))

for (author_id,name,nationality) in cursor:
  print("{}, {} {}".format(
    author_id,name,nationality))

cursor.close()


####inser

tomorrow = datetime.now().date() + timedelta(days=1)

add_employee = ("INSERT INTO transactions "
               "(book_id, client_id, type, created_at, finished) "
               "VALUES (%s, %s, %s, %s, %s)")
add_salary = ("INSERT INTO salaries "
              "(emp_no, salary, from_date, to_date) "
              "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

INSERT INTO transactions (book_id, client_id, type, created_at, finished) VALUES (3, 2, 'sell',  '1977-06-14',0);
data_employee = (3, 20, 'sell', '1977-06-14 22:10:01',0)

# Insert new employee
cursor.execute(add_employee, data_employee)

# Make sure data is committed to the database
mariadb_connection.commit()

cursor.close()