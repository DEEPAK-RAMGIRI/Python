#SLIDNING WINDOW
#Window Size is 3
def function1(a,n):
    for i in range(len(a)-n+1):
        sums=0
        for j in range(i,i+n):
            sums=max(sums,a[j]+sums)
    print(sums)

def function2(a,n):
    sums=sum(a[:n])
    for i in range(len(a)):
        sums=max(sums,sums-a[i-n]+a[i])
    return sums

def longestSubString(b):
    CharSet=set()
    maximum=0
    j=0
    for i in range(len(b)):
        while b[i] in CharSet:
            CharSet.remove(b[j])
            j+=1
        CharSet.add(b[i])
        maximum=max(maximum,i-j+1)
    return maximum
    
        
a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
n=3
# function1(a,n)
print()
# print(function2(a,n))
b="abcabcbb"
print(longestSubString(b))