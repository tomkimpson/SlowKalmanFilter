#This is the test file for py_src/gravitational_waves.py 
from src import system_parameters,pulsars,synthetic_data
# import random 
import numpy as np 
# from numpy import sin,cos

"""Make sure that the data generated with the same seeds is the same, and different seeds is different"""
def test_seeding():

    # Seed 1
    P1   = system_parameters.SystemParameters(seed=1)    # User-specifed system parameters
    PTA1 = pulsars.Pulsars(P1)            # All pulsar-related quantities
    data1 = synthetic_data.SyntheticData(PTA1,P1) # Given the user parameters and the PTA configuration, create some synthetic data
    

    # Seed 1
    P2   = system_parameters.SystemParameters(seed=1)    # User-specifed system parameters
    PTA2 = pulsars.Pulsars(P2)            # All pulsar-related quantities
    data2 = synthetic_data.SyntheticData(PTA2,P2) # Given the user parameters and the PTA configuration, create some synthetic data
    

    #Seed 3
    P3   = system_parameters.SystemParameters(seed=3)    # User-specifed system parameters
    PTA3 = pulsars.Pulsars(P3)            # All pulsar-related quantities
    data3 = synthetic_data.SyntheticData(PTA3,P3)


    assert np.all(data1.f_measured==data2.f_measured)
    assert np.all(data1.f_measured!=data3.f_measured)


"""If no GW, the noiseless measured f and the state f should be the same"""
def test_no_GW():

   
    P   = system_parameters.SystemParameters(h=0.0)    # User-specifed system parameters
    PTA = pulsars.Pulsars(P)            # All pulsar-related quantities
    data = synthetic_data.SyntheticData(PTA,P) # Given the user parameters and the PTA configuration, create some synthetic data
    
    assert np.all(data.measurement_without_noise == data.state)

    #but the measured phi is differnt due to noise
    assert np.all(data.f_measured != data.state)


"""If gamma = 0 and sigma=0, f should be unchanged """
def test_no_f():
    P   = system_parameters.SystemParameters(σp=0,γ=0.0)    # User-specifed system parameters
    PTA = pulsars.Pulsars(P)            # All pulsar-related quantities
    data = synthetic_data.SyntheticData(PTA,P) #


    for i in range(PTA.Npsr):
        assert data.state[i,0] == data.state[i,-1] #for the ith pulsar, check the initial state is the same as the final state



