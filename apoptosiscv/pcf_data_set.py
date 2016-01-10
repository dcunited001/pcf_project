#import apoptosiscv
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
    examples = {} # { 'id', 'fga' }
    with open(csvname, 'r') as f:
        csvrdr = csv.reader(f)
        for row in csvrdr:
            example_id = int(row[0])
            examples[example_id] = {'id': example_id, 'fga': float(row[1])}
    return examples

def parse_example_id(filename):
    return int(filename.split('-')[0])

def parse_png_metadata(path, filename):
    filepath = os.path.join(path, filename)
    with open(filepath, 'r') as pngfile:
        pngrdr = png.Reader(filepath)
        pngrdr.preamble()
        png_metadata = {
            'file': filename,
            'filepath': filepath,
            'height': pngrdr.height,
            'width': pngrdr.width,
            'bitdepth': 2,
            'color_type': pngrdr.color_type}
        # pngrdr.close()
        return png_metadata

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

    return dict(map(lambda pngimg: (parse_example_id(pngimg), parse_png_metadata(path, pngimg)), png_images))

def write_examples_to_csv(examples, filepath):
    """Writes a list of examples and associated image metadata into a
    CSV that can be more easily read in.
    :param examples: examples (either test or training)
    """
    headers = ['id', 'fga',
               'dx_height', 'dx_width', 'dx_color_type', 'dx_bitdepth',
               'ts_height', 'ts_width', 'ts_color_type', 'ts_bitdepth']

    with open(filepath, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, lineterminator=os.linesep)
        csvwriter.writerow(headers)
        for k in examples:
            eg = examples[k]
            dx_vals = map(lambda k: eg['dx'][k], ['height', 'width', 'color_type', 'bitdepth'])
            ts_vals = map(lambda k: eg['ts'][k], ['height', 'width', 'color_type', 'bitdepth'])
            fga = eg['fga'] if 'fga' in eg else None
            row = [eg['id'], fga] + dx_vals + ts_vals
            csvwriter.writerow(row)

#TODO: function to read training-orig.csv
# - and produce test-examples.csv and training-examples.csv

def merge_image_metadata(examples, img_key, img_metadata):
    for k in examples:
        examples[k][img_key] = img_metadata[k]
    return examples

def separate_test_and_training_data(paths, orig_csv_file = 'training.csv'):
    """Reads in the original training.csv, then reads in image metadata for DX and TS"""
    training_examples = read_training_examples_orig(os.path.join(paths['data'], 'training.csv'))
    all_example_ids = read_example_ids(paths['dx'])

    # filtering test_ids from training_ids
    training_ids = map(lambda x: training_examples[x]['id'], training_examples)
    test_ids = filter_test_example_ids(all_example_ids, training_ids)

    # reading metadata from pngs (width/height)
    dx_pngs = read_image_metadata('dx', os.path.join(paths['dx']))
    ts_pngs = read_image_metadata('ts', os.path.join(paths['ts']))

    training_examples = merge_image_metadata(training_examples, 'dx', dx_pngs)
    training_examples = merge_image_metadata(training_examples, 'ts', ts_pngs)

    test_examples = dict(map(lambda x: (x, {'id': x}), test_ids))
    test_examples = merge_image_metadata(test_examples, 'dx', dx_pngs)
    test_examples = merge_image_metadata(test_examples, 'ts', ts_pngs)

    print(len(training_examples))
    print(len(test_examples))

    return {'train': training_examples, 'test': test_examples}

    # no multiline lambda's ?1?1 i don't know if i can deal with that
    # training_examples = training_examples.reduce((lambda eg,x: eg[x]['dx'] = dx_pngs[x]:; :eg[x]['ts'] = ts_pngs[x]:; :eg), training_examples)xs
    # print(training_examples['12345'])
    # test_examples = map(lambda x: {id: x}, test_ids)
