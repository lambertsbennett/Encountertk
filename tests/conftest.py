from pytest import fixture
from encountertk.e_model import EncounterModel, ps_encounter, mean_vol_encountered


@fixture(scope='function')
def EModel():
    return EncounterModel(kernel=1,pop2c=[1],pop1c=[1])
