SELECt * FROM etudiant
WHERE age = (SELECT MAX(age) FROM etudiant);