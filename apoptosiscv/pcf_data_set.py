import apoptosiscv
import os.path
import csv

def config_paths(path):
    return {'home': path,
            'data': os.path.join(path, 'data'),
            'tf': os.path.join(path, 'tfdata'),
            'dx': os.path.join(path, 'img/dx'),
            'ts': os.path.join(path, 'img/ts')}

# this_module.HOMEDIR = os.path.dirname(__file__)

# HOMEDIR = os.path.dirname(__file__)
# DATADIR =  os.path.join(HOMEDIR, 'data')
# TFDATA = os.path.join(HOMEDIR, 'tfdata')
# DXPATH = os.path.join('img/dx')
# TSPATH = os.path.join('img/ts')

def read_training_samples(csvname):
    samples = [] # { 'id', 'fga' }
    with open(csvname, 'r') as f:
        csvrdr = csv.reader(f)
        for row in csvrdr:
            samples.append({'id': row[0], 'fga': row[1]})
    return samples


