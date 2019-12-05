'''
Module to carry out common encounter rate calculations and modeling

This file is separated broadly into two sections. The first is for basic encounter
rate modeling. This being between predator-prey, cells and viruses, bacteria and particles.
Most of the heavy lifting is done through the EncounterModel class. In order to effectively use this class
you must know the encounter rate kernel for your process of interest. There are a number of kernels
supplied in the kernels.py module and the Kernel class allows you to simply define your own
symbolically. If that is more complex than desired, custom numeric values can be input directly.

The class EncounterModel can serve as a base class to build increasingly complex encounter rate models
and the values it's methods return are in a format that plays nicely with etk's associated plotting functions.

The second portion of this file is related to microbial foraging in marine particle landscapes. This code is
the basis for the analyses carried out in Lambert et al. 2019 (L&O: Letters) and Lambert et al. 2020 (Currently on
the biorxiv). The functions provided allow calculation of specific total encounter rate between a microbe and particles
in a landscape defined by the particle slope spectrum and the power law coefficient. Example data and usage of these functions are
presented in the Examples folder.

Here and everywhere when making use of oceanographic data you need to be absolutely certain that the units are consistent.
Everywhere possible I've tried to specifiy the units needed for constants and variables '''

'''

import numpy as np


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

    def calc_encounter_range(self):
        ''' Calculate the encounter rate between two populations across varying
        cell concentrations. The concentrations must be in list format.
        The encounter rate is returned as a list of arrays.
        This can be a useful function to explore encounter rates across permutations of
        cell concentrations'''

        if len(self.pop1c) == 1:
            assert (self.pop1c[0] != 0), "Requires non-zero concentrations"
        elif len(self.pop2c) == 1:
            assert (self.pop2c[0] != 0), "Requires non-zero concentrations"

        self.e_rate = [self.kernel*np.multiply(self.pop2c,p1) for p1 in self.pop1c]
        return self.e_rate

    def calc_encounter_pairwise(self):
        ''' Calculate encounter row-wise. Useful in the case of discrete samples with
        defined cell concentrations. E.g. oceanographic station data.
        '''
        self.e_rate = self.kernel*np.multiply(self.pop1c,self.pop2c)
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
        expr_v = ((16/3)*N0*D*(np.pi**2)*(r**4)*(r/r0)**(-B))*(1+0.619*(((0.13*r**0.26)*r/v)**0.412)*(v/D)**(1/3))
        mean_v = integrate(expr_v,(r,rmin,rmax))
        return mean_v

if __name__ == "__main__":
    print("Here's a toy example with two populations")
    model = EncounterModel(kernel=1,pop1c = [1,5,10],pop2c = [1,5,10])
    e = model.calc_encounter()
