from Employe import Employe
from Voiture import Voiture
e1=Employe("12345","Ali","Karim")
e2=Employe("23456","souhila","azzouz")


v1=Voiture("AA123",2023,"TOYOTA",50000)
v2=Voiture("BA1236",2022,"HONDA",20000)


print("=======Situation initiale=========")
e1.affectervoiture(v1)
e2.affectervoiture(v2)
e1.afficherInformations()
e2.afficherInformations()

print("\n*****Retirer une voiture*****")
e1.retirervoiture()

e1.afficherInformations()

print("========Test ERROR!=========")
e2.affectervoiture(v2)


