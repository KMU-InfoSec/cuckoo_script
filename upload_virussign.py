#-*-coding:utf-8-*-
import requests, os, subprocess

import time, sys, pickle
import multiprocessing as mp

REST_URL = "http://localhost:8090/tasks/create/file"
#DIRECTORY = "/home/seclab/virussign_20170727"

def explorer( root ):
    ret = []
    file_list = []

    save_root_path = "/home/seclab/Desktop/report"
    save_dir_path = ""
    before_save_dir_name = ""

    for p, dir, files in os.walk(root) :

        save_dir_name_check = p.split(os.sep)[-1]


        if "virussign" in save_dir_name_check:
            if not os.path.exists(os.path.join(save_root_path, save_dir_name_check.split("_")[1])):
                save_dir_name = save_dir_name_check.split("_")[1]
                save_dir_path = os.path.join(save_root_path, save_dir_name)
                os.mkdir(save_dir_path)

                before_save_dir_name = save_dir_name

        if len(file_list) > 0 and before_save_dir_name != save_dir_name:
            with open(os.path.join(save_root_path, before_save_dir_name, "classify.csy"), "wb") as f:
                pickle.dump(file_list, f)
            file_list.clear()



        # if root_dir[1] != '':
        #     tmp = os.path.join(root_path, p.split(root.split(os.sep)[-1])[1][1:])
        # else :
        #     tmp = root_path
        # if len(dir) != 0 :
        #     for dir_name in dir :
        #         try :
        #             os.mkdir(os.path.join(tmp, dir_name))
        #         except :
        #             pass
        if not dir:
            dir_name = p.split(os.sep)[-1]

            if dir_name == "dll32" or dir_name == "exe32":
                for file in files:
                    ret.append(os.path.join(p, file))
                    file_list.append(file)

            if dir_name == "dll64" or dir_name == "exe64":
                for file in files:
                    file_list.append(file)

    return ret


def get_file_name ( file_path ) :
    return os.path.basename(file_path)


def send_file(file_path):
    with open(file_path, 'rb') as f:
        file_name = get_file_name(file_path)
        fs = {'file' : (file_name, f)}
        r = requests.post(REST_URL, files=fs)
        if r.status_code == 200:
            print("{} is succeeded".format(file_name))
        else :
            print("{} is failed".format(file_name))


def run(root, process_count=os.cpu_count()):
    file_path_list = explorer(root)
    mp.freeze_support()
    p = mp.Pool(process_count)
    p.map(send_file, file_path_list)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        start = time.time()
        run(sys.argv[1])
        print("Time : {}".format(time.time() - start))
    elif len(sys.argv) == 3:
        start = time.time()
        run(sys.argv[1], int(sys.argv[2]))
        print("Time : {}".format(time.time() - start))


