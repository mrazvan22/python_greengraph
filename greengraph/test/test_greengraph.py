from nose.tools import assert_equals, assert_almost_equal
import numpy as np
from ..geolocation import *
from ..url import map_at
from ..green_analysis import *
from ..points import *
from ..visualise import *

def test_geolocate_1():
  london_location = np.array(geolocate("London"))

  assert_almost_equal(sum(london_location - np.array([51.5073509, -0.1277583])), 0.0)




