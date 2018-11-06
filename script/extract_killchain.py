import json, pickle, os
from multiprocessing import Process


def get_num_of_folder(path):
    return len(os.listdir(path))


def ip(report):
    ret = []

    dst_num = len(report["network"]["tcp"])
    for i in range(0, dst_num + 1):
        try:
            ret.append(report["network"]["tcp"][i]["dst"] + ":" + str(report["network"]["tcp"][i]["dport"]))
        except IndexError:
            break

    try:
        num_of_dead_hosts = len(report["network"]["dead_hosts"])
        if num_of_dead_hosts > 0:
            for dead_host_element in report["network"]["dead_hosts"]:
                ret.append(dead_host_element[0] + ":" + str(dead_host_element[1]))
    except:
        pass

    return ret


def domain(report):
    ret = []

    try:
        domain_num = len(report["network"]["domains"])
        if domain_num > 0:
            for i in range(0, domain_num + 1):
                ret.append(report["network"]["domains"][i]["domain"] + ":" + report["network"]["domains"][i]["ip"])
    except:
        pass

    return ret


def behavior_file(report):
    ret = []
    try:
        num_of_file_created = len(report["behavior"]["summary"]["file_created"])

        if num_of_file_created > 0:
            for file_create_info in report["behavior"]["summary"]["file_created"]:
                ret.append(file_create_info)
    except:
        pass

    try:
        num_of_file_delete = len(report["behavior"]["summary"]["file_deleted"])

        if num_of_file_delete > 0:
            for file_delete_info in report["behavior"]["summary"]["file_deleted"]:
                ret.append(file_delete_info)
    except:
        pass

    try:
        num_of_file_opened = len(report["behavior"]["summary"]["file_opened"])

        if num_of_file_opened > 0:
            for file_open_info in report["behavior"]["summary"]["file_opened"]:
                ret.append(file_open_info)
    except:
        pass

    try:
        num_of_file_written = len(report["behavior"]["summary"]["file_written"])

        if num_of_file_written > 0:
            for file_write_info in report["behavior"]["summary"]["file_written"]:
                ret.append(file_write_info)
    except:
        pass

    try:
        num_of_file_read = len(report["behavior"]["summary"]["file_read"])

        if num_of_file_read > 0:
            for file_read_info in report["behavior"]["summary"]["file_read"]:
                ret.append(file_read_info)
    except:
        pass

    try:
        num_of_file_exists = len(report["behavior"]["summary"]["file_exists"])

        if num_of_file_exists > 0:
            for file_exist_info in report["behavior"]["summary"]["file_exists"]:
                ret.append(file_exist_info)
    except:
        pass

    return ret


def behavior_regkey(report):
    ret = []

    try:
        num_of_regkey_opened = len(report["behavior"]["summary"]["regkey_opened"])

        if num_of_regkey_opened > 0:
            for reg_info in report["behavior"]["summary"]["regkey_opened"]:
                ret.append(reg_info)
    except:
        pass

    try:
        num_of_regkey_read = len(report["behavior"]["summary"]["regkey_read"])

        if num_of_regkey_read > 0:
            for reg_info in report["behavior"]["summary"]["regkey_read"]:
                ret.append(reg_info)
    except:
        pass

    try:
        num_of_regkey_written = len(report["behavior"]["summary"]["regkey_written"])

        if num_of_regkey_written > 0:
            for reg_info in report["behavior"]["summary"]["regkey_written"]:
                ret.append(reg_info)
    except:
        pass

    return ret


def dropped(report):
    ret = []
    try:
        if len(report["dropped"]) > 0:
            for drop in report["dropped"]:
                ret.append([drop["name"]])
    except:
        pass

    return ret


def pdb_path(report):
    ret = ""

    try:
        pdb_path = report["static"]["pdb_path"]
        if pdb_path is not None:
            ret = report["static"]["pdb_path"]
    except:
        pass

    return ret


def get_signature(report):
    ret = {}

    try:
        for signature_index in report["signatures"]:
            ret[signature_index["name"]] = signature_index["description"]
    except:
        pass

    return ret


def parsing(path):
    for p, d, files in os.walk(path):
        if not d:
            dir_name = p.split(os.sep)[-1]
            if not os.path.exists(os.path.join(DIR_PATH, dir_name)):
                os.mkdir(os.path.join(DIR_PATH, dir_name))

            for file in files:

                dat_cyber_killchane = os.path.join({PATH}, dir_name, file.split(".")[0] + ".killchain")

                file_path = os.path.join(p, file)

                with open(file_path) as f:
                    try:
                        report = json.load(f)

                        ip_list = ip(report)
                        behavior_file_list = behavior_file(report)
                        behavior_regkey_list = behavior_regkey(report)
                        domain_list = domain(report)
                        dropped_list = dropped(report)
                        _pdb_path = pdb_path(report)
                        signature_dict = get_signature(report)


                        pickle_dict = {}

                        weaponization = {"Signatures": signature_dict, "PDB": _pdb_path}
                        installation = {"Dropped": dropped_list}
                        c2 = {"Domain": domain_list, "Ip": ip_list}
                        action = {"File": behavior_file_list, "Register": behavior_regkey_list}
                        
                        pickle_dict["Weaponization"] = weaponization
                        pickle_dict["Installation"] = installation
                        pickle_dict["C2"] = c2
                        pickle_dict["Action"] = action

                        pickle_dict = json.dumps(pickle_dict)

                        with open(dat_cyber_killchane, 'w') as f:
                            json.dump(pickle_dict, f, indent="\t")

                        print(file, "Complete to Extract Cyber Killchain")

                    except Exception as e:
                        print(e)
                        print(file_path + " error")
                        pass
            else:
                continue

    print("Extract Complete")


def run(PATH={PATH}):
    process = []

    for cpu in range(10) :
        proc = Process(target=parsing, args=PATH)
        process.append(proc)
        proc.start()

    for proc in process :
        proc.join()

if __name__ == '__main__':
    # if len(sys.argv) == 1:
    #     print("arg 1 : Type the report folder path")
    # elif len(sys.argv) == 2:
    #     report_path = sys.argv[1]
    parsing({PATH})
