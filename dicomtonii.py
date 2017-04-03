#!/usr/bin/env python
from time import time
import argparse
import glob
import shutil
import os
import string
import random
import subprocess



def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


def converter(input_dicom,input_zip=[],output='output'):
	# Create temporary directories
	cwd = os.getcwd()
	print 'Current directory'
	print cwd
	# Grunt will unzip the files in a folder named input_dicom
	# have to find the folder that contains the dicoms
	# Get all the data based on the search key-- these data consist of the nifti file and a zip version of the original nifti
	curdir,folderdicomfiles=os.walk(cwd+'/input_dicom/').next()
	command='plastimatch convert --input %s --output-img %s'%(cwd+'/input_dicom/'+folderdicomfiles[0],cwd)
	print 'Running'
	print  command
	subprocess.call(command, shell=True)
	# shutil.make_archive(output, 'zip', outputfolder)
	return 0

def main(argv):
	converter(argv.input_dicom,argv.output)
	return 0

if __name__ == "__main__":
	parser = argparse.ArgumentParser( description='Convert between dicom and nifti files.')
	parser.add_argument ("-i", "--input_dicom",  help="nitifile input" , required=True)
	parser.add_argument ("-o", "--output",  help="nitifile input" , required=False)
	parser.add_argument('--version', action='version', version='%(prog)s 0.1')
	parser.add_argument("-q", "--quiet",
						  action="store_false", dest="verbose",
						  default=True,
						  help="don't print status messages to stdout")
	args = parser.parse_args()
	main(args)
