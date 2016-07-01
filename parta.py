#Name: Craig Harris
#Student ID: c1335098
#Python Version: 2.7

import sys
import time

def keySetup (arrKey):

	k = []

	for i in range(0,256): #Create list of size 0-256
		k.append(i)

	j = 0

	for i in range(0, 255):
		j = (j + k[i] + arrKey[i % len(arrKey)]) % 256 #Create permutation of list based on key file
		k[i], k[j] = k[j], k[i]

	return k

def stringASCII (String):
	return [ord(c) for c in String] #Convert text String to ASCII Values

def IntASCII (String):
	return ''.join([chr(i) for i in String]) #Convert ASCII to text

def byteGenerator(arrKSetup):

	i = 0
	j = 0

	while True:
		i = (i + 1) % 256
		j = (j + arrKSetup[i]) % 256

		arrKSetup[i], arrKSetup[j] = arrKSetup[j], arrKSetup[i] #Swap values in arrays
		yield arrKSetup[(arrKSetup[i]+arrKSetup[j]) % 256] #Produce one result from the array as the return value


def main(argv):

	total = []

	if argv[1] == "e":

		start = time.time() #Timer function

		file = open(argv[2], 'r') #Opening file found as second argument in command line
		input = file.read()
		file.close()
		key = list(input)

		key = stringASCII(key)

		key = keySetup(key)

		key = byteGenerator(key)

		file = open(argv[3], 'r')
		input = file.read()
		file.close()
		plainTxt = list(input)

		plainTxt = stringASCII(plainTxt)

		output = []

		for i in range(0, len(plainTxt)):
			output.append("%02X" % (plainTxt[i] ^ next(key))) #XOR values and convert to HEX

		file = open(argv[4], 'w')

		for i in output:

			file.write('%s' % i)
		file.close()

		end = time.time()

		print"The function took %s seconds" % (end-start)


	elif argv[1] == "d":
		
		file = open(argv[3], 'r')

		hexxedList = []

		while True:
			hexxedPlain = file.read(2)
			if not hexxedPlain:
				break
			hexxedList.append(hexxedPlain) #Read 2 characters in at a time and add to list

		file = open(argv[2], 'r')
		input = file.read()
		file.close()
		key = list(input)

		key = stringASCII(key)

		key = keySetup(key)

		key = byteGenerator(key)

		baseList = []
		output = []

		for i in range(0, len(hexxedList)):
			baseList.append(int(hexxedList[i], 16)) #Convert back to base 10
			output.append(baseList[i] ^ next(key)) #XOR with key value

		output = IntASCII(output)

		file = open(argv[4], 'w')
		file.write(output)

	else:
		print "EXAMPLE: python parta.py e key.txt plaintext.txt output1.txt"


if __name__ == "__main__":
	main(sys.argv[0:])