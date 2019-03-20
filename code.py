#this code shows you how connect to your mysql instance and perform basic tasks
#install mysql driver first
import MySQLdb

#getting data from python
#replace with your database details
db = MySQLdb.connect(host='localhost', user = 'root', passwd= 'root', db = 'mydatabase')

#create a cursor object to execute your queries
cur = db.cursor()

#cur.execute("CREATE DATABASE mydatabase") create a database if database does not exist already
# to show databases 
cur.execute("SHOW DATABASES")


###### create a new table with keys
cur.execute("CREATE TABLE tablename (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), occupation VARCHAR(255))")

### view your table
for item in cur:
	print (item)
####################

#####insert multiply data into the table we created 
sqlquery = "INSERT INTO tablename (name, address) VALUES (%s, %s)"
content = [
  ('James', 'Teacher'),
  ('Chuks', 'Engineer'),
  ('Okey', 'Baker'),
  ('Haruna', 'Technician'),
  ('Blessing', 'Designer'),
  ('Jennifer', 'Software Developer'),
  ('Richard', 'Driver'),
  ('Julius', 'Typist'),
  ('Victoria', 'Preacher')
  
]

cur.executemany(sqlquery, content)

db.commit()

print(cur.rowcount, "was inserted.")

###### to select data from table
cur.execute("SELECT * FROM tablename")

#####print the first and second columns 
for row in cur.fetchall():
	print row[0], " ", row[1]

######select with a filter 
select_specific = "SELECT * FROM tablename WHERE occupation = 'Engineer'"
cur.execute(select_specific)
result = cur.fetchall()
for item in result:
	print (item)

#### sort in ascending or descending order
sort_query = "SELECT * FROM tablename ORDER BY occupation"
sort_query_descending = "SELECT * FROM tablename ORDER BY occupation DESC"
cur.execute(sort_query)
sort_result = cur.fetchall()
for item in sort_result:
	print (item)
for item in sort_query_descending:
	print (item)


###Delete rows from tables

delete_query = "DELETE FROM tablename WHERE name = 'Julius'"
cur.execute(delete_query)
db.commit()  ##this is required to make the changes 

### Delete tables 
delete_table_query = "DROP TABLE tablename"
###delete a table if it exists
delete_table_query = "DROP TABLE IF EXISTS tablename"
cur.execute(delete_table_query)

### add update/overide items in the table 
update_query = "UPDATE tablename SET name = 'Ben' WHERE name = 'Chuks'"
cur.execute(update_query)
db.commit()

##Limit 
limit_query = "SELECT * FROM tablename LIMIT 7 OFFSET 2"
cur.execute(limit_query)
result = cur.fetchall()
for item in result:
	print (item)


#Join tables
# we would create a new table so we can join the rows on the two tables 
cur.execute("CREATE TABLE newtable (id INT AUTO_INCREMENT PRIMARY KEY, location VARCHAR(255), gender VARCHAR(255))")

insert_query = "INSERT INTO newtable (location, gender) VALUES (%s, %s)"
content = [
  ('Nigeria', 'M'),
  ('Egypt', 'M'),
  ('Nigeria', 'M'),
  ('Sudan', 'M'),
  ('USA', 'F'),
  ('UK', 'F'),
  ('Canada', 'M'),
  ('Ghana', 'M'),
  ('Australia', 'F')
  
]

cur.executemany(sqlquery, content)

db.commit()

print(cur.rowcount, "was inserted.")

join_query = "SELECT \
tablename.name AS user, \
newtable.name AS details \
FROM users \
JOIN newtable ON users.occupation = newtable.id"

cur.execute(join_query)
result = cur.fetchall()
for item in result:
	print (item)
