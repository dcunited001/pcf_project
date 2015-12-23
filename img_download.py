#!/usr/bin/python3
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import csv

print("authenticating to google")

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

print("you have been authenticated")

drive = GoogleDrive(gauth)

print("connected to google drive")

def read_from_csv(filename):
    rows = []
    with open(filename, 'r') as f:
        csvrdr = csv.reader(f)
        for row in csvrdr:
            rows.append(row)
    return rows

# load data from csv
CSV_DX = './img-dx.csv'
CSV_TS = './img-ts.csv'

img_dx = read_from_csv(CSV_DX)
img_ts = read_from_csv(CSV_TS)

print("csv data loaded")

print("retrieving metadata")
imgtest = drive.CreateFile({'id': img_ts[0][1]})

print("downloading data")
imgtest.GetContentFile(img_ts[0][0])
