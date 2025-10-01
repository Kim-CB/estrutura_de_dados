import random


from nose.tools import *
import importlib
import ods
from listtest import exercise_list

def test_as():
    exercise_list(ods.ArrayStack())