'''
Helper functions to determine parameters for encounter rate models
'''
from numpy import pi,nan


def calculate_diffusivity_particle(r, T = 298.15, eta = 10e-2):
    ''' Calculate diffusivity of non-motile particle.
    Requires: Temperature (T; in K), particle radius (r; in cm),
    dynamic viscosity of water (eta; in g cm^-1 s^-1).
    Returns: diffusivity in cm^2 s^-1 '''
    
    K = 1.38e-16 # Boltzmann's constant
    Dnm = K*T / (6*pi*eta*r)
    return Dnm



def calculate_diffusivity_rw(v_mean, tau = 1, alpha = 0, n =3):
    ''' Calculate the diffusivity of an organism performing a random walk.
    Requires: the mean swimming velocity (v_mean), mean run duration (tau),
    the average cosine of angle between successive runs (alpha),
    and the dimensionality of the problem (n; default 3D). 
    Returns: diffusivity of organism in units L^2/t '''
    
    Drw = (v_mean**2) * tau / (n * (1-alpha))
    return Drw


def calculate_Re(u,r,v):
    ''' Calculate the Reynolds number.
    Requires: characteristic length scale (r), characteristic velocity (u), 
    and the kinematic viscosity of the fluid (v; approx. 10e-2 cm^2 s^-1).
    Returns: Reynolds number (dimensionless) '''
    
    Re = u*r/v
    return Re

def calculate_Pe(u,r,D):
    ''' Calculate the Peclet number.
    Requires: characteristic velocity (u), characteristic length scale (r),
    Diffusivity of solute (D).
    Returns: Peclet number (dimensionless) '''
    
    Pe = u * a / D
    return Pe

def calculate_Sh(Re,Pe,D,v):
    ''' Calculate the Sherwood number using empirical relationships if possible.
    Requires: Reynolds number (Re), Peclet number (Pe), Solute diffusivity (D),
    and kinematic viscosity (v).
    Returns: Sherwood number (if defined; dimensionless) '''
    
    if Re < 0.1:
        Sh = 0.5*(1+(1+2*Pe)**(1/3))
        return Sh
    elif Re > 0.1 and Pe > 30 and Pe < 50000:
        Sh = 1 + 0.619*(Re**0.412)*(v/D)**(1/3)
        return Sh
    else:
        print ('Sh is undefined for these hydrodynamic conditions in this package')
        return nan

def calculate_stokes_velocity(rho_p, r, eta, rho_f = 1030, g = 9.81):
    ''' Calculate settling velocity of particle with radius r.
    Requires: Density of fluid (rho_f), Density of particle (rho_p),
    acceleration due to gravity (g), particle radius (r), dynamic viscosity (eta; kg m^-1 s^-1).
    Returns: sinking velocity (m/s) '''
    
    print ('Be aware length-scales should be in m')
    v_s = (2/9)*((rho_p-rho_f)/eta)*(r**2)
    return v_s
