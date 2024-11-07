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
        

# First, set up the comparision object
clusterHolder = Holder()
clusterHolder.l = 2000
clusterHolder.iterations = 100
# Set up the coordinates of the initial state, set a for Argon
a=525.6 #pm
coodinateHandler= CoordinateHandler(a)
# assign these to the comparision object
clusterHolder.original_array = coodinateHandler.get_all_cords()
clusterHolder.current_state = coodinateHandler.get_all_cords() ## refernce to original array 

# Init the objects needed 
acceptanceCounter = AcceptanceCounter()
lennard_jones = LJ(0.34, 0.0104) 
test_lennard_jones=LJ(0.34, 0.0104)

# Calculate all the distances between the atoms calculated earlier
distanceHelper = Distances(coodinateHandler.get_all_cords(), clusterHolder.l) # calculates all relative distances

# calculate the energy of the entire system and hold in the cluster onbject
clusterHolder.current_energy=lennard_jones.get_total_energy(distanceHelper.get_all_distances())

# Now iterate over tiny movements until the iteration threshold is reached
for i in range(clusterHolder.iterations) : 

    # move a random particle a random amount in random distance
    move_particle = ParticleMover(500, -500, clusterHolder.current_state)
    # assign to the test arrangement state
    clusterHolder.test_state=move_particle.move_random()
    # calculate the distances in the new arrangement
    test_distancehelper = Distances(clusterHolder.test_state, clusterHolder.l)
    #calculate the energies and assign to the test energy 
    clusterHolder.test_energy=test_lennard_jones.get_total_energy(test_distancehelper.get_all_distances())
    ##print(f"old energy{clusterHolder.current_energy}, test :  {clusterHolder.test_energy}")
    # decide to keep or reject the new arrangement
    keep_current = acceptanceCounter.decide(clusterHolder.current_energy, clusterHolder.test_energy)
    if keep_current :
        # if the new arrangement is chosen, assign the current state to the test state
        clusterHolder.current_state = clusterHolder.test_state
        clusterHolder.current_energy = clusterHolder.test_energy
        clusterHolder.energies.append(clusterHolder.test_energy)
        
    print(f"Accepted {acceptanceCounter.get_accepted()}, rejected {acceptanceCounter.get_rejected()}")
    ## increment

# Calculate the averages and Std deviation
postProcess = PostProcessing.PostProcessing(clusterHolder.energies)
print(f"Average Energy : {clusterHolder.current_energy}, Averager Accepted energy : {postProcess.average}, Std Deviation of accepted energes : {postProcess.std_dev}")
print(f"Accepted {acceptanceCounter.get_accepted()}, rejected {acceptanceCounter.get_rejected()}")

# plot the final arrangement 
PlotHandler.plot_all_coords(clusterHolder.current_state)
#PlotHandler.plot_all_coords(clusterHolder.original_array)
