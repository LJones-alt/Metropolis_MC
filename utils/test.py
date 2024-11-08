import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation
from FiileHelper import FileHelper 

fh = FileHelper()
all_data=[]
all_data.append(fh.get_matrix_from_file("11-08-11-49-16T298.txt"))
all_data.append(fh.get_matrix_from_file("11-08-11-37-02T150.txt"))





fig, ax = plt.subplots()
ax = plt.axes(projection ='3d')


artists = []
x_vals = []
y_vals = []
z_vals= []
for k in range(len(all_data)):
    for j in range(len(all_data[k])):
        holdt = all_data[k]
        hold=holdt[j]
        x_vals.append(hold[0])
        y_vals.append(hold[1])
        z_vals.append(hold[2])
    for i in range(len(all_data)):
    
        container = ax.plot3D(x_vals[i], y_vals[i], z_vals[i], c='r', marker='o')
    artists.append(container)


ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=400)
plt.show()