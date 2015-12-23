#!/usr/bin/python3
from pydrive.drive import GoogleDrive as gdrive
import csv

def read_from_csv(filename):
    rows = []
    csvrdr = csv.reader(filename)
    for row in csvrdr:
        rows.append(row)
    rows

# load data from csv
CSV_DX = './img-dx.csv'
CSV_TS = './img-ts.csv'

img_dx = read_from_csv(CSV_DX)
img_ts = read_from_csv(CSV_TS)

print(img_dx)
