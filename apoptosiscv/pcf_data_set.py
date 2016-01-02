import apoptosiscv
import os.path
import csv
import png

def config_paths(path):
    return {'home': path,
            'data': os.path.join(path, 'data'),
            'tf': os.path.join(path, 'tfdata'),
            'dx': os.path.join(path, 'img/dx'),
            'ts': os.path.join(path, 'img/ts')}

def read_training_samples(csvname):
    samples = [] # { 'id', 'fga' }
    with open(csvname, 'r') as f:
        csvrdr = csv.reader(f)
        for row in csvrdr:
            samples.append({'id': row[0], 'fga': row[1]})
    return samples

def parse_sample_id(filename):
    return filename.split('-')[0]

def parse_png_metadata(filename):
    with open(filename, 'r') as pngfile:
        with png.Reader(filename) as pngrdr:
            pngrdr.preamble()
            return {
                'height': pngrdr.height,
                'width': pngrdr.width,
                'bitdepth': 2,
                'color_type': pngrdr.colortype}

#PNG Colour Channels
# 0 - L - greyscale
# 2 - RGB - color
# 4 - LA - greyscale with alpha
# 6 - RGBA - color with alpha

def read_image_metadata(imgtype, path):
    samples = []
    files = filter(lambda f: os.path.isfile(os.path.join(path, f)), os.listdir(path))
    png_images = [f for f in files if f.endswith('png')]

    return map(lambda pngimg: ({
        'id': parse_sample_id(pngimg),
        'file': pngimg,
        'path': os.path.join(path, pngimg)
        #} + parse_png_metadata(os.path.join(path, pngimg))), png_images)
        }), png_images)





def write_test_sample_csv(samples, filepath):
    with open(filepath, 'rw') as csvfile:
        csvwriter = csv.writer(csvfile)

#TODO: function to read training-orig.csv
# - and produce test-samples.csv and training-samples.csv

