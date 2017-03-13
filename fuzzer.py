#!/usr/bin/python -w

import socket, sys, time, struct


if len(sys.argv) < 2:
	print "[-] Usage:%s <target address> <target port> <length of fuzz>"
	print "[-] Example: fuzzer.py 192.168.1.100 22 3000"
	sys.exit(0)

target = sys.argv[1]
#port = sys.argv[2]
#flength = sys.argv[3]

buffer = 'x41'*50

print "\
[+] Basic Fuzzer v1.0\n\
[+] Author: Chris Neal (g0jirasan)\n\
[+] Connecting to "+target


while True:


	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		s.settimeout(2)
		s.connect((target, 22))
		s.recv(1024)


		print "[*] Sending..."
		print "[*] Length "+ str(len(buffer))

		s.send(buffer)
		s.close()
		time.sleep(4)
		buffer = buffer + 'x41'*50

	except:
		print "[-] Connection to "+target+" failed!"
		sys.exit(0)



