from pytest import mark
from encountertk._utils import *
from numpy import isnan

@mark.utils
class TestUtils:

    def test_particle_diffusivity(self):
        pass

    def test_rw_diffusivity(self):
        pass

    def test_calculate_re(self):
        pass

    def test_calculate_pe(self):
        pass

    def test_sh_lessthan(self):
        pass

    def test_sh_greaterthan(self):
        pass

    def test_sh_undefined_highpe(self):
        res = calculate_Sh(Re=1,Pe=100000,D=1,v=1)
        assert isnan(res)

    def test_sh_undefined_lowpe(self):
        res = calculate_Sh(Re=1,Pe=10,D=1,v=1)
        assert isnan(res)
