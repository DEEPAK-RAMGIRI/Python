#Finding the majority of the  ocuurence of the element in the array
class arr:
    def __init__(self,array):
        self.array=array
    def BruteForce(self):
        for i in self.array:
            count=0
            for j in self.array:
                if i == j:
                    count+=1
            if count > len(self.array) // 2:
                return i
        return -1
            
if __name__ == "__main__":
    array = arr([3,2,3])
    print(array.BruteForce())
    