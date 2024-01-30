import mysql.connector

cnx = mysql.connector.connect(user='root', password='n21217916',
                              host='localhost',
                              database='laplateforme')

cursor=cnx.cursor()

cursor.execute('SELECT SUM(capacite) FROM salle')

results = cursor.fetchone()[0]
results= int(results)


print("La capacité de toutes les salles est de :",results)

cursor.close()
cnx.close()