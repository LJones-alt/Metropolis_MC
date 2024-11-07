import matplotlib.pyplot as plt 
import mpl_toolkits as tk

a = 5.256    #Angstroms
p1 = [0, 0, 0]
p2 = [a, 0, 0]
p3 = [a, a, 0]
p4 = [0, a, 0]
p5 = [0, 0, a]
p6 = [a, 0, a]
p7 = [a, a, a]
p8 = [0, a, a]
p9 = [a/2, a/2, a]
p10 = [0, a/2, a/2]
p11 = [a/2, 0, a/2]
p12 = [a/2, a/2, 0]
p13 = [a, a/2, a/2]
p14 = [a/2, a, a/2]

unit_cell_coords = []
unit_cell_coords.append(p1)
unit_cell_coords.append(p2)
unit_cell_coords.append(p3)
unit_cell_coords.append(p4)
unit_cell_coords.append(p5)
unit_cell_coords.append(p6)
unit_cell_coords.append(p7)
unit_cell_coords.append(p8)
unit_cell_coords.append(p9)
unit_cell_coords.append(p10)
unit_cell_coords.append(p11)
unit_cell_coords.append(p12)
unit_cell_coords.append(p13)
unit_cell_coords.append(p14)

print('Original unit cell coordinates:')
print()
print(unit_cell_coords)
print()

def extend_unit_cell(atom_coords, expansion = 3):
    extended_coords = []
    for x_offset in range(expansion):
        for y_offset in range(expansion):
            for z_offset in range(expansion):
                for x, y, z in atom_coords:
                    new_x = x + x_offset
                    new_y = y + y_offset
                    new_z = z + z_offset
                    extended_coords.append((new_x, new_y, new_z))
    return extended_coords

extended_cell_coords = extend_unit_cell(unit_cell_coords, expansion = 3)

print('New unit cell coordinates:')
print()
print(extended_cell_coords)
print()
print('New number of atomic coordinates is', len(extended_cell_coords))

print()
flag = 0
for i in range(0, len(unit_cell_coords)):
    for j in range(i+1, len(unit_cell_coords)):
        if unit_cell_coords[i] == unit_cell_coords[j]:
            flag = 1
if flag == 1:
    print('Two of the coordinates are equal')
else:
    print('None of the coordinates are equal')

fig = plt.figure()
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')
 
coords = extended_cell_coords
 
# plotting
for i in range (len(coords)):
    plt_this = coords[i]
    ax.plot3D(plt_this[0], plt_this[1], plt_this[2], c='r', marker='o')
ax.set_title('3D line plot geeks for geeks')
plt.show()
