import numpy as np

# text_file = open('d13ex.txt', 'r')
# text_file = open('d13ex2.txt', 'r')
text_file = open('d13.txt', 'r')
lines = text_file.read().split('\n')

data = [i for i in lines[:-1]]

for i in data:
    print i
    
xlength = len(data[0])
ylength = len(data)

array = np.chararray((ylength,xlength))
print np.shape(array)

location = {}
direction = {}

rules = {
    '>':'-',
    '<':'-',
    '^':'|',
    'v':'|',
    }

car = 0
for k,i in enumerate(data):
    for l,j in enumerate([x for x in i]):
        array[k,l] = j
        if j in ['>', '<', '^', 'v']:
            location[car] = [[k,l], j, 0]
            array[k,l] = rules[j]
            car +=1


print location

cars = range(len(location))

directions = {
    'v':[1,0],
    '^':[-1,0],
    '>':[0,1],
    '<':[0,-1],
    'v/':'<',
    '^/':'>',
    '>/':'^',
    '</':'v',
    'v\\':'>',
    '^\\':'<',
    '>\\':'v',
    '<\\':'^',
    'v|':'v',
    '^|':'^',
    '>-':'>',
    '<-':'<',
    }

turn_dir = ['^','>','v','<']*1000
cars_remove_all = []
cars_remove = []
i = 0
while i>=0:
    values = []
    for key, value in location.iteritems():
        values.append((key,list(value[0])))

    cars_sorted = []
    for car,val in sorted(values,key=lambda x:x[1]):
        cars_sorted.append(car)
    for car in cars_sorted:
        if car not in cars_remove_all:
            loc_car = list(location[car][0])
            loc_keys = location.keys()
            loc_keys.remove(car)
            loc_others = [list(location[k][0]) for k in loc_keys]

            route_info = array[loc_car[0],loc_car[1]]
            if route_info in ['-','|']:
                location[car][0] = np.array(directions[directions[location[car][1]+route_info]])+np.array(loc_car)
            elif route_info in ['/', '\\']:
                location[car][0] = np.array(directions[directions[location[car][1]+route_info]])+np.array(loc_car)
                location[car][1] = directions[location[car][1]+route_info]
            else:
                turns = location[car][2]
                if turns % 3 == 0:
                    val = location[car][1]
                    location[car][1] = turn_dir[turn_dir.index(val)-1]
                    val = location[car][1]
                    location[car][0] = np.array(directions[val])+np.array(loc_car)
                elif turns % 3 == 1:
                    val = location[car][1]
                    location[car][0] = np.array(directions[val])+np.array(loc_car)
                    location[car][1] = val
                elif turns % 3 == 2:
                    val = location[car][1]
                    location[car][1] = turn_dir[turn_dir.index(val)+1]
                    val = location[car][1]
                    location[car][0] = np.array(directions[val])+np.array(loc_car)

                turns+=1
                location[car][2] = turns

            i+=1
            if loc_car in loc_others:
                # print 'loc',location
                # print 'loc_car',loc_car
                # print 'loc_others',loc_others
                print 'CRASH', loc_car[1],loc_car[0]
                cars = location.keys()
                cars_remove = [c for c in cars if list(location[c][0])==loc_car]+[car]
                cars_remove_all.extend(cars_remove)
                print 'cars_remove',cars_remove
                for c in cars_remove:
                    del location[c]

                if len(cars) == len(cars_remove):
                    sdf
            if len(cars) == len(cars_remove)+1:
                for c in cars:
                    if c not in cars_remove:
                        print 'REMAINING CAR',location[c][0][1],location[c][0][0]
                        sdf


# while i>=0:
#     print 'i', i
#     values = []
#     for key, value in location.iteritems():
#         values.append((key,list(value[0])))

#     print values
#     cars_sorted = []
#     for car,val in sorted(values,key=lambda x:x[1]):
#         cars_sorted.append(car)
#     print cars_sorted
#     for car in cars_sorted:
#         print 'car',car
#         loc_car = list(location[car][0])
#         loc_keys = location.keys()
#         loc_keys.remove(car)
#         loc_others = [list(location[k][0]) for k in loc_keys]
#         print 'loc_car',loc_car
#         print 'loc_others', loc_others
#         if loc_car not in loc_others:
#             route_info = array[loc_car[0],loc_car[1]]
#             print 'route info',route_info
#             if route_info in turn_dir:
#                 location[car][0] = np.array(directions[route_info])+np.array(loc_car)
#                 print 'loc_car', location[car][0]
#             else:
#                 if route_info in ['-','|']:
#                     location[car][0] = np.array(directions[directions[location[car][1]+route_info]])+np.array(loc_car)
#                     print 'loc_car',location[car][0]
#                 elif route_info in ['/', '\\']:
#                     location[car][0] = np.array(directions[directions[location[car][1]+route_info]])+np.array(loc_car)
#                     location[car][1] = directions[location[car][1]+route_info]
#                     print 'loc_car', location[car][0]
#                 else:
#                     turns = location[car][2]
#                     if turns in range(0,100,3):
#                         print 'turns',turns
#                         val = location[car][1]
#                         print 'val',val
#                         location[car][1] = turn_dir[turn_dir.index(val)-1]
#                         val = location[car][1]
#                         print 'val',val
#                         location[car][0] = np.array(directions[val])+np.array(loc_car)
#                         print 'loc_car',location[car][0]
#                     elif turns in range(1,100,3):
#                         print turns
#                         val = location[car][1]
#                         location[car][0] = np.array(directions[val])+np.array(loc_car)                
#                         location[car][1] = val
#                         print 'loc_car',location[car][0]
#                     elif turns in range(2,100,3):
#                         print 'turns',turns
#                         val = location[car][1]
#                         print 'val',val
#                         location[car][1] = turn_dir[turn_dir.index(val)+1]
#                         val = location[car][1]
#                         print 'val',val
#                         location[car][0] = np.array(directions[val])+np.array(loc_car)
#                         print 'loc_car',location[car][0]

#                     turns+=1
#                     location[car][2] = turns
                    
#             i+=1
#         else:
#             print 'DONE', loc_car[1],loc_car[0]
#             i = -1


        

        
            
