import os, csv, subprocess


def main() :
	for path, dir, files in os.walk("/home/seclab/Desktop/kbw_Analyses_FIN/kbw_for_cuckoo/not_mz_file/zip_file") :
		dir_name = path.split(os.sep)[-1]

		with open("/home/seclab/Desktop/kbw_zipfile_info.csv", "a+", encoding="utf-8", newline="") as f :
			csvWriter = csv.writer(f)
			for file in files :
				sub = subprocess.check_output(["file", os.path.join(path, file)], universal_newlines=True)
				file_info = sub.split(" ")[1:]

				csvWriter.writerow(["/".join(path.split(os.sep)[6:]), file, len(files),  " ".join(file_info)])








if __name__ == '__main__':
	main()