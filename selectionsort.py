a = [12,56,78,99,65,3,55]
for i in range(len(a)):
    minimum = i
    for j in range(i+1,len(a)):
        if a[minimum] > a[j]:
            minimum = j 
    a[i],a[minimum] = a[minimum],a[i]
print('sorted elements in selection sort')
for i in range(len(a)):
    print(a[i])