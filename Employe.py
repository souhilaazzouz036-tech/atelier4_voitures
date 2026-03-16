class Employe:
    def __init__(self, numeropermis,nom,prenom):
        self.numeropermis = numeropermis
        self.nom = nom
        self.prenom = prenom
        self.voitureservice=None
    def afficherInformations(self):
        print("Employee",self.nom,self.prenom)
        print("permis",self.numeropermis)
        if self.voitureservice:
            print("voiture assignee:", self.voitureservice.marque,self.voitureservice.matricule)
        else:
            print("Aucune voiture assignee")
    def affectervoiture(self,voiture):
        if self.voitureservice is not None:
            print("cet employee a deja une viture")
            return
        if voiture.chauffeur is not None:
            print("cette voiture a deja attribuee")
            return
        self.voitureservice = voiture
        voiture.chauffeur =self

    def retirervoiture(self):
        if self.voitureservice is None:
            print("Aucune voiture a retirer")
            return
        self.voitureservice.chauffeur = None
        self.voitureservice = None


