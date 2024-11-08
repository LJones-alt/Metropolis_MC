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
from utils.FiileHelper import FileHelper

# First, set up the comparision object
clusterHolder = Holder()
clusterHolder.l = 2000
clusterHolder.iterations = 1000
clusterHolder.temp = 298
# Set up the coordinates of the initial state, set a for Argon
a=525.6 #pm
coodinateHandler= CoordinateHandler(a)
# assign these to the comparision object
clusterHolder.original_array = coodinateHandler.get_all_cords()
clusterHolder.current_state = coodinateHandler.get_all_cords() ## refernce to original array 

# Init the objects needed 
acceptanceCounter = AcceptanceCounter()
plthandle = PlotHandler()
lennard_jones = LJ(0.34, 0.0104) 
test_lennard_jones=LJ(0.34, 0.0104)

# Calculate all the distances between the atoms calculated earlier
distanceHelper = Distances(coodinateHandler.get_all_cords(), clusterHolder.l) # calculates all relative distances
plthandle.original = clusterHolder.original_array
# calculate the energy of the entire system and hold in the cluster onbject
clusterHolder.current_energy=lennard_jones.get_total_energy(distanceHelper.distances)

# Now iterate over tiny movements until the iteration threshold is reached
for i in range(clusterHolder.iterations) : 

    # move a random particle a random amount in random distance
    move_particle = ParticleMover(clusterHolder.temp, clusterHolder.current_state, clusterHolder.l)
    # assign to the test arrangement state
    clusterHolder.test_state=move_particle.move_random()
    # calculate the distances in the new arrangement
    test_distancehelper = Distances(clusterHolder.test_state, clusterHolder.l)
    #calculate the energies and assign to the test energy 
    clusterHolder.test_energy=test_lennard_jones.get_total_energy(test_distancehelper.distances)
    ##print(f"old energy{clusterHolder.current_energy}, test :  {clusterHolder.test_energy}")
    # decide to keep or reject the new arrangement
    keep_current = acceptanceCounter.decide(clusterHolder.current_energy, clusterHolder.test_energy)
    if keep_current :
        # if the new arrangement is chosen, assign the current state to the test state
        clusterHolder.current_state = clusterHolder.test_state
        clusterHolder.current_energy = clusterHolder.test_energy
        clusterHolder.energies.append(clusterHolder.test_energy)
    plthandle.add_snapshot(clusterHolder.current_state)
    print(f"Accepted {acceptanceCounter.get_accepted()}, rejected {acceptanceCounter.get_rejected()}")
    del move_particle
    del test_distancehelper
    # ## increment
# Save final geometery in text file
plthandle.animate_plotting()
fileholder =FileHelper()
fileholder.write_list_to_file(clusterHolder.current_state,clusterHolder.temp)

# Calculate the averages and Std deviation
postProcess = PostProcessing(clusterHolder.energies)
print(f"Average Energy : {clusterHolder.current_energy}, Averager Accepted energy : {postProcess.average}, Std Deviation of accepted energes : {postProcess.dev_std}")
print(f"Accepted {acceptanceCounter.get_accepted()}, rejected {acceptanceCounter.get_rejected()}")
Cv = postProcess.calc_heat_capacity(0.00008617,clusterHolder.temp,3)
print(f"CV : {Cv}")
# plot the final arrangement 

plthandle.plot_all_coords(clusterHolder.current_state)
#PlotHandler.plot_all_coords(clusterHolder.original_array)

#plthandle.plotRDF(postProcess.calc_drf(clusterHolder.current_state, 0.1))

