'''
This is the post-processing class for the simaltions. 
This can be handled outside of the main run if needed

Init this class with the list of energies (current / test / accpeted ).
Post-processing values can then get access as:
 dev_std (standard deviation)
 average (mean average)
 cv (heat capacity) (required parameters as shown in the function definition)

 Todo : get all these by reading from a file
 
Author: Laura Jones
Contact : Laura.Jones3@liverpool.ac.uk
'''
import numpy as np
import statistics as st


class PostProcessing:
    def __new__(pp, energy: list):
        postProcess = super().__new__(pp)
        return postProcess

    def __init__(self,energy:list):
        self.energies = energy
        self.dev_std = self.std_dev()
        self.average = self.average_energy()
        self.cv = 0
        
    def std_dev(self):
        print(f"Srd dev is {np.std(self.energies)}")
        return np.std(self.energies)
    
    def average_energy(self):
        return st.mean(self.energies)
    
    def calc_heat_capacity(self, k: float, t:float, v: float):
        cv = (1/(k*(t**2)))*(( (self.dev_std)**2)/len(self.energies))+ ((v/2)*k)
        self.cv = cv
        return cv

