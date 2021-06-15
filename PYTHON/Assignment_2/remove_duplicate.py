list1=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]==list1[j]:
            list1[j].remove(j)
print(list1)