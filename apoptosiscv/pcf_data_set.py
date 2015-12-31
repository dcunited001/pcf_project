import os.path
import csv

def read_training_samples(csvname):
    samples = [] # { 'id', 'fga' }
    with open(csvname, 'r') as f:
        csvrdr = csv.reader(f)
        for row in csvrdr:
            samples.append({'id': row[0], 'fga': row[1]})
    return rows


