import random

class pesoArista:
    vcarro = 20000 #m
    def __init__(self, dist):
        self.dist = dist
        self.t=[]

    def mru(self):
        for i in self.dist:
            self.t.append(self.dist[i]/self.vcarro)

    def trafico(self, hora):
        if hora >= 13 and hora <= 18:
            for i in self.t:
                self.t[i] = self.t[i] * (random.randint(1,3)/10)
        if hora >= 7 and hora < 13:
            for i in self.t:
                self.t[i] = self.t[i] * (random.randint(1,5)/10)
        if hora >18 and hora < 7:
            for i in self.t:
                self.t[i] = self.t[i] * (random.randint(1,5)/100)

    def actualizarGrafo(self, hora, n):
        self.trafico(hora)

        g=[[] for _ in range(len(n))]
        for i in range(len(n)):
            for j in range(len(n)-1):
                if  n[i].getY() == n[j].getY():
                    g[i].append(((n[j].getID(),abs(self.t[i]))))
                if n[i].getX() == n[j].getX():
                    g[i].append(((n[j].getID(),abs(self.t[i]))))
        return g

                     