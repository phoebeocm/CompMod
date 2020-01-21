"""
Phoebe O'Carroll-Moran, s1624742
CMod Ex2.2: Particle 3D, a class to describe the properties of a 3D particle

"""

import numpy as np

class Particle3D:
    """
       Class to describe 3D particles.

       Properties:
       position(float) - an array containing the position component along all 3 axes
       velocity(float) - an array containing the velocity component along all 3 axes
       mass(float) - particle mass

       Methods:
       * formatted output
       * kinetic energy
       * first-order velocity update
       * first- and second order position updates
       * reading data from a file and using it to create and instance of a particle
       * finding the relative  vector separation of two particles
       """
       
    def __init__(self,pos,label,vel,mass):
        """
        Initialise a Particle3D instance
    
        :param pos: position as float
        :param vel: velocity as float
        :param mass: mass as float
        """
        self.position = pos
        self.label = label
        self.velocity = vel
        self.mass = mass


    def __str__(self):
        return "label = " + str(self.label) + ", position = " + str(self.position)
        """
        return a string setting out the parameters
        """
            
    def kinetic_energy(self):
        """
        Return kinetic energy as
        1/2*mass*vel^2
        """
        
        return 0.5*self.mass*(np.linalg.norm(self.velocity))**2
    
    def update_velocity(self,dt,force):
        """
        First-order velocity update,
        v(t+dt) = v(t) + dt*F(t)

        :param dt: timestep as float
        :param force: force on particle as float
        """
        self.velocity += dt*force/self.mass
        return self.velocity
    
    def update_velocity2(self,dt,force,force2):
        """
        Second-order velocity update,
        v(t+dt) = v(t) + dt*(F(t) + F(t + dt))/2*m

        :param dt: timestep as float
        :param force: force on particle as float
        """
        self.velocity += dt*(force + force2)/(2*self.mass)
        return self.velocity
        
    def update_position1(self, dt):
        """
        First-order position update,
        x(t+dt) = x(t) + dt*v(t)

        :param dt: timestep as float
        """
        
        self.position +=  dt*self.velocity
        
        return self.position
    
    def update_position2(self, dt, force):
        """
        Second-order position update,
        x(t+dt) = x(t) + dt*v(t) + 1/2*dt^2*F(t)

        :param dt: timestep as float
        :param force: current force as float
        """
        
        self.position += dt*self.velocity + (dt**2)*force/(2*self.mass)
        
        return self.position
        

    @staticmethod
    def from_file(file_handle):
    
        """
        Method to return the relative vector separation of the two particles
        :param file_handle: the handle of the file we'll be using

        """
        file_handle = open(file_handle,"r")
        
        line = file_handle.readline()
        data  = line.split(",")
        
        pos = map(float, data[0:3])
        pos = np.array(list(pos))
        
        vel = map(float, data[3:6])
        vel = np.array(list(vel))
        
        mass = float(data[6])
        label = str(data[7])
      
        return Particle3D(pos,label,vel,mass)

    @staticmethod
    def separation(p1,p2):
        """
        Method to return the relative vector separation of the two particles
        :param p1: particle 1
        :param p2: particle 2
        """
        r1 = p1.position
        r2 = p2.position
        sep =  r1 - r2
        return sep



