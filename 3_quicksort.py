
lis1=[21,1,94,67,9,7,3]

def partition(lis, first, last): #[94,1,67],[9,7,3]
    pi = lis[first] #94,9
    low = first + 1 #3,1
    high = last #2,2
    while True:
        while low <= high and lis[high] >= pi:
            high = high - 1
        while low <= high and lis[low] <= pi:
            low = low + 1
        if low <= high:
            lis[low], lis[high] = lis[high], lis[low] #[21,1,67,94,9,7,3]
        else:
            break

    lis[first], lis[high] = lis[high], lis[first] #[67,1,94,21,3,7,9]

    return high
def quick(lis, first, last):
    if first >= last:
        return

    p = partition(lis, first, last) #3,2,2
    quick(lis, first, p-1)
    quick(lis, p+1, last)
quick(lis1,0,len(lis1)-1)
print(lis1)