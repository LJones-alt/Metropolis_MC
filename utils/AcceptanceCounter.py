import numpy as np
import random as rand

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

