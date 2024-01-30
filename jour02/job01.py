import mysql.connector

cnx = mysql.connector.connect(user='root', password='n21217916',
                              host='localhost',
                              database='laplateforme')

cursor=cnx.cursor()

cursor.execute('SELECT * FROM etudiant')

results=cursor.fetchall()

print(results)

cursor.close()
cnx.close()