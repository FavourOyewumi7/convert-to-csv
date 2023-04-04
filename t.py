import os

root  = os.getcwd

entries = os.scandir(r'C:\Users\favour.oyewumi\OneDrive\Desktop\work')

for file in entries:
    head, tail = os.path.splitext(file)
    print(tail)
	
    src = head+tail
    dst = head+tail+'.csv'
    print(src,dst)
    os.rename(src, dst)



