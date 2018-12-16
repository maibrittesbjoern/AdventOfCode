text_file = open('d8ex.txt', 'r')
lines = text_file.read().split()

data = [int(i) for i in lines]

#### Additional test example ###
data = [2, 3, 1, 3, 0, 1, 90, 10, 11, 12, 2, 1, 0, 1, 99, 1, 2, 0, 3, 20, 21, 22, 30, 31, 2, 1, 1, 2]
#       A-----------------------------------------------------------
#             B-------------------------- C-----------------
#                   D-------                    E-------
# metadata = 90+99+10+11+12+2+1+1+2
# print metadata
# total = 138+90 = 228
# print total
##################################
print data


### PART 1 - solution 1

# metas = []
# def remove_children(data):
#     global metas
#     global c
#     while len(data)>1:
#         for i in range(0,len(data),2):
#             node = data[i]
#             if node == 0:
#                 meta = data[i+1]
#                 idx0 = i
#                 idx1 = i+1+meta
#                 metas.extend(data[i+2:i+2+meta])
#                 data[i-2] += -1
#                 data = data[:idx0]+data[idx1+1:]
#                 break
#             else:
#                 continue
#     return metas, data

# metas,data = remove_children(data)
# print sum(metas)

### PART 1 - solution 2
# i = 0
# metas = []
# count = 0
# def get_meta(data,i):
#     global metas
#     global count
#     node = data[i]
#     meta_parent = data[i+1]
#     count+=meta_parent
#     while i<(len(data)-2-data[1]):
#         for n in range(node):
#             if count == 0:
#                 break

#             i+=2
#             if data[i] == 0:
#                 meta = data[i+1]
#                 metas.extend(data[i+2:i+2+meta])
#                 i+=meta
#             else:
#                 print 'recursive'
#                 metas, i = get_meta(data,i)
#         break
#     metas.extend(data[i+2:i+2+meta_parent])
#     i+=meta_parent
#     count-=meta_parent
#     return metas,i


# metas, i = get_meta(data,i)
# print metas
# print sum(metas)


#### PART 2
i = 0
metas = []
count = 0
level=0
def get_meta(data,i):
    global metas
    global count
    global level
    node = data[i]
    meta_parent = data[i+1]
    count+=meta_parent
    while i<(len(data)-2-data[1]):
        level +=1
        for n in range(node):
            if count == 0:
                break

            i+=2
            if data[i] == 0:
                meta = data[i+1]
                node_info = data[i]
                metas.append((level,node_info,data[i+2:i+2+meta]))
                i+=meta
            else:
                metas, i = get_meta(data,i)

        break
    node_info = node
    level -=1
    metas.append((level,node_info,data[i+2:i+2+meta_parent]))
    i+=meta_parent
    count-=meta_parent
    return metas,i


metas, i = get_meta(data,i)
print
for i in sorted(metas):
    print i
print

metass = sorted(metas)
print 'test'
total = []

def is_node_in_meta(node_no, m, node_in_meta=False):
    if node_no == m:
        node_in_meta = True
    return node_in_meta

def get_k_total(metass,k):
    global total
    while k<len(metass):
        node = metass[k][1]
        if node == 0:
            k+=1
            break
        meta = metass[k][2]
        for m in meta:
            for n in range(node):
                node_no = n+1
                node_child = metass[k+node_no][1]
                meta_child = metass[k+node_no][2]
                if node_child>0:
                    k,total = get_k_total(metass,k)
                    k+=1

                if is_node_in_meta(node_no, m):
                        total.extend(meta_child)
                        print 'total', total
        k+=1
    return k, total

k = 0
k, total = get_k_total(metass,k)


print 'total',total
sfsdf

i = 0
metas = []
metas_parent = []
metas_total = []
count = 0

def get_meta(data,i):
    global metas
    global count
    global metas_parent
    node = data[i]
    meta_parent = data[i+1]
    count+=meta_parent
    while i<(len(data)-2-data[1]):
        for n in range(node):
            if count == 0:
                break

            i+=2
            if data[i] == 0:
                meta = data[i+1]
                # metas.extend(data[i+2:i+2+meta])
                metas = data[i+2:i+2+meta]
                i+=meta
            else:
                # print 'recursive'
                metas, i = get_meta(data,i)

            print 'metas_parent', metas_parent
            print 'meta_parent', meta_parent
            print 'node', node
            print 'n', n
            for p in metas_parent:
                if p == n+1:
                    print 'add'
                    metas_total.extend(metas)
                else:
                    metas = []
        break

    print 'metas_total', metas_total
    print '#############################'

    metas.extend(data[i+2:i+2+meta_parent])
    metas_parent = data[i+2:i+2+meta_parent]

    # for n in range(node):
    #     for p in metas_parent:
    #         if p == n+1:
    #             print 'add'
    #             metas_total.extend(metas)
    #         else:
    #             metas = []


    i+=meta_parent
    count-=meta_parent
    return metas,i



metas, i = get_meta(data,i)
print sum(metas_total)



### 81828 too high
