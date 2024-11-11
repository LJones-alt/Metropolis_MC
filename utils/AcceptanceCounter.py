'''
This is the acceptance handler class, it accepts or rejects a new energy 
and keeps track of the number accepted or rejected

To use, just init the class. 
call decide() to compare two Arrangemnt objects. Returns TRUE to accept the object

Call get_accepted() or get_rejected() to get the current number of accepted / rejected comparisions

Author: Laura Jones
Contact : Laura.Jones3@liverpool.ac.uk
'''
import numpy as np
import random as rand
from utils.ArrangementHolder import Arrangement as ar

class AcceptanceCounter():
    def __init__(self):
        self.accept=0
        self.reject=0
    
    def decide(self,e1:ar , e2: ar):
        if e1.ljp>=e2.ljp :
            self.__increment_accept()
            return True
        
        else :
            p=np.exp((-(e2.ljp-e1.ljp))/((8.617*((10)**(-5)))*300))
            randomnum=rand.uniform(0,1)
            if p<randomnum:
                self.__increment_accept()
                return True
            else:
                self.__increment_reject()
                return False 
    
    def __increment_accept(self):
        self.accept = self.accept+1
    
    def __increment_reject(self):
        self.reject = self.reject+1

    def get_accepted(self):
        return self.accept

    def get_rejected(self):
        return self.reject

