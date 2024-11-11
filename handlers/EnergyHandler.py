'''
This is a LJP calculator. Init this calss with the epsilon and sigma values
Call get_total_energy(<your coordinate list>) to return the LJP for an ENITIRE arrangement
Call get_new_energy(<your coordinate list>) to return JUST the LJP for a single particle resp. all others

Once called, these can be accessed as total_energy for the total or energies for a list of all LJPs
'''
from utils.ArrangementHolder import Arrangement as ar

class LJ:
    def __new__(ch, eps, sig):
       # print('Creating new cluster object')
        handler = super().__new__(ch)
        return handler
    
    def __init__(self, eps:float, sig: float):
        self.epsilon = eps
        self.sigma = sig
        self.energies=[]
        self.total_energy=0
        self.ljp = 0

    def __calculate_ljp(self,x : float):
        if (x!=0):
            r=x/self.sigma
            self.ljp = 4*self.epsilon*(pow(r, (-12)) - pow(r, (-6)))
        else :
            self.ljp=0
        ##print(f"The LJP of {x} is {self.ljp}")
        return self.ljp
    
    def get_total_energy(self, distances: list):
        self.particles, x = distances.shape
        energies = []
        energy_sum = 0.0
        for b in range(self.particles):
            for a in range(b, self.particles):
                energies.append(self.__calculate_ljp(distances[b,a]))
       ## print(energies)
        energy_sum=sum(energies)
        self.energies = energies
        self.total_energy = energy_sum
        return energy_sum

    def get_new_energy(self, test_state:ar ):
        self.particles = len(test_state.distances)
        energies = []
        energy_sum = 0.0
        for a in range(self.particles):
            ## calculate LJP from the changed distances
            energies.append(self.__calculate_ljp(test_state.distances[a]))
       ## print(energies)
        energy_sum=sum(energies)
        self._partial_energies = energies
        
        return energy_sum