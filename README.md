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
