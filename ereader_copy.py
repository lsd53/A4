#! /usr/bin/python 
import termios, sys, os, hashlib
#import termios, TERMIOS, sys, os
TERMIOS = termios
def getkey():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
        new[6][TERMIOS.VMIN] = 1
        new[6][TERMIOS.VTIME] = 0
        termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
        c = None
        try:
                c = os.read(fd, 1)
        finally:
                termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
        return c

if not (os.path.isfile(os.path.expanduser('~')+'/.reader_rc')):
	file=open(os.path.expanduser('~')+'/.reader_rc','w+b')
else:
	file=open(os.path.expanduser('~')+'/.reader_rc','r+')

if len(sys.argv) == 2:
	text_location=os.getcwd()+'/'+sys.argv[1]
	text=open(text_location,'r+')
	
	text1=text.readlines()
	md5_hash=hashlib.md5(text.read()).hexdigest()

	n = 40

	def printlines(n):
		for s in text1[i:i+n]:
			print s

	i=0

	printlines(n)
	while(getkey()!='q'):
		printlines(n)
		while(getkey()==pus'n'):
			i=i+n
			printlines(n)
		while(getkey()=='p'):
			i=i-n
			printlines(n)
	print "Exiting..."
else:
	print "Please enter a filename"