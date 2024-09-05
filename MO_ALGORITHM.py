# way 1 time complexcity is: O(length of arr * length of q)
# space complexcity is: O(1) and that to extra space for the left and right 
def function1(arr,q):
    for i in q:
        left,right=i
        sum=0
        for i in range(left,right+1):
            sum+=arr[i]
        print("the range bettween",i,"is:",sum)
            
arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
Q = [[0, 4], [1, 3], [2, 4]]
function1(arr,Q)