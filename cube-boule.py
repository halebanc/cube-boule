from vpython import *
import random
import sys

c=4 #cote du mur
e=0.1 #eppaisseur du mur
r=0.2 #rayon boule
ral=0.01 #ralentissement de la vitesse 
nombre=10 #nombre de particule
ortho=False

class atome():
    def __init__(self, cote, rayon, eppaiseur, masse, x, y, z, dico):
        self.dico=dico
        self.touche=cote-rayon-eppaiseur
        self.couleur=vec(random.random(), random.random(), random.random())
        self.balle = sphere(pos=vector(x, y, z), color=self.couleur, radius=r, make_trail=False)
        self.balle.p = vector(( (random.random()/ral)*2)-1, ((random.random()/ral)*2)-1, ((random.random()/ral)*2)-1)
        self.balle.masse=masse
    def bouger(self):
        dt=0.001
        rate(500)
        self.balle.pos = self.balle.pos+(self.balle.p/self.balle.masse)*dt
        if ((self.touche <= self.balle.pos.x) or ((-self.touche)>= self.balle.pos.x)):
            self.balle.p.x = -self.balle.p.x
        if ((self.touche <= self.balle.pos.y) or ((-self.touche) >= self.balle.pos.y)):
            self.balle.p.y = -self.balle.p.y
        if ((self.touche <= self.balle.pos.z) or ((-self.touche) >= self.balle.pos.z)):
            self.balle.p.z = -self.balle.p.z
        

        for variable in self.dico.keys():
            particule=globals()[variable]
            xp=particule.balle.pos.x
            yp=particule.balle.pos.y
            zp=particule.balle.pos.z
            if (r>abs(xp-self.balle.pos.x) and r>abs(yp-self.balle.pos.y) and r>abs(zp-self.balle.pos.z) and 0.000001<abs(zp-self.balle.pos.z)):
                
                if (self.balle.p.x>=0):
                    self.balle.p.x=-(abs(self.balle.p.x)+abs(particule.balle.p.x))/2
                    particule.balle.p.x=(abs(self.balle.p.x)+abs(particule.balle.p.x))/2
                    

                    self.balle.pos.x = self.balle.pos.x-(r-abs(xp-self.balle.pos.x))/2
                    particule.balle.pos.x = particule.balle.pos.x+(r-abs(xp-self.balle.pos.x))/2
                
                elif (self.balle.p.x<0):
                    self.balle.p.x=(abs(self.balle.p.x)+abs(particule.balle.p.x))/2
                    particule.balle.p.x=-(abs(self.balle.p.x)+abs(particule.balle.p.x))/2


                    self.balle.pos.x = self.balle.pos.x+(r-abs(xp-self.balle.pos.x))/2
                    particule.balle.pos.x = particule.balle.pos.x-(r-abs(xp-self.balle.pos.x))/2
                
                if (self.balle.p.y>=0):
                    self.balle.p.y=-(abs(self.balle.p.y)+abs(particule.balle.p.y))/2
                    particule.balle.p.y=(abs(self.balle.p.y)+abs(particule.balle.p.y))/2


                    self.balle.pos.y = self.balle.pos.y-(r-abs(yp-self.balle.pos.y))/2
                    particule.balle.pos.y = particule.balle.pos.y+(r-abs(yp-self.balle.pos.y))/2  
                
                elif (self.balle.p.y<0):
                    self.balle.p.y=(abs(self.balle.p.y)+abs(particule.balle.p.y))/2
                    particule.balle.p.y=-(abs(self.balle.p.y)+abs(particule.balle.p.y))/2

                    
                    self.balle.pos.y = self.balle.pos.y+(r-abs(yp-self.balle.pos.y))/2
                    particule.balle.pos.y = particule.balle.pos.y-(r-abs(yp-self.balle.pos.y))/2  
                
                if (self.balle.p.z>=0):
                    self.balle.p.z=-(abs(self.balle.p.z)+abs(particule.balle.p.z))/2
                    particule.balle.p.z=(abs(self.balle.p.z)+abs(particule.balle.p.z))/2


                    self.balle.pos.z = self.balle.pos.z-(r-abs(zp-self.balle.pos.z))/2
                    particule.balle.pos.z = particule.balle.pos.z+(r-abs(zp-self.balle.pos.z))/2

                elif (self.balle.p.z<0):
                    self.balle.p.z=(abs(self.balle.p.z)+abs(particule.balle.p.z))/2
                    particule.balle.p.z=-(abs(self.balle.p.z)+abs(particule.balle.p.z))/2


                    self.balle.pos.z = self.balle.pos.z+(r-abs(zp-self.balle.pos.z))/2
                    particule.balle.pos.z = particule.balle.pos.z-(r-abs(zp-self.balle.pos.z))/2

                 
                
#gestion des arguments
def argument_gestion(liste):
    suivant=2
    for i in liste[1:]:
        if (i[0]=="-"):
            if i[1]=="c":
                if suivant<len(liste):
                    global c
                    c=int(liste[suivant])
            elif i[1]=="r":
                if suivant<len(liste):
                    global r
                    r=float(liste[suivant]) 
            elif i[1]=="n":
                if suivant<len(liste):
                    global nombre
                    nombre=int(liste[suivant])
            elif i[1]=="v":
                if suivant<len(liste):
                    global ral
                    ral=1/float(liste[suivant])
            elif i[1]=="o":
                global ortho
                ortho=True
            elif i[1]=="h":
                print("Aide programme (x est un float et n un entier):\n-c n  pour la longeur des cotes du cube\n-r x pour le rayon des boules\n-n n pour le nombre de boules\n-v x pour la vitesse des boules\n-o pour afficher un repere orthonome\n-h pour ce message d'aide")
                sys.exit()
        suivant+=1

argument_gestion(sys.argv)
print(c)


#corps du programme 
if ortho:    
    arrow(pos=vector(0, 0, 0), axis=vector(1, 0, 0), color=color.red) 
    arrow(pos=vector(0, 0, 0), axis=vector(0, 1, 0), color=color.red) 
    arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), color=color.red) 

#creation de la box 
mur_d = box(pos=vector( c, 0, 0), size=vector(e,2*c-e, 2*c+e), color=color.blue)
mur_g = box(pos=vector(-c, 0, 0), size=vector(e,2*c-e, 2*c+e), color=color.blue)
mur_h = box(pos=vector(0,  c, 0), size=vector(2*c+e, e, 2*c+e), color=color.green)
mur_b = box(pos=vector(0, -c, 0), size=vector(2*c+e, e, 2*c+e), color=color.green)
mur_f = box(pos=vector(0, 0, -c), size=vector(2*c-e, 2*c-e, e), color=color.white)



dico_atome={}
for i in range(0, nombre):
    dico_atome["atome"+str(i)]=(0, 0, 0)
    
for q in dico_atome.keys():
    continuer=True
    while continuer:
        x=(random.random()*((2*c)-(4*r)))-(c-(2*r))
        y=(random.random()*((2*c)-(4*r)))-(c-(2*r))
        z=(random.random()*((2*c)-(4*r)))-(c-(2*r))
        dico_atome[q]=x, y, z
        for xp, yp, zp in dico_atome.values():
            if (r>abs(xp-x) and r>abs(yp-y) and r>abs(zp-z) and 0.0001<abs(zp-z)):
                #print("x: ",x, "y :", y, "z :", z )
                continuer=True
                break
            else:
                continuer=False

        
    globals()[q]=atome(c, 0.4, e, 1, x, y, z, dico_atome)
    
while(True):
    for g in dico_atome.keys():
        globals()[g].bouger()

