from random import randint

class Noeud:
    def __init__(self,nom):
        self.voisins=[]
        self.nom=nom
        self.visite=False

class Arete:
    def __init__(self,voyage,variabilite,tps):
        self.voyage=voyage
        self.time=tps
        self.variable=variabilite
    def add_time(self):
        self.time+=0.01

class Voiture:
    def __init__(self):
        self.Trajet_parcouru=[]
        self.Temps_passe=0


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
                Jct=Arete(['Lyon', 'Lille'],False,0)
            else:
                if i%2==0:
                    Jct=Arete(self.Jonctions[i],False,45)
                else:
                    Jct=Arete(self.Jonctions[i],True,0)
            self.Aretes_classes.append(Jct)




class Trouve_Chemins:
    def __init__(self,Depart,Arrivee,G):
        self.Noeuds=G.Villes_classes
        self.Aretes=G.Aretes_classes
        self.Liste_Chemins=[]
        self.printAllPaths(Depart,Arrivee)
        self.Chemins_Ordonnes()

    def printAllPathsUtil(self,u, d, path):

        u=[j for j in self.Noeuds if j.nom==u][0]
        u.visite=True
        path.append(u.nom)
        if u.nom == d:
            self.Liste_Chemins.append(list(path))
        else:
            for i in u.voisins:
                class_noeud=[j for j in self.Noeuds if j.nom==i][0]
                if class_noeud.visite== False:
                    self.printAllPathsUtil(class_noeud.nom, d, path)
        path.pop()
        u.visite=False


    def printAllPaths(self,s, d):
        for i in self.Noeuds:
            i.visite=False
        path = []
        self.printAllPathsUtil(s, d, path)

    def Chemins_Ordonnes(self):
        array=[]
        for i in self.Liste_Chemins:
            New_L=[]
            for j in range(len(i)-1):
                New_L.append([i[j],i[j+1]])
            array.append(New_L)
        self.array=array






def Plus_Court_Chemin(List,Way):
    mini=0
    total_temps=[]
    for i in range(len(List)):
        temps=0
        for j in List[i]:
            v=[k for k in Way if [j[0],j[1]]==k.voyage or [j[1],j[0]]==k.voyage][0]
            temps+=v.time
        total_temps.append(temps)
        mini=total_temps.index(min(total_temps))
    return List[mini],total_temps[mini]

G=Graphe(('Marseille','Lyon','Paris','Lille'),(['Paris','Lyon'],['Paris','Lille'],['Lille','Marseille'],['Lyon','Marseille']))
Chems=Trouve_Chemins('Paris','Marseille',G)




i=0
L_Car=[]
while i<4000:
    Car=Voiture()
    PATH=Plus_Court_Chemin(Chems.array,G.Aretes_classes)
    Car.Trajet_parcouru.append(PATH[0])
    Car.Temps_passe=round(PATH[1],1)
    L_Car.append(Car)
    for j in PATH[0]:
        v=[i for i in G.Aretes_classes if [j[0],j[1]]==i.voyage or [j[1],j[0]]==i.voyage][0]
        if v.variable==True:
            v.add_time()
    i+=1




























