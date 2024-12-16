class password:
    def __init__(self,string):
        
        self.string = string
        
    
    def Encode(self):
        result=""
        for i in self.string:
            result += str(len(self.string)) + "#" + i
        return result
    
    def Decode(self,passwords):
        res = []
        i = 0
        
        while i < len(passwords):
            j = i
            while passwords[j] != "#":
                j+=1
            length = int(passwords[i:j])
            i = j+1
            res.append(passwords[i:i+length])
            i += length
        return res

if __name__ == "__main__":
    obj1 = password(["leet","code","love","you"])  
    ans = obj1.Encode()
    print(obj1.Decode(ans))      
                
                  