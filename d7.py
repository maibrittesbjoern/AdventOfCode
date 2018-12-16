from datetime import datetime
import numpy as np

text_file = open("d7.txt", "r")
lines = text_file.read().split('\n')[:-1]

order = []
            


# for k,i in enumerate(lines):
#     data = i.split()
#     first = data[1]
#     last = data[7]
#     order.append((first,last))


# instructions = np.array(order)
# unique = list(np.unique(np.ndarray.flatten(instructions)))
# print unique


# complete = []

# inst_up = list(order)
# ready_sort = []
# length = []
# while inst_up:
#     ready = []
#     for i in unique:
#         if i not in [y for x,y in inst_up]:
#             ready.append(i)

#     ready_sort = sorted(set(ready))

#     print 'ready_sort',ready_sort
#     print '##########'

#     complete.append(ready_sort[0])
#     print 'complete',complete
#     inst_up = [i for i in inst_up if ready_sort[0] != i[0]]

#     unique.remove(ready_sort[0])
#     print inst_up

# complete.extend(unique)
# print ''.join(complete)






for k,i in enumerate(lines):
    data = i.split()
    first = data[1]
    last = data[7]
    order.append((first,last))


# List of tuples of instructions. A before B.
instructions = np.array(order)

# Find a list of unique tasks to be done.
unique = list(np.unique(np.ndarray.flatten(instructions)))

print instructions
print unique


inst_up = list(order)
ready_sort = []
length = []

workers = 5

import string
alpha = string.ascii_uppercase
alpha_time = range(1,len(alpha)+1,1)
at_dict = {}
for k,s in zip(alpha,alpha_time):
    at_dict[k] = s+60
    # at_dict[k] = s
print at_dict


active_tasks = {}

global_clock = 0

def worker_available():
    return len(active_tasks)<workers
        
def perform_first(available,inst_up):
    for i in range(len(available)):
        if worker_available():
            task = available.pop(0)
            time = at_dict[task]
            active_tasks[task] = time
        else:
            break

    done = advance_time()
    inst_up = [i for i in inst_up if i[0] not in done]
    return done, inst_up


def advance_time():
    global active_tasks, global_clock
    m = min(active_tasks.values())
    done = [i for i in active_tasks.keys() if active_tasks[i] == m]
    print 'done',done
    print 'at',active_tasks
    for key in done:
        active_tasks.pop(key)

    print active_tasks
    active_tasks = dict((k,v-m) for k,v in active_tasks.items())
    global_clock += m
    return done


completed = []
while inst_up:
    
    # Find tasks ready to do, by checking for a given task in second column
    ready = []    
    for i in unique:
        if i not in [y for x,y in inst_up]:
            ready.append(i)

    # Find the unique tasks and sort them alphabetically
    ready_sort = sorted(set(ready)-set(completed))

    print '-------',ready_sort

    ready_sort = [i for i in ready_sort if i not in active_tasks.keys()]
    done, inst_up = perform_first(ready_sort, inst_up)
    completed.extend(done)
    print inst_up


            
missing = [x for x in unique if x not in completed]
print missing

completed.extend(missing)
total_time = global_clock+at_dict[missing[0]]


    



# Print the final order of tasks
print ''.join(completed), total_time
