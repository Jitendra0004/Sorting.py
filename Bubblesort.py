def bubblesort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr=[22,11,45,34,223,1,2,23,33,456,43]
bubblesort(arr)
for i in range(len(arr)):
    print(arr[i])