# Photoalbum

## Flask app to generate webpage of images

This app will render HTML from a directory of images (/static/images) to a development server at [localhost](localhost:5000) or export to a local directory (build/).

### Usage

#### Prepare images

Jpeg images must be name sequentially as 1.JPG, 2.JPG, 3.JPG ..... 

#### Clone repo

`git clone https://github.com/jimholdaway/python_scripts.git`

#### Pythonista with Working Copy on iOS

[Pythonista 3](http://omz-software.com/pythonista/) is a python scripting environment that runs on iOS/iPadOS.
[Working Copy](https://workingcopyapp.com) is a git client for iOS/iPadOS.

Also possible to run git using [iSH](https://ish.app).

Clone the repo using Working Copy and open the folder through Pythonista. To render HTML to development server, simply run the script. To export HTML to the  `build/` directory, enter build under run options.

Haven't tried running from iOS shortcuts app.

#### Linux/Mac

In photoalbum dir

Live dev server `python3 app.py`
Export HTML `python3 app.y build`

#### Windows

Not tested 




