#! /usr/bin/python 
import sys, os, hashlib
if not (os.path.isfile(os.path.expanduser('~')+'/.reader_rc')):
	file=open(os.path.expanduser('~')+'/.reader_rc','w+b')
else:
	file=open(os.path.expanduser('~')+'/.reader_rc','r+')

file_lines=file.readlines()
file.close()



file=open(os.path.expanduser('~')+'/.reader_rc','w+b')
if len(sys.argv) <= 2:
	text_location=os.getcwd()+'/'+sys.argv[1]
	text=open(text_location,'r+')
	
	text1=text.readlines()
	md5_hash=hashlib.md5(text.read()).hexdigest()
	page=40
	text.close()
else:
	
	page=int(sys.argv[2])
	text_location=os.getcwd()+'/'+sys.argv[3]
	text=open(text_location,'r+')
	
	text1=text.readlines()
	md5_hash=hashlib.md5(text.read()).hexdigest()

	text.close()


print md5_hash
if md5_hash not in [s.split(',')[0] for s in file_lines]:
	i=page
	for s in text1[0:page]:
		print s
	key=raw_input()
	while(key!='q'):
		os.system('clear')
		if key=='n':

			for s in text1[i:i+page]:
				print s
			i=i+page
		if key=='p':
			i=i-page
			for s in text1[i-page:i]:
				print s
			
		key=raw_input()
	
	file.write(md5_hash+','+str(i))

else:
	lines_read='0'
	for line in file_lines:
		
		if md5_hash==line.split(',')[0]:
			lines_read=line.split(',')[1]

	i=int(lines_read)
	for s in text1[i:i+page]:
		print s
	key=raw_input()
	while(key!='q'):
		os.system('clear')
		if key=='n':
			for s in text1[i:i+page]:
				print s
			i=i+page
		if key=='p':
			i=i-page
			for s in text1[i-page:i]:
				print s
			

		key=raw_input()
		
	for x in xrange(len(file_lines)):
		if md5_hash==line.split(',')[0]:
			file_lines[x]=line.split(',')[0]+','+str(i)
		file.write(file_lines[x])

os.system('clear')

file.close()


	
	


