#! /usr/bin/python 
import sys, os, hashlib
if not (os.path.isfile(os.path.expanduser('~')+'/.reader_rc')):
	file=open(os.path.expanduser('~')+'/.reader_rc','w+b')
else:
	file=open(os.path.expanduser('~')+'/.reader_rc','r+')

if len(sys.argv) <= 2:
	text_location=os.getcwd()+'/'+sys.argv[1]
	text=open(text_location,'r+')
	
	text1=text.readlines()
	md5_hash=hashlib.md5(text.read()).hexdigest()
	if md5_hash not in [s.split(',')[0] for s in file ]:
		i=0
		key=raw_input()
		while(key!='q'):
			for s in text1[i:i+40]:
				print s
			key=raw_input()
			i=i+40
		file.write(md5_hash+str(i))

	else:
		lines_read='0'
		for line in file:
			if md5_hash==line.split(',')[0]:
				lines_read=line.split(',')[1]
		i=int(lines_read)
		key=raw_input()
		while(key!='q'):
			for s in text1[i:i+40]:
				print s
			key=raw_input()
			i=i+40

