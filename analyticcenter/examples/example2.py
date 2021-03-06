##
## Copyright (c) 2019
##
## @author: Daniel Bankmann
## @company: Technische Universität Berlin
##
## This file is part of the python package analyticcenter
## (see https://gitlab.tu-berlin.de/PassivityRadius/analyticcenter/)
##
## License: 3-clause BSD, see https://opensource.org/licenses/BSD-3-Clause
##
import numpy as np
import analyticcenter
from os.path import join, dirname
from analyticcenter import WeightedSystem, get_algorithm_object
from analyticcenter import NewtonDirectionMultipleDimensionsCT
from analyticcenter import SteepestAscentDirectionCT
_example_file = resource_filename(__name__, 'example-n-6-m-3.npy')
sysmat = np.load(_example_file, allow_pickle=True)
sys = WeightedSystem(*sysmat)

if __name__=="__main__":
    alg = get_algorithm_object(sys, 'newton', discrete_time=False, save_intermediate=True)
    alg()
