students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# for idx in range(len(students)):
    # print(0,1).format(students(idx))
    # print(0,1).format(students(idx))

# for idx, item in enumerate(students):
    # print(0,1).format(item)

# for idx, item in zip(range(len(students))students):

# for i in range(len(students)):
#     for key in students[i]:
#         print students[i][key]
#     print ('\n')
for idx in range(len(students)):
    print students[idx]['first_name'] + " " + students[idx]['last_name']



#part2


users={
'Students':[
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ],
}
# for key in users:
#         print key
#         for i in range(len(users[key[i]])):
#             print i+1
#             sum = 0
#             for k in users[key][i]:
#                 print users[key][i][k]
#                 sum += len(users[key][i][k])
#             print sum,
#             print('\n')

for key in users:
    count = 1
    print key
    for value in users[key]:
        first_name = value['first_name']
        last_name = value['last_name']
        length = len(first_name) + len(last_name)
        print "{} - {} {} - {}".format(count, first_name, last_name, length)
        count += 1
