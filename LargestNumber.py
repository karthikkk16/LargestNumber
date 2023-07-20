def largestNumber(array):
    singledigit=[]
    for i in range(len(array)):
        if array[i]>9:
            while array[i]>0:
                singledigit.append(str(array[i]%10))
                array[i]//=10
        else:
            singledigit.append(str(array[i]))
    singledigit.sort(reverse=True)
    return "".join(singledigit)

array=list(map(int, input().split()))
print(largestNumber(array))