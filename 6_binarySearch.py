def binary_search(lis , x):
    mid = len(lis) // 2
    if mid > 0:
        if x == lis[mid]:
            print("element found")
            return True
        elif x > lis[mid]:
            binary_search(lis[mid:], x)
        else:
            binary_search(lis[:mid], x)
    else:
        print("element not found")
        return False


lis = [3, 4, 5, 6, 7, 8, 90, 101]
x = int(input("enter the number you wanna search for: "))
result = binary_search(lis, x)

#why does it return NONE here?
