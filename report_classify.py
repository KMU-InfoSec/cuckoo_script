import os, sys, json, pickle, shutil,subprocess

import multiprocessing as mp
import pathos.pools as pp
#from multiprocessing import Process


def get_pcap_path_list(path):
    ret = []
    num_of_files = len(os.listdir(path))
    for i in range(1, num_of_files):
        pcap_path = os.path.join(path, str(i), "dump.pcap")

        if os.path.exists(pcap_path):
            ret.append(pcap_path)
            print(pcap_path, "added to the list")
        else:
            print(pcap_path + " does not exist")

    return ret

def get_report_path_list(path) :
    ret = []
    num_of_files = len(os.listdir(path))
    for i in range(1, num_of_files) :
        report_path = os.path.join(path, str(i), "reports", "report.json")

        if os.path.exists(report_path) :
            ret.append(report_path)
            print(report_path, "added to the list")
        
        else :
            print(report_path + " does not exist")

    return ret


def report_classify(report_path, pcap_path):
    with open(report_path) as a:
        try:
            report = json.load(a)
            file_name = report["target"]["file"]["name"]
            md5_file_name = report["target"]["file"]["md5"]

            for p, dir, f in os.walk("/home/seclab/Desktop/report"):
                if not dir:
                    try:
                        with open(p + "/classify.csy", 'rb') as b:
                            files = pickle.load(b)

                            if file_name in files:
                                shutil.copy(report_path, os.path.join(p, md5_file_name + ".json"))
                                print(md5_file_name + ".json" + " classify complete")

                        shutil.copy(pcap_path, os.path.join(p, md5_file_name + ".pcap"))
                        print(md5_file_name + ".pcap" + " classify complete")
                        break

                    except:
                        continue

        except:
#            print(path, e)
            pass


# def pcap_classify(path):
#     with open(path) as a:
#         try:
#             # report = json.load(a)
#             # file_name = report["target"]["file"]["name"]
#             # md5_file_name = report["target"]["file"]["md5"]
#
#             for p, dir, f in os.walk("/home/seclab/Desktop/report"):
#                 if not dir:
#                     try:
#
#                         with open(p + "/classify.csy", 'rb') as b:
#                             files = pickle.load(b)
#
#                             if file_name in files:
#                                 shutil.copy(path, os.path.join(p, md5_file_name + ".pcap"))
#                                 print(md5_file_name + ".pcap" + " classify complete")
#                                 break
#                     except:
#                         continue
#         except:
# #            print(path, e)
#             pass


def csy_remove():
    for path, dir, file in os.walk("/home/seclab/Desktop/report"):
        if not dir:
            try:
                os.remove(os.path.join(path, "classify.csy"))
            except:
                continue

def run(path):
    sys.setrecursionlimit(2000)

    report_list = get_report_path_list(path)
    pcap_list = get_pcap_path_list(path)

    p = pp.ProcessPool(os.cpu_count())

    p.map(report_classify, report_list, pcap_list)


    # process1 = []
    # process2 = []

    # for report_cpu in range(30):
    #     proc = Process(target=report_classify, args=report_list)
    #     # proc2 = Process(target=pcap_classify, args=pcap_list)
    #     process1.append(proc)
    #     # process2.append(proc2)
    #     proc.start()
    #     # proc2.start()

    # for proc in process1:
    #     proc.join()

    # for proc in process2:
    #     proc.join()


if __name__ == '__main__':
    run("/home/seclab/.cuckoo/storage/analyses")

