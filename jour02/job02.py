import mysql.connector

cnx = mysql.connector.connect(user='root', password='n21217916',
                              host='localhost',
                              database='laplateforme')

cursor=cnx.cursor()

table_etage="""CREATE TABLE etage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    numero INT,
    superficie INT
);"""

table_salle="""
CREATE TABLE salle (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    id_etage INT,
    capacite INT
);"""

cursor.execute(table_etage)
cursor.execute(table_salle)
cursor.execute("SHOW TABLES")

results=cursor.fetchall()
print(results)

cnx.commit()
cursor.close()
cnx.close()
