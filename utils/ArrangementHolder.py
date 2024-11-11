'''
This is a custom class to hold info about a specific test. 
To use, init and then assign/ read as you please

Todo : make public / private access

Author: Laura Jones
Contact : Laura.Jones3@liverpool.ac.uk
'''
class Arrangement:
    def __init__(self):
        self.particle_index = int(0)
        self.coord = []
        self.ljp = 0
        self.distances = []