import MySQLdb

db = MySQLdb.connect('localhost', 'testuser', 'test123', 'testdb')

cursor = db.cursor()

sql_insert = """ insert into EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) values ('Mac', 'Monah', 20, 'M', 2009)"""

sql_create = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
cursor.execute(sql_create)

try:
    cursor.execute(sql_insert)
    db.commit()
except:
    db.rollback()

sql_select = "select * from EMPLOYEE where income > %d" % (1000)

try:
    cursor.execute(sql_select)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print "fname=%s, lname=%s, age=%d, sex=%s, income=%d" % \
              (fname, lname, age, sex, income)
except:
    print 'Error: unable to fetch data'
#data = cursor.fetchall()
#print "Database version: %s " % data

db.close()