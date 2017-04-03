import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="192.168.43.81"
port=12345
s.bind((host,port))
s.listen(5)

while True:
	conn,addr=s.accept()
	print'got connection..\n'
	print'from '+addr[0]+':'+str(addr[1])

s.send('hello')
s.close()

#to connect with the client .. telnet it to this ip n port confi.
