#Name: Craig Harris
#Student ID: c1335098
#Python Version: 2.7

import sys

def stringASCII (String):
	return [ord(c) for c in String]

def IntASCII (String):
	return ''.join([chr(i) for i in String])

def main(argv):

	origList = []
	repList = []

	byteStart = argv[2]
	byteEnd = argv[3]

	original = argv[4]
	replace = argv[5]

	for char in original:
		origList.append(char)

	for char in replace:
		repList.append(char)
		
	file = open(argv[1], 'r')

	hexxedList = []

	while True:
		hexxedPlain = file.read(2)
		if not hexxedPlain:
			break
		hexxedList.append(hexxedPlain)

	origList = stringASCII(origList)
	repList = stringASCII(repList)

	baseList = []
	firstOut = []

	for i in range(0, len(hexxedList)):
		baseList.append(int(hexxedList[i], 16))

	for i in range(0, int(byteEnd)-int(byteStart) + 1):
		pointer = (int(byteStart)-1+i)
		firstOut.append(baseList[pointer] ^ origList[i])

	output = []

	for i in range(0, len(repList)):
		output.append("%02X" % (firstOut[i] ^ repList[i]))

	for i in range(0, int(byteEnd)-int(byteStart) + 1):
		pointer = (int(byteStart)-1+i)
		hexxedList[pointer] = output[i]

	file = open('PartBOutput.txt', 'w')

	for i in hexxedList:

		file.write('%s' % i)
	file.close()

if __name__ == "__main__":
	main(sys.argv[0:])