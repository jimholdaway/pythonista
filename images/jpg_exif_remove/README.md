# jpg_exif_remove.py

## Description

Removes EXIF data from directory of jpeg images whilst preserving image orientation and quality.

## Parameters

in_dir: string, directory containing jpgs to have EXIF removed, default 'images'
out_dir: string, destination directory of cleaned jpgs, default 'images_cleaned'
abs_path: boolean, if True in_dir and out_dir must be full absolute paths

## Behaviour

Calling the function will iterate through jpeg files in _in_dir_, rotate image according to EXIF Orientation value and save without EXIF data to _out_dir_. When saving, quality is set to 95 (any higher isn't useful) and subsampling to 0 to preserve image quality.

## Suggested usage

### How I use it

I use this mainly on an IPad. I manage git repos using [Working Copy](https://workingcopyapp.com) and run Python scripts using [Pythonista](http://omz-software.com/pythonista/). The `piexif` module is not in the standard library but is pure python so can be added to Pythonista using `pip install piexif` using [Stash](https://github.com/ywangd/stash).

### On Linux with python

Requires `pip` and `venv`

```sh
git clone https://github.com/jimholdaway/python_scripts.git
cd python-scripts/jpg_exif_remove
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt
python3 jpg_exif_remove.py jpg_exif_remove in_dir out_dir
```

_Note: in_dir and out_dir only needed if different from defaults of images and images_cleaned respectively_


