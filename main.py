'''
This is a particle motion simulator
Author: Laura Jones
Contact : Laura.Jones3@liverpool.ac.uk

Clone this repos : git@github.com:LJones-alt/Metropolis_MC.git
'''
from utils.AcceptanceCounter import  AcceptanceCounter
from utils.CoordinateMaker import CoordinateHandler
from utils.PlotHelper import PlotHandler
from handlers.PostProcessing import PostProcessing
from handlers.DistanceHandler import Distances
from handlers.EnergyHandler import LJ
from handlers.ParticleHandler import ParticleMover
from utils.EnergyHolder import Holder
from utils.FileHelper import FileHelper

# First, set up the comparision object
clusterHolder = Holder()
clusterHolder.l = 2000
clusterHolder.iterations = 1000
clusterHolder.temp = 298
clusterHolder.step_size=10
# Set up the coordinates of the initial state, set a for Argon
a=525.6 #pm
coodinateHandler= CoordinateHandler(a)
# assign these to the comparision object
clusterHolder.start_state.coord = coodinateHandler.coords
clusterHolder.current_state.coord= coodinateHandler.coords ## refernce to original array 

# Init the objects needed 
acceptanceCounter = AcceptanceCounter()
plthandle = PlotHandler()
lennard_jones = LJ(0.34, 0.0104) 
test_lennard_jones=LJ(0.34, 0.0104)

# Calculate all the distances between the atoms calculated earlier
distanceHelper = Distances(clusterHolder.current_state.coord, clusterHolder.l) # calculates all relative distances
plthandle.original = clusterHolder.start_state.coord
# calculate the energy of the entire system and hold in the cluster onbject
clusterHolder.start_state.ljp=lennard_jones.get_total_energy(distanceHelper.get_all_distances())
#clusterHolder.current_state.ljp = clusterHolder.start_state.ljp
clusterHolder.current_state.ljp=0
# Now iterate over tiny movements until the iteration threshold is reached
for i in range(clusterHolder.iterations) : 

    # move a random particle a random amount in random distance
    move_particle = ParticleMover(clusterHolder.temp, clusterHolder.current_state.coord, clusterHolder.l)
    # assign to the test arrangement state
    clusterHolder.test_state.coord, clusterHolder.test_state.particle_index=move_particle.move_random()
    
    # calculate the distances in the new arrangement
    test_distancehelper = Distances(clusterHolder.test_state.coord, clusterHolder.l)
    clusterHolder.test_state.distances = test_distancehelper.get_new_distances(clusterHolder.test_state.particle_index)
    #calculate the energies and assign to the test energy 
    clusterHolder.test_state.ljp=test_lennard_jones.get_new_energy(clusterHolder.test_state )
   
    # decide to keep or reject the new arrangement
    keep_current = acceptanceCounter.decide(clusterHolder.current_state, clusterHolder.test_state)
    if keep_current :
        # if the new arrangement is chosen, assign the current state to the test state
        clusterHolder.current_state = clusterHolder.test_state
        clusterHolder.accepted_energies.append(clusterHolder.test_state.ljp)
    # Take snapshots
    if ((i%clusterHolder.step_size)==0):
        plthandle.add_snapshot(clusterHolder.current_state)

    print(f"Accepted {acceptanceCounter.get_accepted()}, rejected {acceptanceCounter.get_rejected()}")
    del move_particle
    del test_distancehelper
    # ## increment

#now we have finsished, find the overall energy
finalDistanceHelper = Distances(clusterHolder.current_state.coord, clusterHolder.l)
clusterHolder.current_state.distances=finalDistanceHelper.get_all_distances()
clusterHolder.current_state.ljp=test_lennard_jones.get_total_energy(clusterHolder.current_state.distances)

# Save final geometery in text file
fileIO = FileHelper()
fileIO.write_list_to_file(clusterHolder.current_state.coord, int(clusterHolder.temp))

# Calculate the averages and Std deviation - this could be done in a separate file
postProcess = PostProcessing(test_lennard_jones.energies)
print(f"Average Energy : {clusterHolder.current_state.ljp}, Averager Accepted energy : {postProcess.average}, Std Deviation of accepted energes : {postProcess.dev_std}")
print(f"Accepted {acceptanceCounter.get_accepted()}, rejected {acceptanceCounter.get_rejected()}")
Cv = postProcess.calc_heat_capacity(0.00008617,clusterHolder.temp,3)
print(f"CV : {Cv}")

# Uncomment these for plotting functions 

#plthandle.plot_all_coords(clusterHolder.current_state)
#PlotHandler.plot_all_coords(clusterHolder.original_array)

#plthandle.plotRDF(postProcess.calc_drf(clusterHolder.current_state, 0.1))

