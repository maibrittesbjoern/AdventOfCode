from datetime import datetime
import numpy as np

text_file = open("d4.txt", "r")
lines = text_file.read().split('\n')

data = lines[:-1]

mylist = []
for d in data:
    idx1 = d.find('[')
    idx2 = d.find(']')
    date = d[idx1+1:idx2]
    info = d[idx2+2:]
    mylist.append([date,info])



list_sort = sorted(mylist, key=lambda x: x[0])

for i in list_sort:
    print i

mydict = {}


for k,(i,j) in enumerate(list_sort):
    if 'Guard' in j:
        guard = j.split()[1]
        if guard not in mydict:
            mydict[guard] = []
    while 'Guard' not in j:
        if 'fall' in j:
            tstamp1 = int(list_sort[k][0][-2:])
            tstamp2 = int(list_sort[k+1][0][-2:])
            print tstamp1, tstamp2
            sleep = np.arange(tstamp1,tstamp2,1)
            mydict[guard].extend(sleep)

        break





max_sleep = -1
for key,val in mydict.iteritems():
    if len(val)>max_sleep:
        max_sleep = len(val)
        max_key = key


print max_key
print max_sleep
# print mydict[max_key].count(39)
# sdf

def most_common(lst):
    ret = max(set(lst), key=lst.count)
    return ret,lst.count(ret)

minute,count = most_common(mydict[max_key])
print minute,count
print int(max_key[1:])*minute


max_occur = -1
for key,val in mydict.iteritems():
    if len(val)>0:
        minute,count = most_common(val)
        if count > max_occur:
            print count
            max_occur = count
            max_ckey = key
            max_cminute = minute


print 'max_count', max_occur
print 'mak_ckey', max_ckey
print 'mak_cminute', max_cminute
print  int(max_ckey[1:]) * max_cminute

