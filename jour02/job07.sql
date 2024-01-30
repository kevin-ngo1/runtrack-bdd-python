CREATE DATABASE restaurant;

CREATE TABLE employe (
id INT AUTO_INCREMENT PRIMARY KEY,
nom VARCHAR(255),
prenom VARCHAR(255),
salaire DECIMAL(10,2),
id_service INT
);

INSERT INTO employe (nom, prenom, salaire, id_service)
VALUES
("Rauwens","William",300,1),
("Valle","Maxime",2200,1),
("Ngo","Kevin",3000,2),
("Serra","Mathis",100,2);

SELECT * FROM employe WHERE salaire > 3000;

SELECT employe.nom, employe.prenom,employe.salaire,employe.id_service,service.nom FROM employe
JOIN service ON employe.id_service=service.id;