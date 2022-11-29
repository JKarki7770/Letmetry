from copy import deepcopy
l1 = [ 10, 'a', [1,2] ]
l2 = list(l1) #create a *shallow* copy of l1
l3 = deepcopy(l1) #create a *deep* copy of l1
l2[2] += [3,4]
l3[2] += [5,6]
#what does this print?
print(l1)
print(l2)
print(l3)