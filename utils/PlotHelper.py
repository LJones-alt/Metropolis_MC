import matplotlib.pyplot as plt 
import mpl_toolkits as tk
import matplotlib.animation as animation 

class PlotHandler:
    def __init__(self):
        self.original = []

    def plot_all_coords(self, coords):
        fig = plt.figure()
        
        ax = plt.axes(projection ='3d')
        
        for i in range (len(coords)):
            plt_this = coords[i]
            ax.plot3D(plt_this[0], plt_this[1], plt_this[2], c='r', marker='o')
        ax.set_title('Final Layout of the Atoms in the cube')
        
        plt.show()

    def animate_plotting(self, original, updated_position, updated_index):
        fig = plt.figure()
        ax = plt.axes(projection ='3d')
        artists = []
        for i in range(len(original)):
            plt_this = original[i]
            plt_x = plt_this[0]
            plt_y = plt_this[1]
            plt_z = plt_this[2]
            container = ax.plot3D(plt_x, plt_y, plt_z, c='r', marker='o')
            artists.append(container)
    
    def plotRDF(self, g_r, rad):
        plt.plot(rad, g_r, 'o')
        plt.show()
        
