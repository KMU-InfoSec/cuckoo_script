import os, hashlib, subprocess, sys


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def move_report():
	for path, dir, files in os.walk("/home/seclab/Desktop/report/04"):
		if not dir:
			dir_name = path.split(os.sep)[-1]

			if dir_name == "exe32" or dir_name == "dll32" or dir_name == "exe64" or dir_name == "dll32":
				for file in files:
					ext = file.split(".")[-1]
					if ext != "csy":
						subprocess.run("sudo mv {SOURCE} {DEST}".format(SOURCE=os.path.join(path, file), DEST="/home/seclab/Desktop/report/report_04"), shell=True)
						print(file, "move complete")

def move_vir():
	for path, dir, files in os.walk("/home/seclab/Desktop/virussign_data/04_vir"):
		if not dir:
			dir_name = path.split(os.sep)[-1]

			if dir_name == "exe32" or dir_name == "dll32" or dir_name == "exe64" or dir_name == "dll64":
				for file in files:
					file_md5 = md5(os.path.join(path, file))

					command = "sudo mv {SOURCE} {DEST}/{MD5}.vir".format(SOURCE=os.path.join(path, file), DEST="/home/seclab/Desktop/report/vir_send_04", MD5=file_md5)
					# print(command)
					subprocess.run(command ,shell=True)
					print(file_md5, "move complete")



if __name__ == '__main__':
	if len(sys.argv) > 1:
		if str(sys.argv[1]) == "report":
			move_report()
		elif sys.argv[1] == 'vir':
			move_vir()
	else:
		print("argv: report | vir")
