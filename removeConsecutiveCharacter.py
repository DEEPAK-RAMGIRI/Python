def function1(a):
    b=''
    b+=a[0]
    for i in range(1,len(a)):
        if a[i] != a[i-1]:
            b+=a[i]
    return b
a="aabbabbbabb";
print(function1(a))