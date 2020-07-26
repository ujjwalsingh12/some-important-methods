class LISTSET:
    #this function is defined for y = f(x) such that x corresponds to y and vice versa in this the list doesnot have a repeated valuee
    def __init__(self,domain=set()):
        self.domain = domain
        self.List = []
        
    def append(self,val):
        if(val in self.domain and val not in self.List):
            self.List.append(val)
        else:
            print('append error',val)
    def insert(self,val,pos):
        if(val in self.domain and val not in self.List):
            self.List.insert(val,pos)
        else:
            print('insert error',val,pos)
    def __len__(self):
        return len(self.List)
    def __repr__(self):
        return str(self.List)
    def __add__(self,other):
        if(other is listset):
            self.domain = self.domain.union(other.domain)
            self.List = self.List + other.List
        else:
            print('add error',other)
    def remove(self,val):
        if(val in self.List):
            self.List.remove(val)
        else:
            print('remove error',val)
    def pop(self,ind):
        if(ind < len(self.List)):
            self.List.pop(ind)
        else:
            print('pop error',ind)
    def iter_domain(self): #it iterates over the domain of the list rather than the list itself
        return self.iter('domain')
    def iter_unfilled(self): #it iterates over the domain of the list rather than the list itself
        return self.iter('unfilled')
    def iter_List(self):
        return iter(self,'List')
    def iter(self,name):
        it = None
        if(name=='domain'):
            it = self.domain
        if(name=='unfilled'):
            it = self.domain-set(self.List)
        if(name=='List'):
            it = self.List
        for i in it:
            yield i
                    
class relation:
    def __init__(self,X=[],Y=[]):
        if(type(X) is LISTSET):
            self.X = X
        elif(type(X) is list):
            self.X = LISTSET(X)
        else:
            print('wrong X',X)
        if(type(Y) is LISTSET):
            self.Y = Y
        elif(type(Y) is list):
            self.Y = LISTSET(Y)
        else:
            print('wrong Y',Y)
    def relationVerify(self):
        if(len(self.X)!=len(self.Y)):
            return False
        return True
    def append(self,*args):
        if(len(args)==2):
            self.X.append(args[0])
            self.Y.append(args[1])
        else:
            print('append arguments count mismatch')
    def insert(self,*args):
        if(len(args)==2):
            self.X.insert(args[0])
            self.Y.insert(args[1])
        else:
            print('insert arguments count mismatch')
    def remove(self,val,tag):
        if(tag=='X'):
            ind = self.X.List.index(val)
            self.X.remove(val)
            self.Y.pop(ind)
        if(tag=='Y'):
            ind = self.Y.List.index(val)
            self.Y.remove(val)
            self.X.pop(ind)
    def pop(self,ind):
        self.X.pop(ind)
        self.Y.pop(ind)
    def __repr__(self):
        r = ",".join(map(lambda a:"-".join([str(a[0]),str(a[1])]),zip(self.X.List,self.Y.List)))
        return r
    def iter_domain(self): #it iterates over the domain of the list rather than the list itself
        return zip(self.X.iter('domain'),self.Y.iter('domain'))
    def iter_unfilled(self): #it iterates over the domain of the list rather than the list itself
        return zip(self.X.iter('unfilled'),self.Y.iter('unfilled'))
    def iter_List(self):
        return zip(self.X.iter('List'),self.Y.iter('List'))
    
        
#for testing
NUMBER_OF_CARS = 10
slots = LISTSET(set(range(NUMBER_OF_CARS)))
slots.append(4)
slots.append(5)
print(slots)
print(type(slots.iter_unfilled()))
for i in slots.iter_unfilled():
    print(i)
slots.append(4)
print(slots)
slots.pop(1)
print(slots)
g = relation([1,2,3],[1,2,3])
g.append(1,1)
g.append(2,3)
for i in g.iter_List():
    print(i)
