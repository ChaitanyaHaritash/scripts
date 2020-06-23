#!/usr/bin/env python

import zipfile,re,sys,os

class b:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

_banner_ = b.HEADER + """ MALDOC URL EXTRACTOR\n By @bofheaded\n =====================""" + b.ENDC

print _banner_

#===========================================================================

def sampleextract(sample):
	print b.OKBLUE + " Extracting to :",os.getcwd()+"/extract/\n" + b.ENDC
	with zipfile.ZipFile(sample, 'r') as zip_ref:
    		zip_ref.extractall("./extract")

def urlregx(string):
	 return " \n ".join(re.findall(r'(https?://[^\s"]+)', string))
def main():
	if (len(sys.argv) != 2):
		print "\n Provide Path to Sample."
		sys.exit()
	else:
		print b.OKBLUE + " Sample: ",sys.argv[1] + b.ENDC
		sampleextract(sys.argv[1])
		root = os.getcwd()+"/extract/"
		for path, subdirs, files in os.walk(root):
    			for name in files:
        			listfile = os.path.join(path, name)
				listfile= listfile.split()
				for i in listfile:
					f = open(i,"r").read()
					print (b.WARNING + " ==>"+str(i) + b.ENDC)+" : \n "+urlregx(f)+"\n"
main()
