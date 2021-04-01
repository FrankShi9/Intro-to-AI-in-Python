tuple1 = ('d','c','m','k') #immutable & ordered
print(sorted("h e llo".split(), key=str.lower))#strings are immutable
print(sorted(b'h e llo'.split()))
print(sorted(tuple1))
list1 = [5,2,4,3,1] #ordered
print(sorted(list1,reverse=True))
print(sorted(list1))

dict1 = {'name':'Frank',
         'gender':'M',
         'age':'21'
         }
print(sorted(dict1, key=str.lower))

set1 = {'d','c','m','k'}
print(sorted(set1))

list2 = [1,3,'k']
print(list2)
tuple2 = (2,3,'k')
print(tuple2)
set2 = {1,'k'}
print(set2)