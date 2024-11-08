from time import gmtime, strftime
import numpy as np
class FileHelper:
    def __init__(self):
        self.filename = self.get_file_name


    def write_list_to_file(self, save_list, temp):
        filename = f"{self.get_file_name()}T{temp}.txt"
        f= open(filename, "a")
        for i in range(len(save_list)):
            coord = save_list[i]
            f.write(f"{coord[0]}, {coord[1]}, {coord[2]}\n" )
        f.close
        print(f"Saved to {filename}")
    
    def get_file_name(self):
        return strftime("%m-%d-%H-%M-%S", gmtime())
    
    def get_matrix_from_file(self, filename):
        y=[]
        f = open(filename, 'r')     
        for line in f:                
            g=line.split(',')   ## split on space now         
            y.append(g)
        ##self.particle_coords=np.array(y).astype(np.float16)
        return np.array(y).astype(np.float16)