from collections import Counter
class Day12:
    def __init__(self,no):
        self.no = no
    
    def perfect_no(self):
        values = []
        for i in range(1,self.no):
            if not self.no % i:
                values.append(i)
        print(self.no == sum(values))
        
    def armstrong_no(self):
        no = str(self.no)
        length = len(no)
        sums = 0
        for i in no:
            sums += int(i)**length
        print(self.no == sums)
        
    def strong_no(self):
        sums =0
        no = str(self.no)
        for i in no:
            value = int(i)
            fact = 1
            while  value > 0:
                fact *= value
                value -=1
            sums += fact
        print(sums == self.no)
        
    def frequency(self,string):
        print(Counter(string))
                
        
obj = Day12(3)
# obj.perfect_no()
# obj.armstrong_no()
# obj.strong_no()
obj.frequency("aaabbbduhdiiii")
