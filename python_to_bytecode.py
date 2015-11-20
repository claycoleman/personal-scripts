#!/usr/bin/env python

import py_compile

# test_list = [1, 2, 3, 4, 5, 6, ['a', 'b', 'c']]
# for n in test_list
#   print n

def name_change(new_name, people):
    count = 0 
    for person in people:
        person['name']=new_name
        print count
        count += 1

test_dict = {'people': [
                    {'name':'Cole', 'age':'23', 'sports':['Baseball', 'Basketball', 'Football Americano']},
                    {'name':'Mike', 'age':'18', 'sports':['Baseball', 'Football Americano']},
                    {'name':'Adam', 'age':'430', 'sports':['Futball',]}
                    ],
                'places' : {'name': 'Bridge', 'type': 'Landmark'}
                
            }
name_change('Big Brother', test_dict['people'])

for people in test_dict['people']:
    print people['name']
#better way to do it below -- maintain dict c
for person in test_dict['people']:
    for k, v in person:
        if k =='name'
            print v




# for key, value in test_dict['people'].items():
    # print key
    # print value


py_compile.compile('python_to_bytecode.py')