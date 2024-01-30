import mysql.connector

cnx = mysql.connector.connect(user='root', password='n21217916',
                              host='localhost',
                              database='laplateforme')

cursor=cnx.cursor()

cursor.execute('SELECT SUM(superficie) FROM etage')

results = cursor.fetchone()[0]
results= int(results)


print("La superficie de la Plateforme est de",results,"m²")

cursor.close()
cnx.close()