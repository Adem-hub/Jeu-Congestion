from random import randint

class Noeud:
    def __init__(self,nom):
        self.voisins=[]
        self.nom=nom

class Arete:
    def __init__(self,voyage):
        self.voyage=voyage
        self.time=randint(0,10)
    def add_time(self,temps):
        self.time+=0.1


class Graphe:
    def __init__(self,V,E):
        self.Villes=V
        self.Jonctions=E
        self.Villes_classes=[]
        self.Aretes_classes=[]
        self.Genere_Voisins()
        self.Genere_Aretes()

    def Genere_Voisins(self):
        for i in range(len(self.Villes)):
            Node=Noeud(self.Villes[i])
            for j in range(len(self.Jonctions)):
                if self.Villes[i] in self.Jonctions[j]:
                    Node.voisins.append([k for k in self.Jonctions[j] if k!=self.Villes[i]][0] )
            self.Villes_classes.append(Node)

    def Genere_Aretes(self):
        for i in self.Jonctions:
            Jct=Arete(i)
            self.Aretes_classes.append(Jct)


class Voiture:
    def __init__(self):
        self.Trajet_parcouru=[]
        self.Temps_passe=[]


G=Graphe(('Marseille','Lyon','Paris','Lille'),(['Paris','Lyon'],['Paris','Lille'],['Lille','Marseille'],['Lyon','Marseille']))

Noeuds= G.Villes_classes
Route =G.Aretes_classes

def Generer_Chemins_possibles(A,B):
    Liste=[]
    A=[i for i in Noeuds if i.nom==A][0]
    B=[i for i in Noeuds if i.nom==B][0]
    X=True
    while X:
        L=[A]
        noeud=A
        while noeud!=B:
            for i in range(Liste):
                if noeud==B:
                    pass










