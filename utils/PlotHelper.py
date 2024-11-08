import matplotlib.pyplot as plt 
import mpl_toolkits as tk
import matplotlib.animation as animation 
from FiileHelper import FileHelper 

class PlotHandler:
    def __init__(self):
        self.original = []
        self.array_holder=[]

    def plot_all_coords(self, coords):
        fig = plt.figure()
        
        ax = plt.axes(projection ='3d')
        
        for i in range (len(coords)):
            plt_this = coords[i]
            ax.plot3D(plt_this[0], plt_this[1], plt_this[2], c='r', marker='o')
        ax.set_title('Final Layout of the Atoms in the cube')
        
        plt.show()

    def add_snapshot(self, snap):
        self.array_holder.append(snap)

    def animate_plotting(self):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        
        data = self.array_holder[1]
       
       
    