'''
Module to carry out common encounter rate calculations and modeling
'''

class EncounterModel(self):
    ''' Base class for encounter rate model. Requires an encounter rate kernel value. '''
    
    def __init__(self,kernel_value):
        self.kernel = kernel
