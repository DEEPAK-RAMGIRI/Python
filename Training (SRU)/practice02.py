# # Output: [[1, 4], [6, 8], [9, 10]]
ar = [[1, 3], [2, 4], [6, 8], [9, 10]]
# ans = []
# start,end = ar[0]
# for i in range(1,len(ar)):
#     if ar[i][0] <= end:
#         end = max(end,ar[i][1])
#     else:
#         ans.append([start,end])
#         start,end  = ar[i]
# ans.append()
# print(ans)
    
    
# don't use above method
# ans = []
# for start,end in ar:
#     if ans and ans[-1][1] >= start:
#         ans[-1][1] = max(end,ans[-1][1])
#     else:
#         ans.append([start,end])
# print(ans   )
        
    

# Find minimum number of merge operations to make an array palindrome
arr = [15, 4, 15]
# arr = [1, 4, 5, 1]
# arr = [11, 14, 15, 99]

i = 0
j = len(arr) - 1
count = 0
while i <= j:
    if arr[i] == arr[j]:
        i+=1
        j-=1
    elif arr[i] > arr[j]:
        j-=1
        arr[j] = arr[j] + arr[j+1]
        count+=1
    else:
        i+=1
        arr[i] = arr[i] + arr[i-1]
        count+=1
print(count)