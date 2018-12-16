import numpy as np

text_file = open("d3.txt", "r")
lines = text_file.read().split('\n')

data = lines[:-1]


a = np.ndarray((1000,1000))
a[:] = 0
# a[2:4,5:9] = 1
# print a[2:4,5:9].any()==1
# sdffd

for d in data:
    idx = d.find('@')
    pid = d[:idx]
    info = d[idx+2:]
    l = info[:info.find(',')]
    t = info[info.find(',')+1:info.find(':')]
    w = int(info[info.find(':')+2:info.find('x')])
    h = int(info[info.find('x')+1:])
    i = int(t)
    j = int(l)
    
    a[i:i+h,j:j+w] =  a[i:i+h,j:j+w]+1


cnt = 0
for i in range(1000):
    for j in range(1000):
        if a[i,j]>1:
            cnt +=1


print cnt

for d in data:
    idx = d.find('@')
    pid = d[:idx]
    info = d[idx+2:]
    l = info[:info.find(',')]
    t = info[info.find(',')+1:info.find(':')]
    w = int(info[info.find(':')+2:info.find('x')])
    h = int(info[info.find('x')+1:])
    i = int(t)
    j = int(l)

    b = a[i:i+h,j:j+w]
    array = b.flatten()
    if np.sum(array) == len(array):
        print array
        print pid



