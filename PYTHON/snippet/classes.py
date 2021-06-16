# total female in the list of all entries
class Human:
    population=0#class memeber
    def __init__(self,n,g):
        Human.population+=1   #class member can be accessd with only clasNname
        print("one human created---now total humans:",Human.population)
        self.name=n
        self.gender=g
    def __del__(self):   
        print("R.I.P--->",self.name)
    def __str__(self):
        return "i am "+self.name+" and i am a "+self.gender#only string 
hlist=[]
while True:
    name=input("Enter Name:")
    gender=input("Enter Gender:")
    if name=='' or gender=='':
        break
    
    hlist.append(Human(name,gender))

'''for i in hlist:
    print(i)
'''
for i in hlist:
    if i.gender=='female':
        print(i)