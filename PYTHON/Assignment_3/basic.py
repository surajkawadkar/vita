# s='Hello#81@21349'
s='jflds59733fds'
digit=[]
for i in s:
    if i in '0123456789':
        digit.append(i)
# digit=set(digit)
digit=list(set(digit))
digit.sort()
print(digit)

even=[2,4,6,8,0]
for i in even:
        
    if str(i)  not in digit:
        print("-1")