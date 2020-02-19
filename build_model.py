#!/usr/bin/env python

from modeller import *
from modeller.automodel import *

env = environ()
a = automodel(env, alnfile='alignment.ali',
              knowns='2lru', sequence='T0882',
              assess_methods=(assess.DOPE, assess.GA341))
a.starting_model = 1
a.ending_model = 5
a.make()
