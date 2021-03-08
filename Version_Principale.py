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
    def add_time(self):
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
        for i in range(len(self.Jonctions)):
            if self.Jonctions[i]==['Lyon','Lille']:
                Jct=Arete(['Lyon','Lille'],False,0)
            else:
                if i%2==0:
                    Jct=Arete(self.Jonctions[i],False,45)
                else:
                    Jct=Arete(self.Jonctions[i],True,0)
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
    L=[]
    provenance= A
    w=0
    Liste_chemin_court=[B]
    alli={i.nom:0 for i in Noeuds}
    Dico={A:[A,0]}
    while alli.keys()!=Dico.keys():
        class_noeud=[i for i in Noeuds if i.nom==provenance][0]
        for arrivee in class_noeud.voisins:
            if arrivee not in Dico.keys():
                v=[i for i in Route if [provenance,arrivee]==i.voyage or [arrivee,provenance]==i.voyage][0]
                L.append([v.time+w,[provenance,arrivee]])
        mini=L.index(min([L[i] for i in range(len(L))]))
        X=L.pop(mini)
        if X[1][1] not in Dico.keys():
            Dico[X[1][1]]=[X[1][0],X[0]]
            w+=X[0]
            provenance=X[1][1]

    #Creation du path grace aux chemins trouvés
    Nd=B
    New_L=[]
    while Nd!=A:
        Nd=Dico[Nd][0]
        Liste_chemin_court.append(Nd)
    Liste_chemin_court=Liste_chemin_court[::-1]

    for i in range(len(Liste_chemin_court)-1):
        New_L.append([Liste_chemin_court[i],Liste_chemin_court[i+1]])
    return New_L,Liste_chemin_court





#Generation


i=0
L_Car=[]
while i<400:
    Car=Voiture()
    PATH=Chemin('Paris','Marseille')
    Car.Trajet_parcouru.append(PATH[1])
    L_Car.append(Car)

    for j in PATH[0]:
        v=[i for i in Route if [j[0],j[1]]==i.voyage or [j[1],j[0]]==i.voyage][0]
        print(v.__dict__)
        if v.variable==True:
            v.add_time()
    i+=1



























