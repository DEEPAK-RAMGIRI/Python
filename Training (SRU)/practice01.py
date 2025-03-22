# Practice Problems 
# inputs = input()
# freq = dict()
# for i in inputs:
#     if i.isalpha():
#         freq[i] = freq.get(i,0)+1
# # vvvvw?vxwy?
# count = 0
# for i in freq.values():
#     if i >= 2:
#         count+= (i >> 1) + 1 if i & 1 else i >> 1
#     else:
#         count+=i
# print(count)


mat = [[1,5,6],[0,4,9],[8,7,8]]
row = len(mat)
# col = len(mat[0])
# r = 0
# while r < row:
#     for i in range(col):
#         print(mat[r][i])
#     r+=1
#     if r < row:
#         for i in range(col-1,-1,-1):
#             print(mat[r][i])
#         r+=1
     
for i in range(row):
    if not i & 1:
        print(mat[i])
    else:
        print(mat[i][::-1])