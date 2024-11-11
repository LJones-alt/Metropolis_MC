'''
This is the plotting class, it contains the fuctions needed to make pretty plots
Init this class, then pass the snapshots from the simulation by add_sapshot(<your coordinate list>)
To plot a coordinate array, use plot_all_coords(<your coordinate list>)

Todo : add animation and evolving plot functions

Author: Laura Jones
Contact : Laura.Jones3@liverpool.ac.uk

'''
import matplotlib.pyplot as plt 
import mpl_toolkits as tk
import matplotlib.animation as animation 
#from utils import FileHelper 

class PlotHandler:
    def __init__(self):
        self.original = []
        self.array_holder=[]

    def plot_all_coords(self, coords : list):
        fig = plt.figure()
        
        ax = plt.axes(projection ='3d')
        
        for i in range (len(coords)):
            plt_this = coords[i]
            ax.plot3D(plt_this[0], plt_this[1], plt_this[2], c='r', marker='o')
        ax.set_title('Final Layout of the Atoms in the cube')
        
        plt.show()

    def add_snapshot(self, snap : list):
        self.array_holder.append(snap)

    def animate_plotting(self):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        
        data = self.array_holder[1]
       
       
    