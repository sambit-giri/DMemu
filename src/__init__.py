'''
Emulator is a Python package for constructing emulators.

You can also get documentation for all routines directory from
the interpreter using Python's built-in help() function.
For example:
>>> import BCMemu
>>> help(BCMemu.use_emul)
'''

import sys
from .BaryonEffectsEmulator import *
from . import kpls 
import smt


#Suppress warnings from zero-divisions and nans
import numpy
numpy.seterr(all='ignore')
