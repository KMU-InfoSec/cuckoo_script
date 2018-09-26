import os, csv



def main() :
	for path, dir, files in os.walk("/home/seclab/Desktop/kbw_Analyses_FIN/kbw_for_cuckoo (1)") :
		print(dir)
		if len(dir) == 0 :
			dir_name = path.split(os.sep)[-1]

			with open(os.path.join("/home/seclab/Desktop/kbw_Analyses_FIN/kbw_for_cuckoo (1)", dir_name + ".csv"), "w", encoding="utf-8", newline="") as f :
				csvWriter = csv.writer(f)

				for file in files :
					csvWriter.writerow([dir_name, file.split(".")[0]])
					print(dir_name, file.split(".")[0], "write success")


if __name__ == '__main__':
	main()