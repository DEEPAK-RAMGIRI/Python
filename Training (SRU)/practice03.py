from collections import Counter
arr = [3,10,3,10,21,9,6]
# arr =  list(map(int,input().split()))
map = dict()
for i in arr:
    map[i] = map.get(i,0)+1
# print([i for i in map if map[i]==1])


# arr = [100,200,400,800,1000]
# b = [4,2,0,6,10,0]
# m = len(arr)
# for i in b:
#     print(arr[i] if i< m else -1,end=" ")
    
    
# arr = [4,4,4,4,1,1,7]
# arr = [1,2,3,1,2,3]
# maps = Counter(arr)
# count = 0
# for i in maps.values():
#         count += (i // 2) 
# print(count)

altitude = [-5,1,5,0,-7]
maxi = sums = 0
for i in altitude:
    sums += i 
    maxi = max(maxi,sums)
print(maxi)