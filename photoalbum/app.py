# imports
import sys
import os
import platform
from flask import Flask, render_template
from flask_frozen import Freezer

# config
if platform.system() == 'Darwin':
	if platform.machine().startswith('iP'):
		use_reloader = False #disable dev server reload, subprocesses not allowed on iOs
	else:
		use_reloader = True
else:
	use_reloader = True

debug = True #can now run with app.run() in dev server mode

#create app
app = Flask(__name__)
app.config.from_object(__name__) # sets config from within this file
freezer = Freezer(app)

@app.route('/')
def index():
	num_imgs = len(os.listdir(os.getcwd() + '/static/images'))
	imgs = [f'{num}' for num in range(1, num_imgs + 1)]
	return render_template('index.html', images = imgs)
	
'''
add freeze generator to generate links here for more structured pages, calling url_for
'''

#make callable with argument condition
if __name__ == '__main__':
	if len(sys.argv) > 1 and sys.argv[1] == 'build':
		freezer.freeze()
	else:
		app.run()
