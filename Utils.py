import matplotlib.pyplot as plt 
import mpl_toolkits as tk
import random as rand
import numpy as np

class CoordinateHandler:
    def __new__(ch, a):
        handler = super().__new__(ch)
        return handler

    def __init__(self, a):
        self.a = a
        self.a1=[0,0,0]
        self.a2=[(self.a/((2)**0.5)),0,(self.a/((2)**0.5))]
        self.a3=[(self.a/((2)**0.5)),(self.a/((2)**0.5)),0]
        self.a4=[self.a,0,0]
        self.coords = self.get_all_cords()

    def get_all_cords(self):
        coords=[]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    coordscalc1=[self.a1[0]+i*self.a, self.a1[1]+j*self.a,self.a1[2]+k*self.a]
                    coordscalc2=[self.a2[0]+i*self.a,self.a2[1]+j*self.a,self.a2[2]+k*self.a]
                    coordscalc3=[self.a3[0]+i*self.a,self.a3[1]+j*self.a,self.a3[2]+k*self.a]
                    coordscalc4=[self.a4[0]+i*self.a,self.a4[1]+j*self.a,self.a4[2]+k*self.a]
                    
                    coords.append(coordscalc1)
                    coords.append(coordscalc2)
                    coords.append(coordscalc3)
                    coords.append(coordscalc4)
        return coords

class PlotHandler:
    def plot_all_coords(coords):
        fig = plt.figure()
        
        ax = plt.axes(projection ='3d')
        
        for i in range (len(coords)):
            plt_this = coords[i]
            ax.plot3D(plt_this[0], plt_this[1], plt_this[2], c='r', marker='o')
        ax.set_title('Original Layout of the Atoms in the cube')
        
        plt.show()

class AcceptanceCounter():
    def __init__(self):
        self.accept=0
        self.reject=0
        self.energies = []
    
    def decide(self,e1, e2):
        
        if e1>=e2 :
            self.increment_accept()
            return True
        
        else :
            p=np.exp((-(e2-e1))/((8.617*((10)**(-5)))*300))
            randomnum=rand.uniform(0,1)
            if p<randomnum:
                self.increment_accept()
                return True
            else:
                self.increment_reject()
                return False 


    def increment_accept(self):
        self.accept = self.accept+1
    
    def increment_reject(self):
        self.reject = self.reject+1

    def get_accepted(self):
        return self.accept

    def get_rejected(self):
        return self.reject


