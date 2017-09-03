from ftplib import FTP
print 'FTP connector :'
add=raw_input('enter address or ip: ')
ftp=FTP() 
ftp.connect(add)
login_id=raw_input('enter login id:')
login_pass=raw_input('enter login password:')
ok=ftp.login(login_id,login_pass)
print ok
print  ftp.getwelcome()
print ftp.retrlines('LIST')
ftp.close()
