l1=[1,2,3,4,5]
list1=set(l1)
print(list1)
l2=[2,5,6,4,8,9]
list2=set(l2)
print(list2)
def union(list1,list2):
    list_union=list1.union(list2)
    return list_union
def intersection(list1,list2):
    list_intersect=list1.intersection(list2)
    return list_intersect
def difference(list1,list2):
    list_diff=list1.difference(list2)
    return list_diff
print('union is',union(list1,list2))
print('intersection is',intersection(list1,list2))
print('list1 diff list2 is',difference(list1,list2))









