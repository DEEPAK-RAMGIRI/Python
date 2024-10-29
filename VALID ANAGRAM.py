class ana:
    def __init__(self,string1,string2):
        self.string1 = string1
        self.string2 = string2
    
    def function1(self):
        self.string1=''.join(sorted(self.string1))
        self.string2=''.join(sorted(self.string2))
        return self.string1 == self.string2

    def function2(self):
        alphabets =[0] * 26
        
        for i in self.string1:
            alphabets[ord(i)-ord('a')]+=1
            
        for i in self.string2:
            alphabets[ord(i) - ord('a')] -=1
        
        for i in alphabets:
            if i != 0:
                return False
        return True
        
        
if __name__ == "__main__":
    ana.string1="anagram"
    ana.string2="nagaram"
    # print(ana.function1())
    print(ana.function2())