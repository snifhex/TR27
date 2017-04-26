import os

def encrypt(a, b):
	alphaLibrary=list('abcdefghijklmnopqrstuvwxyz')
	cipher = ''
	while len(b) < len(a):
		b=b*2
	b = b[:len(a)]

	for character,key in zip(a,b):
		if character == ' ':
			cipher = cipher+' '
		elif character == '!':
			cipher = cipher + '!'
		elif character == '.':
			cipher = cipher + '.'
		else:
			newIndex = alphaLibrary.index(character) + int(key)
			if newIndex < 26:
				cipher = cipher + alphaLibrary[newIndex]
			else:
				cipher = cipher + alphaLibrary[newIndex%26]

	print cipher

def decrypt(a, b):
	alphaLibrary=list('abcdefghijklmnopqrstuvwxyz')
	decipher = ''
	while len(b) < len(a):
		b=b*2
	b = b[:len(a)]

	for character,key in zip(a,b):
		if character == ' ':
			decipher = decipher+' '
		elif character == '!':
			decipher = decipher + '!'
		elif character == '.':
			decipher = decipher + '.'
		else:
			newIndex = alphaLibrary.index(character) - int(key)
			if newIndex < 26:
				decipher = decipher + alphaLibrary[newIndex]
			else:
				decipher = decipher + alphaLibrary[newIndex%26]

	print decipher



def main():
	userSelection = raw_input("\n[*] What you want to do sir? \n[1] Encryt \n[2] Decrypt \n> ")
	if userSelection== str(1):
		os.system('clear')
		print 'Welcome, You have selected Encryt!!'
		plainTxt=list(raw_input('[*] Enter your text you want to convert \n >'))
		key=list(raw_input('[*] Enter encryption key \n >'))
		encrypt(plainTxt,key)

	elif userSelection==str(2):
		os.system('clear')
		print 'Welcome, You have selected Decryt!!'
		plainTxt=list(raw_input('[*] Enter your text you want to convert \n >'))
		key=list(raw_input('[*] Enter decryption key \n >'))
		decrypt(plainTxt,key)
		
	else:
		print '\tOops! wrong selection please select encrypt or decrypt.'
		print '\t\t\tSelect "1" for Encrypt.'
		print '\t\t\tSelect "2" for Decrypt.\n'

main()