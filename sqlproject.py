import mysql.connector

cnx = mysql.connector.connect(user='',password='',
                              host='',
                              database='')
cursor= cnx.cursor()
listi=[]
query = ' SELECT * FROM stuf ORDER BY height DESC,weight ASC ;'
cursor.execute(query)
for (name , weight ,height) in cursor:
    print(name , height ,weight)
cnx.close() 