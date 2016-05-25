def mapper():
	inputFile=open("/home/training/udacity_training/data/purchases.txt",'r')
	outputFile=open("mapperOutput.txt", 'w')
	for curr in inputFile:
		data = curr.strip().split("\t")
		if(len(data)!=6):
			continue
		try:
			if(data[3] == "Toys"):
				outputFile.write("Toys" + "\t" + data[4]+"\n")
			if(data[3] == "Consumer Electronics"):
				outputFile.write("Consumer Electronics" +"\t" + data[4] + "\n")
		except Exception:
			print ""


if __name__ == '__main__':
	mapper()
