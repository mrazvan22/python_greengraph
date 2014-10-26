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

def test_is_green_1():
  assert(is_green(0,1,0))

def test_linespace():
  start = np.array((0,0))
  end = np.array((4,4))
  steps = 3
  points = np.array(location_sequence(start, end, steps))

  diff = points - np.array([(0,0), (2,2), (4,4)])

  assert(np.count_nonzero(diff) == 0)




