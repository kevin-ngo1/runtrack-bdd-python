import mysql.connector

cnx = mysql.connector.connect(user='root', password='n21217916',
                              host='localhost',
                              database='laplateforme')

cursor=cnx.cursor()


insert_etage="""INSERT INTO etage (nom, numero, superficie)
VALUES
('RDC', 0, 500),
('R+1', 1, 500);"""

insert_salle="""INSERT INTO salle (nom, id_etage, capacite)
VALUES
('Lounge', 1, 100),
('Studio Son', 1, 5),
('Broadcasting', 2, 50),
('Bocal Peda', 2, 4),
('Coworking', 2, 80),
('Studio Video', 2, 5);"""

cursor.execute(insert_etage)
cursor.execute(insert_salle)

cnx.commit()
cursor.close()
cnx.close()
