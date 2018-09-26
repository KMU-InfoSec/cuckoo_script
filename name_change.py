import os, subprocess, json

PATH = "/home/seclab/Desktop/kbw_report/not_mz_file/"

files = os.listdir(PATH)

for file in files :
    with open(PATH + file) as f :
        try :

            report = json.load(f)

            md5 = report["target"]["file"]["md5"]

            subprocess.call(["mv", PATH+file, PATH+md5+".json"])
        
        except :
            pass

