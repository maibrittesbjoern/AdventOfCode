import numpy as np
import collections

### Example
# init = '#..#.#..##......###...###'

init = '#..######..#....#####..###.##..#######.####...####.##..#....#.##.....########.#...#.####........#.#.'


print init
pad_n = 10
pad = 150

pot_status = {}
for k,i in enumerate(init):
    pot_status[k] = i

pad_pots = range(-pad_n,0)+range(len(init),len(init)+pad)
for k in pad_pots:
    pot_status[k] = '.'


print pot_status


rules = {}
# text_file = open('d12ex.txt', 'r')
text_file = open('d12.txt', 'r')
lines = text_file.read().split('\n')[:-1]
for i in lines:
    key = i[0:5]
    val = i[-1]
    rules[key] = val

print rules

pot_update = {}


for gen in range(140):
    # print gen
    status_full_init = ''
    for s in range(-pad_n,len(init)+pad):
        status_full_init = status_full_init + pot_status[s]

    # print gen, status_full_init
    # print gen
    status_full = ''
    for pot in range(-pad_n+2,len(init)+pad-2):
        status = pot_status[pot-2]+pot_status[pot-1]+pot_status[pot]+pot_status[pot+1]+pot_status[pot+2]
        if status in rules.keys():
            pot_update[pot] = rules[status]
            # print pot, rules[status]
        else:
            pot_update[pot] = '.'
            # print pot, '.'

    status_full = '..'
    for s in range(-pad_n+2,len(init)+pad-2):
        status_full = status_full + pot_update[s]
    status_full = status_full + '..'

    # print status_full
    pot_status = pot_update
    pot_status[-pad_n] = '.'
    pot_status[-pad_n+1] = '.'
    pot_status[len(init)+pad-2] = '.'
    pot_status[len(init)+pad-1] = '.'
    pot_update = {}
    pots_with_plants = [key  for (key, value) in pot_status.items() if value == '#']
    # print pots_with_plants
    # print sum(pots_with_plants)
    
print gen
print pots_with_plants
left = 50000000000-gen-1
updated = [x+left for x in pots_with_plants]
print updated
print sum(updated)

