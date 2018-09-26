import csv, os, subprocess, sys




def run(PATH) :
    for path, dir, files in os.walk(PATH) :
        if len(dir) == 0 :
            dir_name = path.split(os.sep)[-1]

            csv_path = "/home/seclab/Desktop/virussign_information.csv"

            file_list = []

            for file in files :
                file_format_string = subprocess.check_output(["file", os.path.join(path, file)], universal_newlines=True)
                
#                print(file_format_string)
                file_format = file_format_string.split(" ")[1]

                
                #print(dir_name + " " + file + " " + file_format)
                file_list.append(dir_name + " " + file + " " + file_format)
            with open(csv_path, "a+", newline="") as f :
                csvWriter = csv.writer(f)

                for write in file_list :
                    print(write)
                    csvWriter.writerow([write.split(" ")[0], write.split(" ")[1], write.split(" ")[2]])


if __name__ == '__main__':
    if len(sys.argv) > 1 :
        run(sys.argv[1])
