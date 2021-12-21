'''
Emulators for fast modelling of power spectra in various dark matter scenarios.

You can also get documentation for all routines directory from
the interpreter using Python's built-in help() function.
For example:
>>> import DMemu
>>> help(DMemu.use_emul)
'''

import sys
from .functions import *


#Suppress warnings from zero-divisions and nans
import numpy
numpy.seterr(all='ignore')
