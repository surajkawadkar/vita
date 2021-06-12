deposit=5000
total=0.0
for year in range(1,11):
    temp=0
    temp=deposit+(deposit*10*year)/100
    total+=temp
print(total)