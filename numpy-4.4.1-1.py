import numpy as np

quarter=np.array([1,2,3,4], dtype=int)
results=np.array([37.4,47.3,73.4,99])
outfile=open("q4.txt","w")
outfile.write("The results for the first quarters\n\n")
for q,r in zip(quarter, results):
    outfile.write("For quarter %d the result is %5.1f\n"%(q,r))
    
outfile.close()