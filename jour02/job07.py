import mysql.connector

class Employe:
    def __init__(self, user, password, host, database):
        self.cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
        self.cursor = self.cnx.cursor()

    def create_employe(self, nom, prenom, salaire, id_service):
        exec = f"INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('{nom}', '{prenom}', {salaire}, {id_service})"
        self.cursor.execute(exec)
        self.cnx.commit()

    def read_all_employes(self):
        self.cursor.execute("SELECT * FROM employe")
        return self.cursor.fetchall()
    
    def read_employe_id(self, id_employe):
        exec_read_id = f"SELECT * FROM employe WHERE id = {id_employe}"
        self.cursor.execute(exec_read_id)
        return self.cursor.fetchone()
    
    def update_employes(self,id_employe,what,change):
        exec_upd = f"UPDATE employe SET {what} = {change} WHERE id = {id_employe}"
        self.cursor.execute(exec_upd)
        self.cnx.commit()

    def delete_employes(self,id_employe):
        exec_del = f"DELETE FROM employe WHERE id = {id_employe}"
        self.cursor.execute(exec_del)
        self.cnx.commit()

    def close(self):
        self.cursor.close()
        self.cnx.close()

restaurant_panda=Employe('root',"n21217916","localhost","restaurant")
restaurant_panda.create_employe('Pal','Michel',3000.00,1)
print(restaurant_panda.read_all_employes())
restaurant_panda.update_employes(5,"salaire",100)
print(restaurant_panda.read_employe_id(5))
restaurant_panda.delete_employes(5)
print(restaurant_panda.read_all_employes())
restaurant_panda.close()