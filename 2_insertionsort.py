
lis=[21,1,94,67,9,7,3]
def insertion(lis):
    for i in range(1,len(lis)):
        temp=lis[i]
        preindex=i-1
        while preindex>=0 and lis[preindex]>temp:
            lis[preindex+1]=lis[preindex]
            preindex=preindex-1
        lis[preindex+1]=temp
    print(lis)
insertion(lis)