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

### Configuring the TensorFlow

#### Download the images



### Starting the TensorFlow Project




#### Visualizing the graph with TensorBoard

```
python tensorflow/tensorboard/tensorboard.py --logdir=./log
```

### Documentation

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

#### dealing with disparate methodologies (DX/TS)

In the TS images, the average fragmented DNA will be slightly higher,
across the board.  In the DX images, the average fragmented DNA should
be much lower, especially in samples where fragmented DNA is not a
problem.  That is, the skew of fragmented DNA in DX images will tend
to be more normal.  And FGA will usually only be higher in images that
actually have FGA problems.

Therefore, 


#### processing neural network to score

all operations, such as scaling, filtering and segmenting,
need to be capable of running in a single pipeline to score

#### macro features?



## Useful Techniques


- use histogram and identify the background to normalize the data



- Sholl analysis?
- Breast Cancer paper used 3 categories of feature sets: Morphology,
  Intensity, Texture)
- Also used RGB => YUV Color Detection to ID nuclei with H&E stain
- morphology (erosion on filtered images to ID circles?)
- transform to HSV (YUV) color space and filter
- chop images into smaller images in order to train faster
- how to create & persist maps that denote transformations applied to
  source images
- how to filter out erroneous shapes (dark blobs & streaks)

#### SIFT

- Scale Invariant Feature Transform
- no GPU implementation in OpenCV

#### SURF

- similar to sift, mostly as accurate, but different implementation.
- available in OpenCV
- GPU implementation available in OpenCV

#### FRST

useful for detecting circular objects

[Automatic Nuclei Segmentation (Breast Cancer)](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0070221)

FRST was used in this study. Notes:

Figure 3. Marker imposition and watershed segmentation for nuclei
segmentation.  Prior to applying the FRST the image is preprocessed
with color unmixing and morphological operations (n = 10). The set of
radii for the FRST is R = (10, 11,…,20). Note: the markers and
watershed ridges (given in green in the figure) were dilated by one
pixel for better visualization. A) Original image. B) Hematoxylin
channel. C) Pre-processed image (hematoxylin channel processed with
series of morphological operations). D) Fast radial symmetry transform
(FRST). E) FRST foreground and background markers. F) Watershed
segmentation with FRST markers. G) Regional minima foreground and
background markers. H) Watershed segmentation with regional minima
markers.

#### SPP - Spatial Pyramid Pooling

useful for building neural networks with variously sized images as
input.  the input scale problem first becomes an issue at the fully
connected layers and is not a problem at the convolutional layers

#### Gabor Filters

- useful for edge detection


## Notes

### High FGA Samples

#### 33088 = 0.72

large growths visible in both TS/DX images. higher density of cell
nuclei and altered nuclei distribution is visible in both.

#### 21157 = 0.66

regions of altered growth rates are visible in both images.  the
nuclei of apparently cancerous cells seem much larger than other
nuclei in both samples, but especially in the TS frozen sample.

#### 47756 = 0.36

this the nuclei in DS look to vary considerably in blue color.
the TS image looks like the sample was stretched.

#### 10549 = 0.58

#### 30333 = 0.54

#### 73674 = 0.45

#### 81026 = 0.41

#### 30003 = 0.4

#### 77274 = 0.39

#### 35897 = 0.36

#### 47756 = 0.36

#### 59688 = 0.34

#### 30192 = 0.33

### Low FGA Samples

#### 73797 = 0.06

DX sample is almost clear.  no pink staining, as in TS image.  Yet,
all the nuclei in both images seem to be enlarged.  you can still see
the various high-growth regions in TS.

this one (and the lighter images) look like there's not enough of the
pink stain being used or something.  because there's almost no pink in
the image at all.

#### 75999 = 0.05

the H&E staining doesn't look consistent in the TS images, the nuclei
are barely visible. almost like not enough H&E was used. though there
was plenty of the pink stain.  The DS image contains lots of
outgrowths with spaces in the middle

