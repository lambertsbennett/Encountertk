# Optics-tk
*under active development

1) Python module to parse and analyse earth sciences optical data
2) Data cleaning and formatting for input into ML packages

Emphasis has been placed on instruments that were used in the TARA Oceans expedition, popular optical scattering measurements, analysis of Underwater Vision Profiler data, and on implementing algorithms that derive additional information from satellite data products. 

Neato use cases:

(1) Calculate encounter rates for a bacterium in a particle landscape described by a given PSD.

usage:```[E,T,mean_vol,mean_surf] = encounter_from_PSD(N0,beta,rmin,rmax,r0)```

This gives you the total encounter rate E, average time to encounter T, mean volume of a particle encountered mean_vol, and the mean surface area of a particle encountered mean_surf.

It's important to note that each of these values depends on the size range of particles that you consider and that the encounter rate model only applies when the particle size >> bacterium size.

(2) Trying to predict community composition from optical data
For now it's important that all the file types in the directory are of the same type. Maybe one day we can extend it to multiple file types.

First create a response vector which includes all microbial taxa in your dataset.
usage: ```resp_vec = generate_taxa_vector(dir, ftype)```

Then for each station or observation populate the same vector.
usage: ```obs_vec = pop_obs_vecs(dir,resp_vec)```

Create input tensor of optical data from optics object.
usage: ```in_tensor = optics_tensor(optics_df)```

Next use Keras to train a NN.
usage: ...

If you're keen on collaborating or would really like to see something implemented, please drop me a line! (lambertb@uw.edu)
