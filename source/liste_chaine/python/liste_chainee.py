class Maillon:
    def __init__(self, valeur=None, suivant=None):
        self.valeur = valeur
        self.suivant = suivant
        
    def __repr__(self):
        if self.suivant is None:
            return "["+str(self.valeur)+"]->" + "[]"
        else:
            return "["+str(self.valeur)+"]->" +str(self.suivant)
        
class Liste:
    
    def __init__(self):
        self.maillon = None
        
    def est_vide(self):
        return self.maillon == None
    
    def tete(self):
        if not self.est_vide():
            return self.maillon.valeur
        
    def queue(self):
        q = Liste()
        if not self.est_vide():
            q.maillon = self.maillon.suivant
        return q
    
    def inserer(self,element):
        nv_maillon = Maillon(element)
        nv_maillon.suivant = self.maillon
        self.maillon = nv_maillon
        
    def __repr__(self):
        if self.maillon == None:
            return "[]"
        else:
            return str(self.maillon)