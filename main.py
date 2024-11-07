from Handlers import LJ, ParticleMover, Distances, PostProcessing
from Utils import PlotHandler, CoordinateHandler, AcceptanceCounter

## First, create an array with all coordinate

class Holder:
    def __init__(self):
        self.original_array =[]
        self.current_state = []
        self.test_state = []
        self.current_energy = 0
        self.original_array = 0
        self.test_energy = 0
        self.l= 2000
        self.energies = []
        


a=525.6 #pm
coodinateHandler= CoordinateHandler(a)
## show existing points
clusterHolder = Holder()
acceptanceHandler = AcceptanceCounter()
clusterHolder.original_array = coodinateHandler.get_all_cords()
clusterHolder.current_state = coodinateHandler.get_all_cords() ## refernce to original array 

##PlotHandler.plot_all_coords(coodinateHandler.get_all_cords())
distanceHelper = Distances(coodinateHandler.get_all_cords(), clusterHolder.l) # calculates all relative distances

lennard_jones = LJ(0.34, 0.0104) # calculate LJ in eV nm

clusterHolder.current_energy=lennard_jones.get_total_energy(distanceHelper.get_all_distances())
##print(lennard_jones.get_total_energy(distanceHelper.get_all_distances())) # print the energy 
acceptanceCounter = AcceptanceCounter()
i=0
while i <100 : 

    move_particle = ParticleMover(500, -500, clusterHolder.current_state)
    clusterHolder.test_state=move_particle.move_random()
    #print(move_particle.move_random(distanceHelper.particle_array))

    test_distancehelper = Distances(clusterHolder.test_state, clusterHolder.l)
    test_lennard_jones = LJ(0.34, 0.0104)
    clusterHolder.test_energy=test_lennard_jones.get_total_energy(test_distancehelper.get_all_distances())
    keep_current = acceptanceCounter.decide(clusterHolder.current_energy, clusterHolder.test_energy)
    print(f"old energy{clusterHolder.current_energy}, test :  {clusterHolder.test_energy}")
    if keep_current :
        clusterHolder.current_state = clusterHolder.test_state
        clusterHolder.current_energy = clusterHolder.test_energy
        clusterHolder.energies.append(clusterHolder.test_energy)
        
    print(f"Accepted {acceptanceCounter.get_accepted()}, rejected {acceptanceCounter.get_rejected()}")
    
    i=i+1

print(f"Accepted {acceptanceCounter.get_accepted()}, rejected {acceptanceCounter.get_rejected()}")
PlotHandler.plot_all_coords(clusterHolder.current_state)
PlotHandler.plot_all_coords(clusterHolder.original_array)
postProcess = PostProcessing(clusterHolder.energies)
print(f"Average Energy : {clusterHolder.current_energy}, Averager Accepted energy : {postProcess.average}, Std Deviation of accepted energes : {postProcess.std_dev}")




