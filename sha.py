import os, sys
import hashlib
 
def getHash(path, blocksize=65536):
    afile = open(path, 'rb')
    hasher = hashlib.sha256()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()



f1 = getHash("/home/seclab/Desktop/kbw_Analyses_FIN/kbw_for_cuckoo (1)/Scarcruft/c45aa30e4a6567050bfbbbfc028f0865.vir")
f2 = getHash("/home/seclab/Desktop/kbw_Analyses_FIN/kbw_for_cuckoo (1)/Andariel/07a18cd4f6db547588e513d8ccd4854e.vir")

print(f1, f2)