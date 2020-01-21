"""
Phoebe O'Carroll-Moran, s1624742
CMod Ex 2.3

Creates two functions that
generate the morse potential
between two particles and the
resulting force they experience

"""

# imports needed libraries

import sys
import math
import numpy as np
import matplotlib.pyplot as pyplot
from Particle3D import Particle3D
   
def from_file_system(file_handle):

    """
     Calculates potential

      :file_handle: handle of the given file
      :param dt: timestep as float
      :param r_e: controls the position of the potential minimum
      :param D_e: controls the depth of the potential minimum
      :param alpha: controls the position of the potential minimum
      :return: data in file assigned to above parameters
    """
    
    # opens file with given name
    file_handle = open(file_handle,"r")
    
    line = file_handle.readline()
    data  = line.split(",")
    # assigns numbers in file to variables
    numstep = int(data[0])
    time = float(data[1])
    alpha = float(data[2])
    r_e = float(data[3])
    D_e = float(data[4])

    return numstep,time,alpha,r_e,D_e

def potential(dist,r_e,D_e,alpha):

    """
    Calculates potential

    :param dist: timestep as float
    :param dist: vector separation of the two particles
    :param r_e: controls the position of the potential minimum
    :param D_e: controls the depth of the potential minimum
    :param alpha: controls the position of the potential minimum
    :return: potential between particles
    """
    
    # find length of separation vector
    dist = np.linalg.norm(dist)
    diff = dist - r_e
    # return potential
    potential = D_e*(((1-(np.exp(-alpha*diff)))**2)-1)
    return potential


def force_dw(dist,r_e,D_e,alpha):
    """
    Calculates forces

    :param dist: vector separation of the two particles
    :param r_e: controls the position of the potential minimum
    :param D_e: controls the depth of the potential minimum
    :param alpha: controls the position of the potential minimum
    :return: the force on one partcle due to the other
    
    """
    
    dist_unit =  dist/np.linalg.norm(dist)
    dist = np.linalg.norm(dist)
    diff = dist - r_e
    # return force
    force = 2*alpha*D_e*((1-np.exp(-alpha*(diff)))*np.exp(-alpha*(diff)))*dist_unit
    return -force

