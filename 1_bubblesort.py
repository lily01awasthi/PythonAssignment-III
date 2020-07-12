"""Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order."""
lis=[21,1,94,67,9,7,3]
def bubble(lis):
    for j in range(len(lis)):
        for i in range(len(lis)-j-1):
            if(lis[i]>lis[i+1]):
                lis[i],lis[i+1]=lis[i+1],lis[i]
    return lis
print(bubble(lis))