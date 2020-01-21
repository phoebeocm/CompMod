"""
Phoebe O'Carroll-Moran, s1624742
CMod Ex 2.4 - Velocity Verlet Method

This code produces plots of the relative positions of two oscillating particles and its energy, both as function of time. Also saves both to file.
Evolution of position and velocity are calculated using Velcocity Verlet methods.
Parameters and initial conditions are obtained from a user-input file.

"""
# import libraries and functions

import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from Particle3D import Particle3D
import statistics as st
from MorsePotential import *
from Frequency import *

def main():

    #have the user enter which particle type they want to simulate
    particle_prompt = input("Which particle are you looking to simulate? Type O or N ")
    
    if particle_prompt == "O":
        p1 = Particle3D.from_file("oxygen1.txt")
        p2 = Particle3D.from_file("oxygen2.txt")
        numstep,time,alpha,r_e,D_e = from_file_system("oxygen_parameters.txt")
         
    elif particle_prompt == "N":
        p1 = Particle3D.from_file("nitrogen1.txt")
        p2 = Particle3D.from_file("nitrogen2.txt")
        numstep,time,alpha,r_e,D_e = from_file_system("nitrogen_parameters.txt")
    
    else:
        print("that doesn't look right!")
        exit()
        
    # have user specify timestep
    dt = input("Enter your preferred timestep: ")
    dt = float(dt)
         
    pos1 = p1.position
    pos2 = p2.position

    initial_dist12 = Particle3D.separation(p1,p2)
 
    # finds the initial energy value
    energy = p1.kinetic_energy() + p2.kinetic_energy() + potential(initial_dist12,r_e,D_e,alpha)
    
    # calculate initial force value
    force = force_dw(initial_dist12,r_e,D_e,alpha)
    print(force)
    
    #initialise data lists for plotting later
    initial_dist12 = np.linalg.norm(initial_dist12)
    time_list = [time*10.8E-15]
    pos_list = [np.linalg.norm(initial_dist12)]
    energy_list = [energy]
    
    #start time integration loop
    
    for i in range(numstep):
        
    # update time, position and energy values
    
        time += dt # time - appended later
        
        new_pos1 = p1.update_position2(dt,force)
        new_pos2 = p2.update_position2(dt,-force)
        new_dist = np.subtract(new_pos1,new_pos2)
        new_dist_norm = np.linalg.norm(new_dist)
        energy = p1.kinetic_energy() + p2.kinetic_energy() + potential(new_dist,r_e,D_e,alpha)
        
        # append energy and time data values to lists
        
        energy_list.append(energy)
        time_list.append(time*10.8E-15)
        pos_list.append(new_dist_norm)
        
        # assign current velocity to variables
        
        vel1 = p1.velocity
        vel2 = p2.velocity
        old_force = -force
        force = force_dw(new_dist,r_e,D_e,alpha)
        # update velocity values
        p1.velocity = p1.update_velocity2(dt,old_force,force)
        p2.velocity = p2.update_velocity2(dt,old_force,-force)
       
    # creates text files to contain energy and relative separation
    outfile_energy = open("VerletEnergy.txt","w")
    outfile_separation = open("VerletSeparation.txt","w")
    
    # for loop writing individual values of energy to file as strings
    for number in energy_list:
        outfile_energy.write(str(number))
    outfile_energy.close()
    
    # for loop writing individual values of position to file as strings
    for number in pos_list:
        outfile_separation.write(str(number))
    outfile_separation.close()

    frequency(pos_list,time_list)
    energy_vals(energy_list)
    
    # create two subplots
    fig, axs = plt.subplots(2, 1, constrained_layout=True)
    # plot trajectory to first subplot
    axs[0].plot(time_list, pos_list, '-')
    axs[0].set_title('Time vs. relative position')
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Relative Position')
    fig.suptitle('Verlet data', fontsize=16)

    # plot time and energy to second subplot
    axs[1].plot(time_list, energy_list, '-')
    axs[1].set_xlabel('Time')
    axs[1].set_title('Time vs. energy')
    axs[1].set_ylabel('Total Energy')

    plt.show()
    
main()
