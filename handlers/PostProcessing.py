import numpy as np
import statistics as st
import rdfpy as rdf

class PostProcessing:
    def __new__(pp, energy):
        postProcess = super().__new__(pp)
        return postProcess

    def __init__(self,energy):
        self.energies = energy
        self.dev_std = self.std_dev()
        self.average = self.average_energy()
        self.cv = 0
        
    def std_dev(self):
        print(f"Srd dev is {np.std(self.energies)}")
        return np.std(self.energies)
    
    def average_energy(self):
        return st.mean(self.energies)
    
    def calc_heat_capacity(self, k,t,v):
        cv = (1/(k*(t**2)))*(( (self.dev_std)**2)/len(self.energies))+ ((v/2)*k)
        self.cv = cv
        return cv

    def calc_drf(self, distances, steps):
        
        g_r , rad = rdf(distances, steps)
        return g_r, rad
