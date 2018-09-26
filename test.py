import os, sys, json, pickle, shutil


import multiprocessing as mp

def get_report_path_list(PATH) :
    ret = []
    num_of_files = len(os.listdir(PATH))
    for i in range(1, num_of_files) :
        REPORT_PATH = PATH + str(i) + "/reports/report.json"

        if os.path.exists(REPORT_PATH) :
            ret.append(REPORT_PATH)

        else :
            print(REPORT_PATH + " does not exist")


    return ret

def classify(PATH) :
    with open(PATH) as f :
        try :
            report = json.load(f)
            file_name = report["target"]["file"]["name"]
            # file_name = report["target"]["file"]["urls"]["path"].split("/")[-1]

            for p, d, f in os.walk("/home/seclab/Desktop/report") :
                if len(d) == 0 :
                    try:

                        with open(p + "/classify.csy", 'rb') as f :
                            files = pickle.load(f)

                            if file_name in files :
                                shutil.copy(PATH, os.path.join(p, report["target"]["file"]["md5"] + ".json"))
                                print(file_name + ".rjson" + " classify complete")
                                break
                    except:
                        continue

        except Exception as e:
            
            print(e, PATH, " load error")


def run(PATH) :
    report_list = get_report_path_list(PATH)

    sys.setrecursionlimit(2000)

    mp.freeze_support()
    p = mp.Pool( os.cpu_count())
    p.map(classify, report_list)

#    process = []

#    for cpu in range (os.cpu_count()) :
#        proc = Process(target=classify, args=(report_list))
#        process.append(proc)
#        proc.start()
#
#    for proc in process :
#        proc.join()


if __name__ == '__main__':
    run("/home/seclab/.cuckoo/storage/analyses/")

# s = path.split("/")[-1]
