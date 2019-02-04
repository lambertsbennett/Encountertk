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
    The scaling factors (sc_f) are provided by the manufacturer and should be modified for your
    specific instrument.

    data_path specifies the path to the bb9 .dat file

    dark_path refers to the dark readings that should be carried out for calibration purposes
    """    
    
    def __init__(self,data=0,dark=0,sc_f=np.array([4.533e-5,1.99e-5,1.946e-5,1.615e-5,1.682e-5,1.047e-5,9.738e-6,8.375e-6,6.404e-6])
):  #These scaling factors do not apply to your instrument!
        self.data = data
        self.dark = dark
        self.sc_f = sc_f
        
    def read_data(self,data_path):
        self.data=pd.read_csv(data_path,sep='\t',header=None)
    
    def set_dark(self,dark_path,dark_reading = np.zeros(9)):
        dark_reading = pd.read_csv(dark_path) #I will update this to read only the necessary columns
        self.dark = np.mean(dark_reading, axis=0)


#b=bb9()
#b.read_data(data_path='/Users/ben/Documents/Optics-tk/example_data/bb9_example_file')
