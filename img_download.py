#!/usr/bin/python3
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import csv
import os.path

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

def check_for_image(filename, path):
    return os.path.isfile(path + filename)

def download_image(gid, filename, path):
    print("downloading: " + filename + " - " + gid)
    drivefile = drive.CreateFile({'id': gid})
    drivefile.GetContentFile(path + filename)

def download_image_set(csv_filename, img_path):
    images = read_from_csv(csv_filename)
    print("csv data loaded")

    for img in images:
        filename = img[0]
        gid = img[1]
        path = img_path

        if not check_for_image(filename, path):
            download_image(gid, filename, path)

# load data from csv
CSV_DX = './img-dx.csv'
CSV_TS = './img-ts.csv'
IMG_DX_PATH= './img/dx/'
IMG_TS_PATH= './img/ts/'

# import as interactive script to download
# import `img_download`
# download_image_set(CSV_TS, IMG_TS_PATH)
