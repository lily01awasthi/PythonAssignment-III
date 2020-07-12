lis=[3,4,6,7,9,2,34,90,67]
x=int(input("enter the element you wanna search for: "))

def linear_search(lis,x):
    for i in range(len(lis)):
        if(lis[i]==x):
            return x
    return False
if linear_search(lis,x):
    print("element found")
else:
    print("element not found!")
