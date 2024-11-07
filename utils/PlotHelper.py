import matplotlib.pyplot as plt 
import mpl_toolkits as tk

class PlotHandler:
    def plot_all_coords(coords):
        fig = plt.figure()
        
        ax = plt.axes(projection ='3d')
        
        for i in range (len(coords)):
            plt_this = coords[i]
            ax.plot3D(plt_this[0], plt_this[1], plt_this[2], c='r', marker='o')
        ax.set_title('Original Layout of the Atoms in the cube')
        
        plt.show()