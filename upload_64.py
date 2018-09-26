#-*-coding:utf-8-*-
import requests, os, subprocess

import time, sys, pickle
import multiprocessing as mp

REST_URL = "http://localhost:8090/tasks/create/file"
#DIRECTORY = "/home/seclab/virussign_20170727"

def explorer( root ):
    ret = []
    
    root_path = "/home/seclab/Desktop/report"

    for p, dir, files in os.walk(root) :
        
        root_dir = p.split(root.split(os.sep)[-1])

        if root_dir[1] != '':
            tmp = os.path.join(root_path, p.split(root.split(os.sep)[-1])[1][1:])
        else :
            tmp = root_path
        if len(dir) != 0 :
            for dir_name in dir :
                try :

                    os.mkdir(os.path.join(tmp, dir_name))
                except :
                    pass
        else :

            file_list = []
            dir_name = p.split(os.sep)[-1]
            
            if dir_name != "dll64" and dir_name != "exe64" :
                continue

            for file in files :
#                output = subprocess.check_output(["file", os.path.join(p, file), ], universal_newlines=True)

 #               if output.split(" ")[1] == "PE32+":
                ret.append(os.path.join(p, file))
                file_list.append(file)
                #print(file + " append to the pool")
            
            with open(os.path.join(tmp, "classify.csy"), "wb") as f :
                pickle.dump(file_list, f)

    
    
    return ret

def get_file_name ( file_path ) :
    return os.path.basename(file_path)

def send_file( file_path ) :
    with open(file_path, 'rb') as f :
        file_name = get_file_name(file_path)
        fs = {'file' : (file_name, f)}
        r = requests.post(REST_URL, files=fs)
        if r.status_code == 200 :
            print("{} is succeeded".format(file_name))
        else :
            print("{} is failed".format(file_name))

def run( root , process_count = os.cpu_count() ) :
    file_path_list = explorer(root)
    mp.freeze_support()
    p = mp.Pool( process_count )
    p.map(send_file, file_path_list)

if __name__ == '__main__' :
    if len(sys.argv) == 2 :
        start = time.time()
        run(sys.argv[1])
        print("Time : {}".format(time.time() - start))
    elif len(sys.argv) == 3 :
        start = time.time()
        run(sys.argv[1], int(sys.argv[2]))
        print("Time : {}".format(time.time() - start))


