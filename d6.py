from datetime import datetime
import numpy as np

text_file = open("d6.txt", "r")
lines = text_file.read().split('\n')[:-1]


size = 350
data = np.zeros((size,size))

for i in lines:
    print i


# size = 10
# data = np.zeros((size,size))
# lines =[
#     (1, 1),
#     (1, 6),
#     (8, 3),
#     (3, 4),
#     (5, 5),
#     (8, 9),
#     ]
# max_dist = 32


print np.shape(data)

for k,d in enumerate(lines):
    # j = d[0]
    # i = d[1]
    j = int(d.split(',')[0])
    i = int(d.split(',')[1])
    data[i,j] = k


max_dist = 10000

for l in range(size):
    for m in range(size):
        dist_short = size+size
        dist_all = 0
        for k,d in enumerate(lines):
            j = int(d.split(',')[0])
            i = int(d.split(',')[1])
            # j = d[0]
            # i = d[1]

            dist = np.abs(i-l)+np.abs(j-m)
            # if dist<dist_short:
            #     dist_short = dist
            #     val = k
            # elif dist == dist_short:
            #     val = -999

            dist_all = dist_all + dist
        if dist_all<max_dist:
            data[l,m] = 1000
        else:
            data[l,m] = -1000
            
        # data[l,m] = val

print data
data_flat = np.ndarray.flatten(data)
a = list(np.array(data_flat))
area_dist = a.count(1000)
print area_dist
sdf
remove = []
for k in range(len(lines)):
    for i in range(size):
        if data[i,0] == k:
            remove.append(k)
        if data[0,i] == k:
            remove.append(k)
        if data[i,size-1] == k:
            remove.append(k)
        if data[size-1,i] == k:
            remove.append(k)


remove_list = np.unique(remove)
data_flat = np.ndarray.flatten(data)

print remove_list
a = list(np.array(data_flat))
area = 0
for i in range(len(lines)):
    if i not in remove_list:
        area_tmp = a.count(i)
        if area_tmp>area:
            area = area_tmp
            key = i
            
print area
print key
