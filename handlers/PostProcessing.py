import numpy as np
import statistics as st

class PostProcessing:
    def __new__(pp, energy):
        postProcess = super().__new__(pp)
        return postProcess

    def __init__(self,energy):
        self.energies = energy
        self.dev_std = self.std_dev()
        self.average = self.average_energy()
        
    def std_dev(self):
        return np.std(self.energies)
    
    def average_energy(self):
        return st.mean(self.energies)