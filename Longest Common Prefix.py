def function1(a):
    a.sort()
    left =a[0]
    right=a[len(a)-1]
    idx=0
    while idx< len(left) and  idx <=len(right):
        if left[idx] != right[idx]:
            break
        idx+=1
    return left[0:idx]
a=["flower","flight","flow"]
b= ["dog","racecar","car"]
print(function1(a))
# print(function1(b))