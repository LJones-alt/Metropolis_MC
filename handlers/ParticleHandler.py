import random as rand

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