#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For the wetlabs BB9
"""
import pandas as pd
import numpy as np
import os

class bb9:
    """
    The scaling factors are provided by the manufacturer and should be modified for your
    specific instrument.

    data_path specifies the path to the bb9 .dat file

    dark refers to the dark readings that should be carried out for calibration purposes
    """

    #scaling_factors=np.array()
    
    def __init__(self,data=0,dark=0):
        self.data = data
        self.dark = dark
    
    def read_data(self,data_path):
        self.data=pd.read_csv(data_path,sep='\t',header=None)
        #need to structure this specifically for the bb9 .dat file
    
    def set_dark(self,dark):
        #read the entire file and then return the average dark reading for each channel
        dark_reading = pd.read_csv(dark_path)
        self.dark = np.mean(dark_reading)
        #need to structure this specifically for the bb9 .dat file


#b=bb9()
#b.read_data(data_path='/Users/ben/Documents/Optics-tk/example_data/bb9_example_file')
