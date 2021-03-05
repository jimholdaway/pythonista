import sys
import argparse
import os
import piexif
from PIL import Image

def jpg_exif_remove(args):
	
	"""
	Removes EXIF data from directory of jpeg images whilst preserving image orientation and quality.
	
	Parameters
	----------
	
	in_dir: string, directory containing jpgs to have EXIF removed, default 'images'
	out_dir: string, destination directory of cleaned jpgs, default 'images_cleaned'
	abs_path: boolean, if True in_dir and out_dir must be full absolute paths 
	"""
	
	# Set args
	
	in_dir = args.in_dir
	out_dir = args.out_dir
	abs_path = args.abs_path
	
	# Set paths according to arg boolean
	
	if (abs_path == True):
		in_path = in_dir
		out_path = out_dir
	elif (abs_path == False):
		in_path = os.getcwd() + "/" + in_dir + "/"
		out_path = os.getcwd() + "/" + out_dir + "/"
	else:
		print("Option 'abs_path' must be boolean")
		
	# Check if output path exists, create if not
	
	try:
		if not os.path.exists(os.path.dirname(out_path)):
			os.makedirs(os.path.dirname(out_path))
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise
			
	# Loop through files in input path directory
	
	for filename in os.listdir(in_path):
		img = Image.open(in_path + filename)
		
		# Check if image has EXIF data
		
		if "exif" in img.info:
			exif_dict = piexif.load(img.info["exif"])
			
			# Check if EXIF data has orientation entry
			
			if piexif.ImageIFD.Orientation in exif_dict["0th"]:
				orientation = exif_dict["0th"].pop(piexif.ImageIFD.Orientation)
				
				# Rotate according to orientation entry
				
				if orientation == 2:
					img = img.transpose(Image.FLIP_LEFT_RIGHT)
				elif orientation == 3:
					img = img.rotate(180)
				elif orientation == 4:
					img = img.rotate(180).transpose(Image.FLIP_LEFT_RIGHT)
				elif orientation == 5:
					img = img.rotate(-90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
				elif orientation == 6:
					img = img.rotate(-90, expand=True)
				elif orientation == 7:
					img = img.rotate(90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
				elif orientation == 8:
					img = img.rotate(90, expand=True)
			
			# Save image without EXIF, with max useful quality, no subsampling
				
			img.save(out_path + filename, quality = 95, subsampling = 0)
			
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Open JPEGs in a directory, removes EXIF data and saves to another directory. If default arguments are not used, ALL arguments must be set.")
	parser.add_argument("in_dir", nargs='?', type=str, default="images", help="Path to directory of images to have EXIF removed")
	parser.add_argument("out_dir", nargs='?', type=str, default="images_cleaned", help="Path of directory to save EXIF removed images too")
	parser.add_argument("abs_path", nargs='?', type=bool, default=False, help="Set to true is absolute path to be used")
	args = parser.parse_args()
	jpg_exif_remove(args)
	

		
