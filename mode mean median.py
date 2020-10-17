import statistics
l=[5,2,4,3,1,1]
m=[12,5,6,7,8,9]
print(l)
def mean(x):
    return sum(l)/len(l)
def median(x):
    x.sort()
    return statistics.median(x)
def mode(x):
    return statistics.mode(x)
print('mean is',mean(m))
print('median is',median(m))
print('mode is',mode(m))
print('mean is',mean(l))
print('median is',median(l))
print('mode is',mode(l))




      
