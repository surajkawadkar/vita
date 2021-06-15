
list1=[(2,5),(1,2),(4,4),(2,3),(2,1)]
newlist=[]
# newlist= sorted(list1,reverse='True')
# newlist=list1.sort(reverse=True)
for i in range(len(list1)-1,-1,-1):
    newlist.append(list1[i])
    
print(newlist)