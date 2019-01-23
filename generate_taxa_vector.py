# -*- coding: utf-8 -*-
"""
A script to parse multiple taxonomy tables in / format and return a vector
representing all unique entries. This vector can then be used in ML as the
response variable.
"""

import numpy as np
import pandas as pd
import os

def generate_taxa_vector(dir=os.getcwd(),ftype):
    os.chdir(dir)
    #read in using pandas
    #select column of taxa depending on ftype
    #concatenate column and then return vector with unique values
    
