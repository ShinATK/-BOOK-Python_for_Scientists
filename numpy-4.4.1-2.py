infile=open("q4.txt", "r")
lquarter=[]
lresult=[]
temp=infile.readline()
for line in infile:
    words=line.split()
    lquarter.append(int(words[2]))
    lresult.append(float(word[6]))
infile.close()
import numpy as np
aquarter=np.array(lquarter, dtype=int)
aresult=n.array(lresult)
print(aquarter)
print(aresult)