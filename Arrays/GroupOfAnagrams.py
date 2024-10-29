from collections import defaultdict
class Anagram:
    def __init__(self,string):
        self.string =string
    
    def function1(self):
        result = defaultdict(list)
        for i in self.string:
            sorted_string = ''.join(sorted(i))
            result[sorted_string].append(i)
        return result.values() 
            
if __name__ == "__main__":
    anangram = Anagram(["act","pots","tops","cat","stop","hat"])
    print(anangram.function1())
    
            