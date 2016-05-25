def reducer():
	inputFile = open("finalMapper.txt", "r")
	outputFile = open("reducerOut.txt", "w")
	
	type = None
	value = 0
	for curr in inputFile:
		data = curr.strip().split("\t")
		if(len(data)!=2):
			continue
		if(data[0]!=None and type==None):
			type=data[0]
			value += float(data[1])
			continue

		if(data[0]!=type):
			outputFile.write(type + '\t' + str(value)+'\n')
			type=data[0]
			value = 0
			value += float(data[1])	
		else:
			value += float(data[1])	
	
	if(type!=None):
		outputFile.write(type + '\t' + str(value)+'\n')

if __name__ == "__main__":
	reducer()
