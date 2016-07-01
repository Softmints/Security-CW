#Name: Craig Harris
#Student ID: c1335098
#Python Version: 2.7

import sys

def stringASCII (String):
	return [ord(c) for c in String] #Convert text String to ASCII Values

def IntASCII (String):
	return ''.join([chr(i) for i in String]) #Convert ASCII to text

def main(argv):

	file = open(argv[1], 'r')

	hexxedListA = []

	while True:
		hexxedPlain = file.read(2)
		if not hexxedPlain:
			break
		hexxedListA.append(hexxedPlain)

	file = open(argv[2], 'r')

	hexxedListB = []

	while True:
		hexxedPlain = file.read(2)
		if not hexxedPlain:
			break
		hexxedListB.append(hexxedPlain)

	file = open(argv[3], 'r')
	input = file.read()
	file.close()
	plainText = list(input)

	plainList = []

	for char in plainText:
		plainList.append(char)

	asciiPlain = stringASCII(plainList)

	asciiA = []
	asciiB = []

	for i in range(0, len(hexxedListA)):
		asciiA.append(int(hexxedListA[i], 16))

	for i in range(0, len(hexxedListB)):
		asciiB.append(int(hexxedListB[i], 16))

	newOut = []
	output = []

	for i in range(0, len(hexxedListA)):
		newOut.append(asciiA[i] ^ asciiPlain[i])
		output.append(newOut[i] ^ asciiB[i])

	finalOut = IntASCII(output)

	print finalOut

	file = open('PartCOutput.txt', 'w')

	for i in finalOut:

		file.write('%s' % i)
	file.close()


if __name__ == "__main__":
	main(sys.argv[0:])