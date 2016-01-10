import os.path
from apoptosiscv.pcf_data_set import *

paths = config_paths(os.getcwd())
data = separate_test_and_training_data(paths)

write_examples_to_csv(data['test'], os.path.join(paths['data'], 'test_examples.csv'))
write_examples_to_csv(data['train'], os.path.join(paths['data'], 'train_examples.csv'))
