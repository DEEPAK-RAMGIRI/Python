# gemeral method 
def general(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def optimized(arr,target):
    left = 0
    right = len(arr) -1
    while left <= right:
        mid = left + (right - left) //2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid +1
            else:
                right = mid - 1
    return -1
            
if __name__ == "__main__":
    # arr = [4,5,6,7,0,1,2]
    # target = 0
    
    # print(general(arr,target))
    # print(optimized(arr,target))
    
    # arr = [4,5,6,7,0,1,2]
    # target = 3
    # print(general(arr,target))
    # print(optimized(arr,target))
    
    arr = [1]
    target = 0
    print(general(arr,target))
    print(optimized(arr,target))
