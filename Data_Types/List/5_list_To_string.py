# Using join Function:
sList = ['Hi', 'There!']
print(sList)
print(' '.join(sList))

nList = [x for x in range(7)]
print(nList)
s = ' '.join(str(i) for i in nList)
print(s)


# Traversal of List Function:
my_string = ''
for x in sList:
    my_string += ' ' + x
print(my_string)


# Using map Function:
aList = ['Hi', 'Eve', '!', 1, 0]
s = ' '.join(map(str, aList))
print(s)


# List Comprehension:
new_List = ['Using', 'List', 'Comprehension', '!']
string = ' '.join([str(item) for item in new_List])
print(string)
