#!/bin/python

import os, sys
import shutil

def task():
	path = sys.argv[1]
	print(os.access(path))

#	try:
#		with open(path, 'w') as f:
#       #robić co wymaga zadanie
#        pass
#    except IOError as x:
#    	print 'error ', x.errno, ',', x.strerror
#    	if x.errno == errno.EACCES:
#    		print path, 'no perms'
#    	elif x.errno == errno.EISDIR:
#    		print path, 'is directory'


def task1():
	path = sys.argv[1] 
	list = os.listdir(path)
	for file in list:
		location = os.path.join(path,file)
		if not os.path.isfile(location): continue
		if os.access(location, os.W_OK): 
			os.rename(location, location+'.old')
			

def task2():
	with open(sys.argv[2],'r') as infile:
		path = sys.argv[1]
		for line in infile:
			line = line.replace('\n','')
			location = path + '/' + line
			with open(location,'w+') as new_file:
				new_file.write('no cóż...')
	        	
	    
def task3():
	path = sys.argv[1] 
	list = os.listdir(path)
	for file in list:
		location = os.path.join(path,file)
		if not os.path.isfile(location): continue
		if os.access(location, os.X_OK): 
			os.remove(location)


def task4():
	path = sys.argv[1] 
	list = os.listdir(path)
	file_size = []
	for file in list:
		location = os.path.join(path,file)
		if os.access(location, os.X_OK): 
			size = os.path.getsize(location)
			file_size.append((size, file))

	file_size.sort(key = lambda s: s[0])
	i = 0
	for item in file_size:
		print(item)

	for item in file_size:
		file = item[1]
		location = os.path.join(path,file)
		os.rename(location, location+'.'+str(i))
		i += 1


def task5():
	ext = ''
	if len(sys.argv) > 2:
		ext = "." + sys.argv[2]
	
	outputPath = sys.argv[1]+'/'+'output'+ext
	#outputPath = sys.argv[1]+'/'+'output{}'.format(ext) #/tstdir/output.cos
	with open(outputPath,'a+') as outputFile: #append mode
		for file in os.listdir(sys.argv[1]):
			if file != 'output{}'.format(ext):
				header = '{}\n'.format(file)
				outputFile.write(header)
				readPath = sys.argv[1]+'/'+file
				with open(readPath,'r') as file_:
					outputFile.write(file_.read() + "\n")

def task6():
	with open(sys.argv[2],'r') as infile:
		path = sys.argv[1]
		for line in infile:
			line = line.replace('\n','')
			location = path + '/' + line #location of thisfile
			outputPath = sys.argv[1]+'/'+'o utput'
			with open(outputPath,'a+') as outputFile: #append mode
				if file != 'output':
					header = '{}\n'.format(line)			
					outputFile.write(header)
					with open(location,'r') as file_:
						outputFile.write(file_.read() + "\n")

	
def task7():	
	srcpath = sys.argv[1]
	dstpath = sys.argv[2]
	list = os.listdir(srcpath)
	for file in list:
		srclocation = os.path.join(srcpath,file)
		dstlocation = os.path.join(dstpath,file)
		if os.access(srclocation, os.W_OK): 
			os.rename(srclocation, dstlocation)
			#shutil.move(srcpath+f, dstpath)


def task8():
	path = sys.argv[1]
	level = int(sys.argv[2])
	for root, dir, files in os.walk(path):
		if root[len(path)+1:].count(os.sep)<level:
			for file in files:
				print(os.path.join(root,file)) 


def task1u():
	path = sys.argv[1] 
	list = os.listdir(path)
	for file in list:
		location = os.path.join(path,file)
		if not os.path.isfile(location): continue
		newname = os.path.splitext(location)[0]
       	#newname = location.rsplit('.', 1)[0]
		os.rename(location, newname)


if __name__ == "__main__":
	task5()



#tworzenie plików w katalogu wedl listy w pliku
#numerowanie plików w katalogu do X.perm +nr kolejny, sort by size

#try:
#   fp = open("myfile")
#except PermissionError:
#    return "some default data"
#else:
#    with fp:
#        return fp.read()

