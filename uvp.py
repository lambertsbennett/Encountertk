#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For the Underwater Vision Profiler
"""
import pandas as pd
import numpy as np
import os
from scipy import optimize

class uvp:
"""
This class at the moment primarily deals with reading TARA Oceans data, calculating PSD parameters,
plotting results, and calculating encounter rates
"""
    
    def __init__(self):
        self.data = data
        self.dark = dark
        self.N0 = N0
        self.beta = beta
    
    def read_data(self,data_path):
        self.data=pd.read_csv(data_path)
        #need to structure this for the TARA data
    
    def fit_psd(self, size_bins, min_points=4, fill_vals='na', r_lim = 0.6):
        """
        This function deals with fitting a power law to each uvp measurement.
        From this the slope and coefficient of the PSD are determined (N0 and beta)
        size_bins correspond to the radius range of each particle bin
        min_points is the lower limit on how few non-zero bins the function will fit a curve to
        fill_vals is what is placed in the output when too few points exist or the fit is exceedingly poor
        r_lim is the r^2 value under which the curve fits are rejected.
        """
        #This is modified from the scipy cookbook
        logx = np.log10(xdata)
        logy = np.log10(ydata)
        logyerr = yerr / ydata

        # define our (line) fitting function
        fitfunc = lambda p, x: p[0] + p[1] * x
        errfunc = lambda p, x, y, err: (y - fitfunc(p, x)) / err

        pinit = [1.0, -1.0]
        out = optimize.leastsq(errfunc, pinit, args=(logx, logy, logyerr), full_output=1)
        pfinal = out[0]
        covar = out[1]
        
    
    
    
    #Leave unimplemented for the moment, but could be developed further for raw measurements
    def set_dark(self,dark):
        #read the entire file and then return the average dark reading for each channel
        dark_reading = pd.read_csv(dark_path)
        self.dark = np.mean(dark_reading)


        