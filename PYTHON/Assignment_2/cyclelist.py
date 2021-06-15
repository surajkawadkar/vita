data=[11,22,33,44,55]
n= int(input())
for i in range(n):
    print(data[i:]+data[:i])
