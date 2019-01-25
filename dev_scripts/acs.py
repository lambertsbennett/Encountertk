#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For the ACS
"""
import pandas as pd
import numpy as np
import os

class acs:
"""
data_path specifies the path to the acs .dat file

dark refers to the dark readings that should be carried out for calibration purposes
"""

    def __init__(self):
        self.data = data
        self.dark = dark
    
    def read_data(self,data_path):
        self.data=pd.read_csv(data_path)
        #need to structure this specifically for the acs .dat file
    
    def set_dark(self,dark):
        #read the entire file and then return the average dark reading for each channel
        dark_reading = pd.read_csv(dark_path)
        self.dark = np.mean(dark_reading)
        #need to structure this specifically for the acs .dat file

        