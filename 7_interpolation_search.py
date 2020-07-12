def interpolation_search(lis , x):
    pos = (x-lis[0])*(len(lis)-1) // (lis[-1]-lis[0])
    if 0 < pos < (len(lis)):
        if x == lis[pos]:
            print("element found")
            return True
        elif x > lis[pos]:
            interpolation_search(lis[pos:], x)
        else:
            interpolation_search(lis[:pos], x)
    else:
        print("element not found")
        return False


lis = [3, 4, 5, 6, 7, 8, 90, 101]
x = int(input("enter the number you wanna search for: "))
result = interpolation_search(lis, x)