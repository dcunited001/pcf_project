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

def read_training_examples_orig(csvname):
    examples = [] # { 'id', 'fga' }
    with open(csvname, 'r') as f:
        csvrdr = csv.reader(f)
        for row in csvrdr:
            examples.append({'id': row[0], 'fga': row[1]})
    return examples

def parse_example_id(filename):
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

def read_example_ids(path):
    """
    Reads a list of id's from either the DX or TS image dir
    """
    example_ids = []
    files = filter(lambda f: os.path.isfile(os.path.join(path, f)), os.listdir(path))
    example_pngs = [f for f in files if f.endswith('png')]
    return map(lambda pngimg: parse_example_id(pngimg), example_pngs)

def filter_test_example_ids(example_ids, training_ids):
    return filter(lambda x: x not in training_ids, example_ids)

#PNG Colour Channels
# 0 - L - greyscale
# 2 - RGB - color
# 4 - LA - greyscale with alpha
# 6 - RGBA - color with alpha

def read_image_metadata(imgtype, path):
    examples = []
    files = filter(lambda f: os.path.isfile(os.path.join(path, f)), os.listdir(path))
    png_images = [f for f in files if f.endswith('png')]

    return map(lambda pngimg: ({
        'id': parse_example_id(pngimg),
        'file': pngimg,
        'path': os.path.join(path, pngimg)
        #} + parse_png_metadata(os.path.join(path, pngimg))), png_images)
        }), png_images)

def write_examples_to_csv(examples, filepath):
    """Writes a list of examples and associated image metadata into a
    CSV that can be more easily read in.
    :param examples: examples (either test or training)
    """
    with open(filepath, 'rw') as csvfile:
        csvwriter = csv.writer(csvfile)

#TODO: function to read training-orig.csv
# - and produce test-examples.csv and training-examples.csv

def separate_test_and_training_data(paths, orig_csv_file = 'training.csv'):
    """Reads in the original training.csv, then reads in image metadata for DX and TS
    and writes test.csv and training.csv"""
    orig_training_examples = read_training_examples_orig(os.path.join(paths['data'], 'training.csv'))
    all_example_ids = read_example_ids(paths['dx'])
    training_ids = map(lambda x: x['id'], orig_training_examples)
    test_ids = filter_test_example_ids(all_example_ids, training_ids)
    print(len(training_ids))
    print(len(test_ids))


