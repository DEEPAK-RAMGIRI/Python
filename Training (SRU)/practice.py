# def minimum_cost(N, M1, P1, M2, P2):
   
#     cost = float('inf')
#     for k1 in range(N // M1 + 1):
#         A = k1 * M1
#         remaining = N - A
#         if remaining % M2 == 0:
#             k2 = remaining // M2
#             total = k1 * P1 + k2 * P2
#             cost = min(cost, total)

#     for k2 in range(N // M2 + 1):
#         B = k2 * M2
#         remaining = N - B
#         if remaining % M1 == 0:
#             k1 = remaining // M1
#             total = k2 * P2 + k1 * P1
#             cost = min(cost, total)
    
#     return cost

# N = int(input()) 
# M1, P1 = map(int, input().split())  
# M2, P2 = map(int, input().split())  

# print(minimum_cost(N, M1, P1, M2, P2))

n = int(input())
string = input()
print(sum(map(int, string[1:-1])))