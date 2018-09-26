import subprocess

if __name__ == '__main__':
    for i in range(36, 56) :
        if 1 <= i and i < 10 :
            subprocess.call(["sudo", "cuckoo", "machine", "--add", "cuckooWin7x86_%d" %i, "192.168.56.1" + str(i % 10)])
        elif 10 <= i and i < 20 :
            subprocess.call(["sudo", "cuckoo", "machine", "--add", "cuckooWin7x86_%d" %i, "192.168.56.2" + str(i % 10)])
        elif 20 <= i and i < 30 :
            subprocess.call(["sudo", "cuckoo", "machine", "--add", "cuckooWin7x86_%d" %i, "192.168.56.3" + str(i % 10)])
        elif 30 <= i and i < 40 :
            subprocess.call(["sudo", "cuckoo", "machine", "--add", "cuckooWin7x86_%d" %i, "192.168.56.4" + str(i % 10)])
        elif 40 <= i and i < 50 :
            subprocess.call(["sudo", "cuckoo", "machine", "--add", "cuckooWin7x86_%d" %i, "192.168.56.5" + str(i % 10)])
        elif 50 <= i and i < 60 :
            subprocess.call(["sudo", "cuckoo", "machine", "--add", "cuckooWin7x86_%d" %i, "192.168.56.6" + str(i % 10)])
        elif 60 <= i and i < 70:
            subprocess.call(["sudo", "cuckoo", "machine", "--add", "cuckooWin7x86_%d" %i, "192.168.56.7" + str(i % 10)])
        else :
            subprocess.call(["sudo", "cuckoo", "machine", "--add", "cuckooWin7x86_%d" %i, "192.168.194.8" + str(i % 10)])
