import numpy as np 
import random as rand
import statistics as st
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
    
class Distances:
    def __new__(cls, particle_array, l):
        #print('Creating new distance object')
        cluster = super().__new__(cls)
        return cluster

    def __init__(self, particle_array, l):
        self.ljp =0
        self.l=l
        self.distance3d = 0
        self.particle_array = particle_array
        self.particles = len(self.particle_array)
        self.dims =3
        self.distances = []

    def get_delta(self, k1, k2, l):
        if (k1-k2) < (-0.5*l):
            return (k1-k2 +l)
        elif (-0.5*l) <= (k1-k2) <= (0.5*l):
            return (k1-k2)
        elif (k1-k2) > (0.5*l):
            return (k1-k2-l)
        else :
            return 0

    def get_particle_distance(self, p1, p2):
        particle_distance = pow(pow(self.get_delta(p1[0], p2[0], self.l), 2) + pow(self.get_delta(p1[1], p2[1], self.l), 2) + pow(self.get_delta(p1[2], p2[2], self.l),2),0.5)
        #print(f"The particle distance is {particle_distance}")
        return particle_distance
    
    def get_all_distances(self):
        distances = np.zeros((int(self.particles), int(self.particles)))
        for b in range(self.particles):
            for a in range(self.particles):
                distances[b,a]= self.get_particle_distance(self.particle_array[b], self.particle_array[a])
       # print(distances)
        return distances


class ParticleMover:
    def __init__(self, max, min, start_state):
        self.min = min
        self.max = max
        self.old_array = start_state
        self.new_array = []
        self.moved_particle=[]
       
    def move_random(self):
        new_array = list(self.old_array)
        particles =len(new_array)
        random_particle = rand.randint(0, particles-1)
        self.moved_particle = self.old_array[random_particle]
        self.index = random_particle
        self.moved_direction = [rand.uniform(self.min, self.max), rand.uniform(self.min, self.max), rand.uniform(self.min, self.max)]
        new_array[random_particle]= [self.moved_particle[0] + self.moved_direction[0], self.moved_particle[1] + self.moved_direction[1],self.moved_particle[2] + self.moved_direction[2]]
        ##print(f"moved particle {random_particle}, by {self.moved_direction}")
        return new_array

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
 
    