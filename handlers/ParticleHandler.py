import random as rand

class ParticleMover:
    def __init__(self, temp, start_state, l):
        self.min, self.max = self.get_movement_from_cv(temp)
        self.old_array = start_state
        self.new_array = []
        self.moved_particle=[]
        self.l = l
    
    def __del__(self):
        return None


    def move_random(self):
        new_array = list(self.old_array)
        particles =len(new_array)
        random_particle = rand.randint(0, particles-1)
        self.moved_particle = self.old_array[random_particle]
        self.index = random_particle
        self.moved_direction = [rand.uniform(self.min, self.max), rand.uniform(self.min, self.max), rand.uniform(self.min, self.max)]
        test_coordinate= [self.moved_particle[0] + self.moved_direction[0], self.moved_particle[1] + self.moved_direction[1],self.moved_particle[2] + self.moved_direction[2]]
        new_array[random_particle] = self.check_for_escape(test_coordinate)
        
        ##print(f"moved particle {random_particle}, by {self.moved_direction}")
        return new_array
    
    def check_for_escape(self, test_coord):
        for i in range (len(test_coord)):
            if (test_coord[i] > self.l):
                test_coord[i] = test_coord[i] - self.l
        return test_coord
    
    def get_movement_from_cv(self, temp):
        if temp<=0:
           self.min = 0
           self.max = 0

        elif 0<temp<=80:
           self.min = -100
           self.max = 100

        elif 80<temp<=150:
            self.min = -500
            self.max = 500

        elif 150>temp<=300:
            self.min = -1500
            self.max = 1500
        else :
            self.min = 0
            self.max = 0
        return self.min, self.max

        
           

