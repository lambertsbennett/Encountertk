'''
Module to carry out common encounter rate calculations and modeling
'''

import numpy as np

class EncounterModel():
    ''' Base class for encounter rate model.
    Requires: an encounter rate kernel value,
    Cell concentration of population 1 (pop1c) list of concentrations,
    Cell concentration of population 2 (pop2c) list of concentrations.
    Concentrations can be a scalar or list of concentrations '''

    def __init__(self,pop2c,kernel,pop1c=[1]):
        self.kernel = kernel
        self.pop1c = pop1c
        self.pop2c = pop2c

    def calc_encounter(self):
        ''' Calculate the encounter rate between two populations. The concentrations must
        be in list format. The encounter rate is returned as a list of arrays'''
        if len(self.pop1c) == 1:
            assert (self.pop1c[0] != 0), "Requires non-zero concentrations"
        elif len(self.pop2c) == 1:
            assert (self.pop2c[0] != 0), "Requires non-zero concentrations"

        self.e_rate = [self.kernel*np.multiply(self.pop2c,p1) for p1 in self.pop1c]
        return self.e_rate


if __name__ == "__main__":
    print("Here's a toy example with two populations")
    model = EncounterModel(kernel=1,pop1c = [1,5,10],pop2c = [1,5,10])
    e = model.calc_encounter()
