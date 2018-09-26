import os, json, pickle, subprocess

path = '/home/seclab/Desktop/todo/else/not_mz_file/'

files = os.listdir(path)

for file in files :
       subprocess.call(["mv", path + file, path + file.split("_")[-1]]) 

