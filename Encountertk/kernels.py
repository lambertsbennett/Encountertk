'''
Define encounter rate kernels. Establish class that enables users to create their own
kernel.
'''

from numpy import pi, abs
from _utils import calculate_diffusivity_rw

def diffusive_kernel(Di,Dj,ri,rj):
    ''' Encounter rate kernel for diffusive encounter.
    Requires: Diffusivity of population i, Diffusivity of population j,
    cell radius population i, cell radius population j.
    Returns: Encounter rate kernel for populations i,j. '''

    B_diff = 4*pi*(Di + Dj)*(ri + rj)
    return B_diff


def differential_settling_kernel(ri,ui,uj):
    ''' Encounter rate kernel for differential settling.
    Requires: radius of smaller particle/cell (ri), settling velocity of small particles (ui),
    settling velocity of larger cell (uj).
    Returns: Encounter rate kernel for populations i,j. '''

    B_settling = 0.5*pi*(ri**2)*abs(ui-uj)
    return B_settling

def feeding_current_kernel(r,u):
    ''' Encounter rate kernel for organisms cruising, sinking, or generating a feeding current.
    Requires: organism sensing radius (r), relative velocity between predator and prey (u).
    Returns: Encounter rate kernel for predator-prey interaction. '''

    B_fc = pi*(r**2)*u
    return B_fc

def pause_travel_kernel(r,f):
    ''' Encounter rate kernel for a pause-travel predator.
    Requires: organism sensing radius (r) and stop frequency (f).
    Returns: Encounter rate kernel for pause-travel predator. '''

    B_pt = (4/3)*pi*(r**3)*f
    return B_pt

def rand_walk_predator_kernel(r, D=10e-5,u=100,calc_D = False, tau =1):
    ''' Encounter rate kernel for random walk predator.
    Can either use known diffusivity of predator, or calculate D based on swimming
    behaviour.
    Requires: organism sensing radius (r), diffusivity (D).
    Optionally requires: Whether to calculate diffusivity (calc_D; Boolean),
    organism swimming speed (u), and run duration (tau).
    Returns: Encounter rate kernel for random walk predator. '''

    if calc_D:
        D = calculate_diffusivity_rw(u)
    B_rw = 4*pi*D*r
    return B_rw

from sympy import *

class Kernel():
    def __init__(self,sym):
        '''
        To establish the class, input the variable representations you'll use to
        define the kernel.
        '''
        Example: K = Kernel(sym='x,y,z')
        self.sym = symbols(sym)

    def set_kernel(self,expression):
        '''
        Add the symbolic equation for the kernel. Should be plain format.
        Example: Kernel.set_kernel(x+y)
        '''
        self.expression = expression

    def eval_kernel(self,vals):
        '''
        Evaluate the kernel for a specific parameter set.
        Input: a list of tuples with format (symbol, value)
        Example: K.eval_kernel(vals=[(x,1),(y,1),(z,1)])
        Returns: Kernel value
        '''
        return self.expression.subs(vals)
