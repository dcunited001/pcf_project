import os.path
from apoptosiscv.pcf_data_set import *

paths = config_paths(os.getcwd())
data = separate_test_and_training_data(paths)
