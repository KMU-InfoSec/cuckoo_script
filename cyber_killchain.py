import json, os


def explore(path, data):
    if type(data) == type(str()):
        print('{0} >>> {1}'.format(path, data))

    elif type(data) == type(dict()):
        key_list = list(data.keys())

        for key in key_list :
            explore(path + " | " + key, data[key])

    elif type(data) == type(list()):
        for element in data :
            # path += " | " + element
            explore(path, element)
            break
    else:
        return


def run(PATH):
    
    for path, dir, files in os.walk(PATH) :
        for file in files :
            print('--{0} analysis start--'.format(file))

            with open(os.path.join(path, file)) as f:
                report = json.load(f)
            key_list = list(report.keys())
        
            for key in key_list:
                _path = ""
                _path += key
                explore(_path, report[key])

            print('------------------------------------')
            print('\n')


if __name__ == '__main__':
    run(PATH)

