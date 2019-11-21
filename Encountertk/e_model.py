'''
Module to carry out common encounter rate calculations and modeling
'''

import numpy as np

'''
This file contains classes and functions related to calculating encounter rates and in the
particle section, parameters associated with particle spectra.

The class EncounterModel can serve as a base class to build increasingly complex encounter rate models
and the values it's methods return are in a format that plays nicely with etk's associated plotting functions.

Here and everywhere when making use of oceanographic data you need to be absolutely certain that the units are consistent.
Everywhere possible I've tried to specifiy the units needed for constants and variables '''

class EncounterModel():
    ''' Base class for encounter rate model.
    Requires: an encounter rate kernel value,
    Cell concentration of population 1 (pop1c) list of concentrations,
    Cell concentration of population 2 (pop2c) list of concentrations.
    Concentrations can be a scalar or list of concentrations '''

    def __init__(self,pop2c,kernel,pop1c=[1]):
        self.kernel = kernel
        self.pop1c = pop1c
        self.pop2c = pop2c

    def set_kernel(self,kernel):
        self.kernel = kernel

    def get_kernel(self):
        return self.kernel

    def calc_encounter(self):
        ''' Calculate the encounter rate between two populations. The concentrations must
        be in list format. The encounter rate is returned as a list of arrays'''
        if len(self.pop1c) == 1:
            assert (self.pop1c[0] != 0), "Requires non-zero concentrations"
        elif len(self.pop2c) == 1:
            assert (self.pop2c[0] != 0), "Requires non-zero concentrations"

        self.e_rate = [self.kernel*np.multiply(self.pop2c,p1) for p1 in self.pop1c]
        return self.e_rate

# ------------------------------------------------------------------------------------
'''
Functions dealing with particle spectra and encounter.
'''

from sympy import *

#Using a symbolic math library makes this much more readable. I hope you would agree.
r = symbols('r')

'''
This is the calculation used in Lambert et al. to caculate total encounter for a particle spectra.
All length units must be in cm for this to work.
rmin: minimum particle radius to consider (cm)
rmax: max. particle radius to consider (cm)
r0: reference particle diameter in psd power law (cm)
B: absolute value of psd slope (cm^-4)
D: Diffusivity of bacterium (cm^2 s^-1)
v: kinematic viscosity of water (roughly 0.01 cm^2 s^-1)
Returns: search time in seconds.
'''

def ps_encounter(rmin,rmax,D,r0,N0,B,v):
        expr = (4*N0*D*np.pi*r*(r/r0)**(-B))*(1+0.619*(((0.13*r**0.26)*r/v)**0.412)*(v/D)**(1/3))
        e_total = integrate(expr,(r,rmin,rmax))
        return e_total

'''
Mean volume encountered by a bacterium within a particle landscape. All parameters have the same definition as
above.
Returns: mean volume encountered in um
'''

def mean_vol_encountered(rmin,rmax,D,r0,N0,B,v):
        expr = ((16/3)*N0*D*(np.pi**2)*(r**4)*(r/r0)**(-B)*(1+0.619*(((0.13*r**0.26)*r/v)**0.412)*(v/D)**(1/3))
        mean_vol = integrate(expr,(r,rmin,rmax))
        return mean_vol

if __name__ == "__main__":
    print("Here's a toy example with two populations")
    model = EncounterModel(kernel=1,pop1c = [1,5,10],pop2c = [1,5,10])
    e = model.calc_encounter()
