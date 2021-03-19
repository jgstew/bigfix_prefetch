"""test bigfix_prefetch"""

import os.path
import site
import sys

# don't create bytecode for tests because it is cluttery in python2
sys.dont_write_bytecode = True

# https://stackoverflow.com/questions/34846584/whats-the-recommended-way-to-import-unittest-or-unittest2-depending-on-pyth/66616071
# try:
#    import unittest2 as unittest
# except ImportError:
#    import unittest

# add module folder to import paths
site.addsitedir(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
)

# using this method to ensure we are always testing the local code and not a copy installed with pip
#from bigfix_prefetch import *

#from bigfix_prefetch.prefetch_validate import validate_prefetch

# pylint: disable=line-too-long

from test_pip import *
