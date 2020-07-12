def merge_sor(lis):
    if 1<len(lis):
        mid=len(lis)//2
        left=lis[:mid]
        right=lis[mid:]
        merge_sor(left)
        merge_sor(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                lis[k]=left[i]
                i+=1
            else:
                lis[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            lis[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            lis[k]=right[j]
            j+=1
            k+=1
    return lis

lis=[2,5,3,9,7,86,54,32,53]
newlis=merge_sor(lis)
print(newlis)

