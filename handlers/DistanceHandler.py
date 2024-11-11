'''
This handler class does all the distance calculations for a particle in a coordinate list

To use, first init the class with the coordinate list and container wall length l
Call get_all_distances() to get all distances between ALL particles (slow, heavy, avoid)
Call get_new_distances(<particle index>) to get all the distances relative to just one particle (faster, more efficient)

Then access the list of distances from distances

Author: Laura Jones
Contact : Laura.Jones3@liverpool.ac.uk
'''
import numpy as np

class Distances:
    def __new__(cls, particle_array : list, l: float):
        #print('Creating new distance object')
        cluster = super().__new__(cls)
        return cluster

    def __init__(self, particle_array: list, l:float):
        self.ljp =0
        self.l=l
        self.distance3d = 0
        self.particle_array = particle_array
        self.particles = len(self.particle_array)
        self.dims =3
        self.distances = []

    def __del__(self):
        return None

    def __get_delta(self, k1, k2, l):
        if (k1-k2) < (-0.5*l):
            return (k1-k2 +l)
        elif (-0.5*l) <= (k1-k2) <= (0.5*l):
            return (k1-k2)
        elif (k1-k2) > (0.5*l):
            return (k1-k2-l)
        else :
            return 0

    def __get_particle_distance(self, p1, p2):
        particle_distance = pow(pow(self.__get_delta(p1[0], p2[0], self.l), 2) + pow(self.__get_delta(p1[1], p2[1], self.l), 2) + pow(self.__get_delta(p1[2], p2[2], self.l),2),0.5)
        #print(f"The particle distance is {particle_distance}")
        return particle_distance
    
    def get_all_distances(self):
        ## do this for the moved particle only!
        distances = np.zeros((int(self.particles), int(self.particles)))
        for b in range(self.particles):
            for a in range(self.particles):
                distances[b,a]= self.__get_particle_distance(self.particle_array[b], self.particle_array[a])
       # print(distances)
        self.distances = distances
        return distances

    def get_new_distances(self, index: int):
        new_distances = []
        for a in range(self.particles):
            new_distances.append(self.__get_particle_distance(self.particle_array[a], self.particle_array[index]))
        return new_distances