### Prostate Cancer

[image identifying tumor cells and tumor stroma](http://www.proteinatlas.org/images_dictionary/prostate_cancer__3__gleason_8__overview.jpg)

[Stroma is connective tissue](https://en.wikipedia.org/wiki/Stromal_cell)
and can be involved in cancer, particularly skin cancer.

[normal prostate cells w/ gland identification](http://www.proteinatlas.org/learn/dictionary/normal/prostate)

### Gleason Grading System

used to evaluate prognosis for prostate cancer patients.

**Carcinoma differentiation** - refers to how fast a sample of cancer
  tissue would appear to grow

**anaplasia** - cells lost the morpholgoical characteristics of mature
  cells.  anaplastic nuclei are variable and bizarre in size and
  shape.  the chromatin is coarse and clumped.  nuclei can be massive. 
  
anaplasia should translate into enlarged nuclei with respect to the
average and they should have greater color variation from h&e stain,
due to chromatin clumping

A pathologist microscopically examines the biopsy specimen for certain
"Gleason" patterns. These Gleason patterns are associated with the
following features:

#### Pattern 1

The cancerous prostate closely resembles normal prostate tissue. The
glands are small, well-formed, and closely packed. This corresponds to
a well differentiated carcinoma.

#### Pattern 2

The tissue still has well-formed glands, but they are larger and have
more tissue between them, implying that the stroma has increased. This
also corresponds to a moderately differentiated carcinoma.

#### Pattern 3

The tissue still has recognizable glands, but the cells are darker. At
high magnification, some of these cells have left the glands and are
beginning to invade the surrounding tissue or having an infiltrative
pattern. This corresponds to a moderately differentiated carcinoma.

#### Pattern 4

The tissue has few recognizable glands. Many cells are invading the
surrounding tissue in neoplastic clumps. This corresponds to a poorly
differentiated carcinoma.

#### Pattern 5

The tissue does not have any or only a few recognizable glands. There
are often just sheets of cells throughout the surrounding tissue. This
corresponds to an anaplastic carcinoma.  In the present form of the
Gleason system, prostate cancer of Gleason patterns 1 and 2 are rarely
seen. Gleason pattern 3 is by far the most common.

### Damage to Freezing on DNA

TS samples are where FGA numbers came from.

#### observations in differences b/w TS & DX images

- looks like there are lots of spaces in the frozen TS images. probably
  places where the cell membrane broke and larger ice crystals formed.
- it also looks like the cells & cell nuclei are generally much closer together
  in high-growth regions in the cancer cells with higher FGA

#### questions

- how are TS samples frozen and stored?
- are TS samples unthawed before micrograph?
- how consistent is the methodology here?
- is oxidative stress more likely to happen in flash frozen samples?
- does oxidative stress cause increase in double strand breaks?  YES
- how prevalent is this oxidative stress in TS samples?

#### Ice Crystals

- ice crystal are formed that can cause cell membrane rupture
- rapid freezing results in ice crystal formation in the outer parts of cells (nucleus?)
- slow cooling allows water to leach out, reducing ice crystal formation
  - however, it leads to cell rupture due to an imbalance in osmotic pressure

#### Freeze Concentrantion

- Ice crystals can cause the salts/proteins to become concentrated
- this impacts the stability of proteins and denatures/conglomerates them
- causes unfolding at ice

#### Oxidative Stress

- it's suggested that ice crystal induced damage to organelle
  structures leads to activation of rescue systems associated with
  energy generation
- this results in subsequence increase in oxidative stress and
  production of ROS (free radicals produced as by-products of REDOX
  reactions)
- oxidative stress results in molecular damage to DNA, proteins and
  lipids in the cell. this happens when the balance b/w ROS and
  antioxidants is lost.
- some studies have shown that 

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

- instead of relying solely on the FGA% for the training set,
  - can i assess features in the image and attach my confidence to that number for each set?

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




