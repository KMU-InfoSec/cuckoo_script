
import json, csv
import sys, os
import pickle, io


# change the range

def get_num_of_folder(path) :
    return len(os.listdir(path))

def mutex(report):
    ret = []

    try:
        for mut in report["behavior"]["summary"]["mutex"]:
            ret.append(mut)

        ret.append(report["target"]["file"]["yara"]["meta"]["description"])
    except:
        pass

    return ret

def strings(report):
    ret = []
    try:
        if len(report["strings"]) > 0:
            for string in report["strings"]:
                ret.append(string)
    except:
        pass

    return ret

def ip(report):
    # ret = []
    ret = set([])

    dst_num = len(report["network"]["tcp"])
    for i in range(0, dst_num + 1):
        try:
            ret.append(report["network"]["tcp"][i]["dst"])
        except IndexError:
            break

    return ret

def api(report):
    ret = []

    try:
        processes = report["behavior"]["processes"]
        for i in range(0, len(processes)):
            if processes[i]["track"]:
                for j in range(0, len(processes[i]["calls"])):
                    ret.append(processes[i]["calls"][j]["api"])
    except:
        pass

    return ret

def domain(report):
    ret = []
    # ret = set([])

    try:
        domain_num = len(report["network"]["domains"])
        if domain_num > 0:
            for i in range(0, domain_num):
                ret.append(report["network"]["domains"][i])
    except:
        print("domain error")
        pass

    return ret

def parsing(path) :
    for p, d, files in os.walk(path):
        if len(d) == 0 :
            dir_name = p.split(os.sep)[-1]
            if not os.path.exists("/home/seclab/Desktop/kbw_json_parse/" + dir_name) :
                os.mkdir("/home/seclab/Desktop/kbw_json_parse/" + dir_name)
                
            for file in files :
                if file != "classify.csy" :

                    DAT_STRING_PATH = os.path.join("/home/seclab/Desktop/kbw_json_parse", dir_name, file + ".str")
                    DAT_DOMAINS_PATH = os.path.join("/home/seclab/Desktop/kbw_json_parse", dir_name, file + ".dom")
                    DAT_IP_PATH = os.path.join("/home/seclab/Desktop/kbw_json_parse", dir_name, file + ".ip")
                    DAT_MUTEX_PATH = os.path.join("/home/seclab/Desktop/kbw_json_parse", dir_name, file + ".mut")
                    DAT_API_PATH = os.path.join("/home/seclab/Desktop/kbw_json_parse", dir_name, file + ".asc")

                    file_path = os.path.join(p, file)

                    with open(file_path) as f:
                        try :
                            report = json.load(f)

                            str_list = strings(report)
                            domain_list = domain(report)
                            ip_list = ip(report)
                            mut_list = mutex(report)
                            api_list = api(report)

                            with open(DAT_STRING_PATH, 'wb') as str_dat, open(DAT_DOMAINS_PATH, 'wb') as dom_dat, open(DAT_MUTEX_PATH, 'wb') as mut_dat , open(DAT_API_PATH, 'wb') as api_dat, open(DAT_IP_PATH, 'wb') as ip_dat:
                                pickle.dump(str_list, str_dat)
                                pickle.dump(domain_list, dom_dat)
                                pickle.dump(ip_list, ip_dat)
                                pickle.dump(mut_list, mut_dat)
                                pickle.dump(api_list, api_dat)
                                print("Complete")

                        except :
                            print(file_path + " error")
                            pass
                else :
                    continue

    print("Parsing Complete")

def run(PATH) :
    process = []

    for cpu in range(50) :
        proc = Process(target=parsing, args=PATH)
        process.append(proc)
        proc.start()

    for proc in process :
        proc.join()



if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("arg 1 : Type the report folder path")
    elif len(sys.argv) == 2:
        report_path = sys.argv[1]
        run(report_path)





