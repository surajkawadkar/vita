list1=[]
size = int(input("size"))
for i in range(size):
    item= int(input("enter number"))
    list1.append(item)
list1.sort()
print("second minimum is",list1[1])