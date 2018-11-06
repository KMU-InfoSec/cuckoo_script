import sys, os, json

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

def check(PATH) :
    for path, dir, files in os.walk(PATH) :
        if len(dir) == 0 :
            for file in files :
                with open(os.path.join(path, file)) as f :
                    try :
                        report = json.load(f)
                        processes = report["behavior"]["processes"]

                    except :
                        print(os.path.join(path, file))


if __name__ == '__main__':
    if len(sys.argv) > 1 :
        check(sys.argv[1])
