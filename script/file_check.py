import subprocess, os, sys

def check(PATH) :
    m = {}
    for path, dir, files in os.walk(PATH) :
        if len(dir) == 0 :
            for file in files :
                file_path = os.path.normpath(os.path.abspath(os.path.join(path, file)))
               # print(file_path)
                echo = subprocess.check_output(["file", file_path], universal_newlines=True)
                print(echo)
#                if "Zip" in echo or "MS" in echo or "gzip" in echo or "RAR" in echo :
#                if "PE32" not in echo and "MS-DOS" not in echo and "DOS" not in echo :
#                   subprocess.call(["mv", file_path, "/home/seclab/Desktop/kbw_Analyses_FIN/kbw_for_cuckoo/not_mz_file/zip_file/"])
                    #foramt = echo[1]
                   # if echo[1] in m :
                    #    m[echo[1]] += 1
                    #else :
                     #   m[echo[1]] = 1

#                    print(file_path, echo)
    
#    print(m)

if __name__ == '__main__':
    if len(sys.argv) > 1 :
        check(sys.argv[1])
    else :
        print("error")
