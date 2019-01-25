# Optics-tk
1) Python module to parse and analyse earth sciences optical data
2) Data cleaning and formatting for input into ML packages

Emphasis has been placed on instruments that were used in the TARA Oceans expedition, popular optical scattering measurements, analysis of Underwater Vision Profiler data, and on implementing algorithms that derive additional information from satellite data products. 

Neato use cases:

(1) Calculate encounter rates for a bacterium in a particle landscape described by a given PSD.

usage: ````python [E,T,mean_vol,mean_surf] = encounter_from_PSD(N0,beta,rmin,rmax,r0)```

This gives you the total encounter rate E, average time to encounter T, mean volume of a particle encountered mean_vol, and the mean surface area of a particle encountered mean_surf.
