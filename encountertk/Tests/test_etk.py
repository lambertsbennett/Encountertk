from pytest import mark
from encountertk.e_model import EncounterModel, ps_encounter, mean_vol_encountered



@mark.modelclass
class TestEncounterModel:

    def test_get_kernel(self):
        self.model = EncounterModel(kernel=1,pop2c=[1],pop1c=[1])
        assert self.model.get_kernel() == 1

    def test_set_kernel(self):
        self.model = EncounterModel(kernel=1,pop2c=[1],pop1c=[1])
        self.model.set_kernel(2.5)
        assert self.model.get_kernel() == 2.5

    def test_calc_encounter_range(self):
        assert True

    def test_calc_encounter_pairwise(self):
        assert True

@mark.particles
def test_ps_encounter():
    assert True

@mark.particles
def test_mean_vol_encountered():
    assert True
