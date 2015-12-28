PCF Image Recognition Project
=============================

The project is in python2, but it runs in a docker container, where
tensorflow is built.  I'm hoping to upgrade to python3, but i don't
know if i have time to update the dockerfile.

### Downloading micrograph images

Downloading images requires PyDrive, which requires python2.  This
is run on the host OS

1. create a Google API application.  follow pydrive directions
1. add the Drive API to the application's services
1. configure the application to provide a client api for a webapp
1. download the `client_secrets.json` file and add it to project directory
1. now the `python -im img_download` should auth with a web browser
1. download images listed in the CSV

Run `python -im img_download` to load the `img_download` module.
Then run `download_image_set(CSV_TS, IMG_TS_PATH)` to begin downloading.

### Problems

#### visualizing layers of network

#### dealing with very large images

- scale images down where possible (images used for segmentation)

#### dealing with images of various sizes?

store data for each segmented image:
- retaining info about transition

#### how to convert to yuv color space?

opencv functions?
- needs to be fast?
- honestly yuv color space can be applied more than once
  - prior to segmentation and centroid identification, but before

#### how to accurately resample images for segmentation?

basically, which algorithm to use?
- i'm pretty sure nearest neighbor is the best to use
  - when scaling image down in size, to some small degree

#### dealing with erroneous data

- some of the images have very large features that are clearly errors
  - for example, large purple streaks that are not features of the cells

#### adjacent & overlapping nuclei

this is where handcrafted features come in handy, i think

if these cases aren't dealt with, it will significantly distort the
results of some layers

#### Determining fragmented DNA

i think the blue color of the DNA has something to do with this.
darker blue == more fragmented/damaged DNA.  it may not be a
strong correlation though

#### dealing with disparate methodologies


#### processing neural network to score

all operations, such as scaling, filtering and segmenting,
need to be capable of running in a single pipeline to score

#### macro features?


## Resources

### Papers

