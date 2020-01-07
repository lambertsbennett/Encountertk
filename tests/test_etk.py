from pytest import mark
from encountertk.e_model import EncounterModel, ps_encounter, mean_vol_encountered

@mark.modelclass
class TestEncounterModel:

    def test_get_kernel(self,EModel):
        self.model = EModel
        assert self.model.get_kernel() == 1

    def test_set_kernel(self,EModel):
        self.model = EModel
        self.model.set_kernel(2.5)
        assert self.model.get_kernel() == 2.5

    def test_calc_encounter_range(self,EModel):
        self.model = EModel
        self.model.pop1c = [1,5,10]
        self.model.pop2c = [2]
        result = self.model.calc_encounter_range()
        assert list(result) == [2,10,20]

    def test_calc_encounter_pairwise(self,EModel):
        self.model = EModel
        self.model.pop1c = [1,5,10]
        self.model.pop2c = [1,2,3]
        result = self.model.calc_encounter_pairwise()
        assert list(result) == [1,10,30]

@mark.particles
def test_ps_encounter():
    res = ps_encounter(rmin,rmax,D,r0,N0,B,v)
    assert True

@mark.particles
def test_mean_vol_encountered():
    res = mean_vol_encountered(rmin=0.1,rmax,D,r0,N0,B,v)
    assert True
