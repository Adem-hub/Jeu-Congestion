from random import randint

class Noeud:
    def __init__(self,nom):
        self.voisins=[]
        self.nom=nom

class Arete:
    def __init__(self,voyage,variabilite,tps):
        self.voyage=voyage
        self.time=tps
        self.variable=variabilite
    def add_time(self,temps):
        self.time+=0.01


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
        for i in range(len(self.Jonctions)):
            if self.Jonctions[i]==['Lyon','Lille']:
                Jct=Arete(['Lyon','Lille'],False,0)
            else:
                if i%2==0:
                    Jct=Arete(self.Jonctions[i],False,45)
                else:
                    Jct=Arete(self.Jonctions[i],True,15)
            self.Aretes_classes.append(Jct)


class Voiture:
    def __init__(self):
        self.Trajet_parcouru=[]
        self.Temps_passe=[]


G=Graphe(('Marseille','Lyon','Paris','Lille'),(['Paris','Lyon'],['Paris','Lille'],['Lille','Marseille'],['Lyon','Marseille'],['Lyon','Lille']))

Noeuds= G.Villes_classes
Route =G.Aretes_classes

def Chemin(A,B):
    #Algorithme de Djikstra (en carton mais ca marche quand même)
    L=[[0,[A,A]]]
    Liste_chemin_court=[B]
    visited=[]
    alli={i.nom:0 for i in Noeuds}
    Dico={A:[A,0]}
    provenance= L[0][1][0]
    w=0
    L.pop(0)
    while alli.keys()!=Dico.keys():
        class_noeud=[i for i in Noeuds if i.nom==provenance][0]
        for arrivee in class_noeud.voisins:
            if arrivee not in Dico.keys():
                v=[i for i in Route if [provenance,arrivee]==i.voyage or [arrivee,provenance]==i.voyage][0]
                L.append([v.time+w,[provenance,arrivee]])
        mini=0
        for i in range(len(L)):
            if L[i][0]<L[mini][0]:
                mini=i
        X=L.pop(mini)
        if X[1][1] not in Dico.keys():
            Dico[X[1][1]]=[X[1][0],X[0]]
            w+=X[0]
            provenance=X[1][1]
            print(Dico)
    Nd=B
    while Nd!=A:
        Nd=Dico[Nd][0]
        Liste_chemin_court.append(Nd)
    return Liste_chemin_court[::-1]























#Generation

#
# i=0
# while i<4000:
#     m=0
#     X=Chemin('Paris')
#     m+=X[0].time
#     x=Chemin([x for x in X[0].voyage if x!='Paris'][0])
#     m+=x.time()








