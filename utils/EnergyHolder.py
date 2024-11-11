'''
This is the setup class for the simulation. 
This holds the simulation parameters and keeps the current/ test variables

Holds a record of the accepted / rejected energies
Author: Laura Jones
Contact : Laura.Jones3@liverpool.ac.uk
'''
from utils.ArrangementHolder import Arrangement

class Holder:
    def __init__(self):
        self.iterations = 0
        self.temp = 0
        self.start_state = Arrangement()
        self.current_state = Arrangement()
        self.test_state = Arrangement()
        self.step_size = 0
        self.accepted_energies =[]