[Efficient Graph-Based Image Segmentation](https://www.cs.cornell.edu/~dph/papers/seg-ijcv.pdf)

### Videos

[RPI Digital Image Processing Playlist (2015)](https://www.youtube.com/watch?v=UhDlL-tLT2U&list=PLuh62Q4Sv7BUf60vkjePfcOQc8sHxmnDX)
[Morphological Image Processing](https://www.youtube.com/watch?v=IcBzsP-fvPo)
[EGGN 510 (from School of Evil)](https://www.youtube.com/watch?v=rbY-JRQEDUU&list=PLyED3W677ALNv8Htn0f9Xh-AHe1aZPftv)

### Resources

[OpenCV Sitching Pipeline](http://docs.opencv.org/2.4/modules/stitching/doc/introduction.html)

### Notes from OSX

TensorFlow Learn
================

I'm planning on exploring machine learning and image recognition in this
repo.  Some of these projects are just tutorials that I'm walking
through and others will be exploratory projects.

[Great list of ML links & papers](https://github.com/robertsdionne/neural-network-papers)
[TensorFlow tuts converted to Jupyter Notebooks](http://nbviewer.ipython.org/github/MarkDaoust/tensorflow/blob/notebooks/tensorflow/g3doc/tutorials/index.ipynb)
[Install CUDA on Docker for GPU access](https://stackoverflow.com/questions/25185405/using-gpu-from-a-docker-container)

ImageNet Competition
[Google's 2014 ImageNet Challenge](http://deeplearning.net/2014/09/19/googles-entry-to-imagenet-2014-challenge/)
[AlexNet implementation with Theano](https://github.com/uoguelph-mlrg/theano_alexnet)


[Mitosis Detection in Breast Cancer Cells using DNN (2013)](http://www.ncbi.nlm.nih.gov/pubmed/24579167)
[Assessment of algorithms for mitosis detection in breast cancer histopathology images.](http://www.ncbi.nlm.nih.gov/pubmed/25547073)
[Deep convolutional neural networks for annotating gene expression patterns in the mouse brain](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4432953/)

[Biological Imaging Software Tools (paper)](Biological Imaging Software Tools)
[Kitware (ITK/VTK)](http://www.kitware.com/opensource/opensource.html)
[ITK Applications](http://www.itk.org/ITK/resources/applications.html)

[Cell Profiler (imageJ - cell image analysis software)](http://www.cellprofiler.org/)
[Predicting DNA Fragmentation (kinda related)](http://www.pnas.org/content/108/51/20796.abstract)
[Size invariant circle detection - Circle Hough Transform](http://www.sciencedirect.com/science/article/pii/S0262885698001607)

### PCF TODO

todo:
- set up graphs for different parts of my image processing pipeline
- learn how to adjust image size for average size of nucleus
  - need to pre-train nucleus features before even resizing .. ugh chickenz & eggz
  - images are at various zoom levels
  - or my nucleus-identifying features can be size invariant. which likely requires lots more processing

math ideas i’ve thought of independently:
- convolution networks
- various methods of feature composition
  - feature deconstruction/reconstruction
- 2d gaussian filters (though i didn’t know to call them filters)
  - these are
- image differencing….?? maybe not
  - i thought this would highlight edges, but in a different way i believe

useful techniques:
- chop images into smaller images in order to train faster
- how to create & persist maps that denote transformations applied to source images
- use histogram and identify the background to normalize the data
- how to filter out erroneous shapes (dark blobs & streaks)

SIFT (scale invariant feature transform)
- OpenCV http://docs.opencv.org/master/da/df5/tutorial_py_sift_intro.html#gsc.tab=0
- how to add op types for tensorflow?
- find *.pb files for inception net and other network graphs

- process images with color filter.
  - then use spatial filter with threshold to highlight purple objects
  - identify circular purple objects and mark centroids
    - identify average circle size and set parameters for image
  - morphology may be useful when considering conjoined nuclei
- the segment the area around centroids in images
  - measure color variance, distribution, morphology, etc

- but what about other features of the cells?  can they predict fragmentation?
  - or are should features be ignored because they are not causitive?

good questions:
- how would a biological neural network do Fourier Transform?
- how do the DX and TS images vary?


## Digital Image Processing notes

mostly notes i'm taking on lectures from [RPI's Digital Image
Processing](https://www.youtube.com/playlist?list=PLuh62Q4Sv7BUf60vkjePfcOQc8sHxmnDX)
class.

just want to notate some techniques and topics i may want to revisit for my project.
really needed to know this stuff a week ago.  now i'm backed up on lectures to watch AND
have to write a bunch of code in python, which i've never really used before.



part 4 - histograms and point operations (filters)

- using histograms to identify common pixels
- contrast filters

part 5 - geometric operations:

- affine transformation
- projection transformation
- bilinear interpolation
- bicubic interpolation

part 6 - spatial filters
- gaussian spatial filters
- averaging out inputs to spatial filter matrix with scalar divisor
- using spatial filters to filter out certain colors by using color thresholds
  - and by reorienting the image to another color system or with a metric tensor in color space
- image differencing
- sharpening filters
  - (1D filter) [-1 1] => approximates df/dx
  - (1D filter) [-1 2 -1] => approximates d2f/dx2
- the 2D version: find edges in both X and Y directions
  - to do this, we use an approximation of the laplacian:  [[0 -1 0] [-1 4 -1] [0 -1 0]]
  - and this approximates the 2nd derivative (in 2 dimensions?)
    - [[0 -1 0] [-1 5 -1] [0 -1 0] retains the original image, but highlights edges
- so laplacian will help identify edges (& thus shapes), but we’ve only demonstrated this for greyscale
  - how to do this for various colors?  RGB?
  - and what about the laplacian, but invariant for the color.
    - so it’s more than just RGB/CMY
    - but moreso relevant to the local color space
- sobul horizontal edge detector: [[-1 -2 -1] [0 0 0] [1 2 1]]
- sobul vertical edge detector: [[-1 0 1] [-2 0 2] [-1 0 1]]
  - trig to rotate edge detectors?
  - i don’t think it really matters which side is positive/negative, though it likely makes a difference
- median filtering: result of J(x,y) is adjusted to aggregate result of M(x,y, 3, 3) for { 3x3 neighborhood around x,y }
  - median filtering is useful for clearing up particular kinds of noise




