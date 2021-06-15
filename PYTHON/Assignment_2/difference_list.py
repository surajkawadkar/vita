list1 = [1,3,5,7,9]
list2 = [1,2,4,6,7]
print(list(set(list1) - set(list2)) + list(set(list2) - set(list1)))