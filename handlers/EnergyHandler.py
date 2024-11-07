class LJ:
    def __new__(ch, eps, sig):
       # print('Creating new cluster object')
        handler = super().__new__(ch)
        return handler
    
    def __init__(self, eps, sig):
        self.epsilon = eps
        self.sigma = sig
        
        self.ljp = 0

    def calculate_ljp(self,x):
        if (x!=0):
            r=x/self.sigma
            self.ljp = 4*self.epsilon*(pow(r, (-12)) - pow(r, (-6)))
        else :
            self.ljp=0
        ##print(f"The LJP of {x} is {self.ljp}")
        return self.ljp
    
    def get_total_energy(self, distances):
        self.particles, x = distances.shape
        energies = []
        energy_sum = 0.0
        for b in range(self.particles):
            for a in range(b, self.particles):
                energies.append(self.calculate_ljp(distances[b,a]))
       ## print(energies)
        energy_sum=sum(energies)
        self.energies = energies
        self.total_energy = energy_sum
        return energy_sum