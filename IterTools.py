from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement
from itertools import groupby

data = input()
for k, g in groupby(data, int):
    print((len(list(g)), k), end=" ")

A,B = input().split() 
[print(''.join(x)) for x in combinations_with_replacement(sorted(A), int(B))]

A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(* product(A,B))

A,B= input().split()
for i in range(1,int(B)+1):
    for j in combinations(sorted(A),i):
        print(''.join(j))
