class arr:
    def __init__(self,array):
        self.array =array
        
    def answer(self):
        col = len(self.array[0])
        row = len(self.array)
        newarray =[]
        for i in range(col+1):
            k=i
            j=0
            while j<col and k>=0:
               newarray.append(self.array[k][j])
               k-=1
               j+=1
        for i in range(1,row):
            k=row-1
            j=i
            while j < col and k>=0:
                newarray.append(self.array[k][j])
                k-=1
                j+=1
        return newarray
        
if __name__ == "__main__":
    array = arr([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]])
    ans = array.answer()
    print(ans)