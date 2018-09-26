import os

def main() :
	for path, dir, files in os.walk("/home/seclab/Desktop/report") :
		for file in files :
			if file == "classify.csy" :
				os.remove(os.path.join(path, file))


if __name__ == '__main__':
	main()