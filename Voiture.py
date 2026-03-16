class Voiture:
    def __init__(self,matricule,annee,marque,kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur=None
    def afficher_info(self):
        print("voiture",self.marque)
        print("annee",self.annee)
        print("matricul",self.matricule)
        print("kilometrage",self.kilometrage)
        print("chauffeur",self.chauffeur)
        if self.chauffeur:
            print("Assignee a ",self.chauffeur.nom)
        else:
            print("Aucune chauffeur")