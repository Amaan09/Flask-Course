r = 1

arr = [5, 4, 3, 2, 1] 

for _ in range(5):
    arr = (arr[-r:] + arr[:-r]) 
    for val in arr:
        print(val, end=" ")
    print() 