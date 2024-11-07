from Handlers import LJ, Boxes, Distances
distanceHelper = Distances([[0,0,0], [1,1,1]], 2,2,2)
lennard_jones = LJ(0.34, 0.0104, distanceHelper.get_all_distances()[1,0])

lennard_jones.get_total_energy(distanceHelper.get_all_distances())
print(lennard_jones.get_total_energy(distanceHelper.get_all_distances()))