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
                Jct=Arete(['Lyon', 'Lille'],False,0)
            else:
                if i%2==0:
                    Jct=Arete(self.Jonctions[i],False,45)
                else:
                    Jct=Arete(self.Jonctions[i],True,0)
            self.Aretes_classes.append(Jct)


class Voiture:
    def __init__(self):
        self.Trajet_parcouru=[]
        self.Temps_passe=0



def Chemins_Ordonnes(Liste):
    array=[]
    for i in Liste:
        New_L=[]
        for j in range(len(i)-1):
            New_L.append([i[j],i[j+1]])
        array.append(New_L)
    return array


#Situation avec le path Lyon Lille= 0 temps
G=Graphe(('Marseille','Lyon','Paris','Lille'),(['Paris','Lyon'],['Paris','Lille'],['Lille','Marseille'],['Lyon','Marseille'],['Lyon','Lille']))

Noeuds1= G.Villes_classes
Route1 =G.Aretes_classes
Liste_possible1=[['Paris','Lille','Marseille'],['Paris','Lyon','Marseille'],['Paris','Lyon','Lille','Marseille'],['Paris','Lille','Lyon','Marseille']]
Chemins1=Chemins_Ordonnes(Liste_possible1)




#Situation sans chemin =0 temps.
G2=Graphe(('Marseille','Lyon','Paris','Lille'),(['Paris','Lyon'],['Paris','Lille'],['Lille','Marseille'],['Lyon','Marseille']))

Noeuds2= G2.Villes_classes
Route2 =G2.Aretes_classes
Liste_possible2=[['Paris','Lille','Marseille'],['Paris','Lyon','Marseille']]
Chemins2=Chemins_Ordonnes(Liste_possible2)


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


def Way_Out(Chemin,Route):
    i=0
    L_Car=[]
    while i<4000:
        Car=Voiture()
        PATH=Plus_Court_Chemin(Chemin,Route)
        Car.Trajet_parcouru.append(PATH[0])
        Car.Temps_passe=round(PATH[1],1)
        L_Car.append(Car)
        for j in PATH[0]:
            v=[i for i in Route if [j[0],j[1]]==i.voyage or [j[1],j[0]]==i.voyage][0]
            if v.variable==True:
                v.add_time()
        i+=1
    return L_Car




Test_Sans_Autoroute_Flash= Way_Out(Chemins2,Route2)
Test_Avec_Autoroute_Flash= Way_Out(Chemins1,Route1)























