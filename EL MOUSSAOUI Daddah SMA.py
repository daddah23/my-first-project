import mesa
import random

class vendeur(mesa.Agent):
    def __init__(self,ID,model):
        super().__init__(ID,model)
        self.unique_id1 = ID
        self.prix1 = random.randint(1, 10)
        self.nombrelivre = 10
    def getprix(self):
        return self.prix1

    def ventlivre (self):
        if self.nombrelivre > 0:
            self.nombrelivre -= 1
            return 1
        else:
            return 0


class Agent(mesa.Agent):
    def __init__(self,ID,model):
        super().__init__(ID,model)
        self.unique_id = ID
        self.argent = 10
        self.livre = 0


    def step(self):
            vendeurs = self.random.choice(self.model.plannificateur1.agents)
            if vendeurs is not None:
                meilleurprix = vendeurs.getprix()
                if meilleurprix <= self.argent:
                    print("Je suis l'agent %d et j'ai %d " % (self.unique_id, self.argent))
                    self.argent -= meilleurprix
                    print("apres l'achat j'ai %d " % (self.argent))


class Environnement(mesa.Model):
    def __init__(self,N,N1):
        super().__init__()
        self.num_agents = N
        self.num_vendeur = N1
        self.plannificateur = mesa.time.RandomActivation(self)
        self.plannificateur1 = mesa.time.RandomActivation(self)
        for i in range(N):
            a = Agent(i,self)
            self.plannificateur.add(a)
        for i in range(N1):
            a = vendeur(i, self)
            self.plannificateur1.add(a)
    def step(self):
        self.plannificateur.step()


model = Environnement(3,2)
model.step()
