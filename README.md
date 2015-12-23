PCF Image Recognition Project
=============================

The project is in python2, but it runs in a docker container, where
tensorflow is built.  I'm hoping to upgrade to python3, but i don't
know if i have time to update the dockerfile.

### Downloading images

Downloading images requires PyDrive, which requires python2.  This
is run on the host OS

1. create a Google API application.  follow pydrive directions
1. add the Drive API to the application's services
1. configure the application to provide a client api for a webapp
1. download the `client_secrets.json` file and add it to project directory
1. now the `python ./img_download.py` should auth with a web browser
1. download images listed in the CSV


