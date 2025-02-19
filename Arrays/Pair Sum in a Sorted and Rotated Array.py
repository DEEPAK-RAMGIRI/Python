def general(arr,target):
    #Time Complexcity = o(n log n)
    arr.sort()
    left =0
    right = len(arr) -1 
    while left < right:
        if arr[left] + arr [right] == target:
            return [arr[left],arr[right]]
        elif arr[left] + arr[right] > target:
            right-=1
        else:
            left +=1
            
def general2(arr,target):
    #Time Complexcity = O(N)
    seen = set()
    for i in arr:
        if target - i in seen:
            return [i,target-i]
        else:
            seen.add(i)
    # above one is already an optmised one

if __name__ == "__main__":

    arr = [11, 15, 6, 8, 9, 10]
    target = 16
    print(general(arr,target))
    print(general2(arr,target))
    