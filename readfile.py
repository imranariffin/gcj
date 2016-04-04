def readfile(name):
	ret = ""
	with open("input.txt") as fi:
		ret = fi.read()
		fi.close()	
	return ret

if __name__=="__main__":
	with open("input.txt") as fi:
		print fi.read()
		fi.close()