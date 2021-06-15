list1=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
list2=[]
for i in list1: 
    for element in i:
        list2.append(element)
print(list2)