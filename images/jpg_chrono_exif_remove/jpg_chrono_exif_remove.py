import sys
import os
import piexif
from PIL import Image

def info_extract(filename, in_path):
	
	# load image EXIF data
	
	exif_dict = piexif.load(in_path + filename)
	
	# Check orientation and DateTime EXIF data present
	
	if piexif.ImageIFD.Orientation in exif_dict["0th"]:
		orientation = exif_dict["0th"][piexif.ImageIFD.Orientation]
	else:
		orientation = None	
	if piexif.ExifIFD.DateTimeOriginal in exif_dict["Exif"]:
		date_time = exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal]
	else:
		date_time = None
		
	# make list of required EXIF entries and return
	
	img_info = [filename, orientation, date_time.decode("utf-8")]
	return img_info

def jpg_chrono_exif_remove(in_dir = "images", out_dir = "images_cleaned", abs_path = False):
	
	# Set paths
	
	if abs_path:
		in_path = in_dir
		out_path = out_dir
	else:
		in_path = os.getcwd() + "/" + in_dir + "/"
		out_path = os.getcwd() + "/" + out_dir + "/"
		
	# Check if output path exists, create if not
	
	try:
		if not os.path.exists(os.path.dirname(out_path)):
			os.makedirs(os.path.dirname(out_path))
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise
			
	# Make list of img_info lists, sort chronologically
	
	info_extracts= []
	for filename in os.listdir(in_path):
		info_extracts.append(info_extract(filename, in_path))
	info_extracts_chrono = sorted(info_extracts, key = lambda i: i[2], reverse = True)
		
	# open image in chrono order, orientate.
	
	count = 1
	for file_to_save in info_extracts_chrono:
		img = Image.open(in_path + file_to_save[0])
		if file_to_save[1] == 2:
			img = img.transpose(Image.FLIP_LEFT_RIGHT)
		elif file_to_save[1] == 3:
			img = img.rotate(180)
		elif file_to_save[1] == 4:
			img = img.rotate(180).transpose(Image.FLIP_LEFT_RIGHT)
		elif file_to_save[1] == 5:
			img = img.rotate(-90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
		elif file_to_save[1] == 6:
			img = img.rotate(-90, expand=True)
		elif file_to_save[1] == 7:
			img = img.rotate(90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
		elif file_to_save[1] == 8:
			img = img.rotate(90, expand=True)
			
		# Save image without EXIF, with max useful quality, no subsampling
		# Save with counted filename, advance count
				
		img.save(out_path + f"{count}.JPG", quality = 95, subsampling = 0)
		count += 1
		
jpg_chrono_exif_remove()

'''
if __name__ == "__main__":
	args = sys.argv
	# args[0] = current file
	# args[1] = function name
	# args[2:] = function args : (*unpacked)
	globals()[args[1]](*args[2:])
''' 
	
