# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import random
import pylab
from Patients import Patient, TreatedPatient
from Viruses import SimpleVirus, ResistantVirus
#from ps3b_precompiled_36 import *

def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    nTimeSteps = 300
    virPopList = [0] * nTimeSteps
    for each in range(numTrials):
        viruses = [SimpleVirus(maxBirthProb, clearProb) for i in range(numViruses)]
        patient = Patient(viruses, maxPop)
        for i in range(nTimeSteps):
            patient.update()
            virPopList[i] += patient.getTotalPop()

    virPopList = [i / numTrials for i in virPopList]

    # pylab.title("SimpleVirus simulation")
    # pylab.xlabel("Time Steps")
    # pylab.ylabel("Average Virus Population")
    # pylab.plot(virPopList, label = "SimpleVirus")
    # pylab.legend(loc = "best")
    # pylab.show()
    return virPopList


# simulationWithoutDrug(100, 1000, 0.1, 0.05, 100)


def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    nTimeSteps = 150
    virPopList = [0] * nTimeSteps * 2
    resistVirPopList = [0] * nTimeSteps * 2
    for each in range(numTrials):
        viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses)]
        patient = TreatedPatient(viruses, maxPop)
        for i in range(nTimeSteps):
            patient.update()
            virPopList[i] += patient.getTotalPop()
            resistVirPopList[i] += patient.getResistPop(["guttagonol"])
        patient.addPrescription("guttagonol")
        for i in range(nTimeSteps):
            patient.update()
            virPopList[nTimeSteps + i] += patient.getTotalPop()
            resistVirPopList[nTimeSteps + i] += patient.getResistPop(["guttagonol"])


    virPopList = [i / numTrials for i in virPopList]
    resistVirPopList = [i / numTrials for i in resistVirPopList]

    # pylab.title("ResistantVirus simulation")
    # pylab.xlabel("Time Steps")
    # pylab.ylabel("Average Virus Population")
    # pylab.plot(virPopList, label = "SimpleVirus")
    # pylab.plot(resistVirPopList, label = "ResistantVirus")
    # pylab.legend(loc = "best")
    # pylab.show()
    return (virPopList, resistVirPopList)


if __name__ == "__main__":
    random.seed(0)
    #simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)
    simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)
    simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)

    #simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 100)
