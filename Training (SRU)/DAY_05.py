from collections import Counter

class Day05:
    a =10
    
    def __init__(self,list1):
        self.list1 = list1
        
    def length(self):
        return len(self.list1)
    
    #finding count duplicate which is greater than n//2 
    def find_dup_in_list(self):
        n = self.length()
        for i in list1:
            return (i if self.list1.count(i) >= n//2 else 0)
        
    def rotate_left_array(self):
        n = int(input())
        # k=self.length()
        
        # while n >= (k-1):
        #     n -= k
        
        # ans =[]
        # ans.extend(self.list1[n:])
        # ans.extend(self.list1[:n])
        # print(ans)
        
        for _ in range(n):
            self.list1.append(self.list1.pop(0))
        
        print(self.list1)
    
    def longest_prefix(self,string):
        # count = 0
        # mini = float('inf')
        # for i in string:
        #     if len(i) < mini:
        #         mini = len(i)
        #         prefix = i
        # string.remove(prefix)
        # prefix = list(prefix)
        
        # for i in range(len(string)):
        #     first = list(string[i])
        #     for j in range(len(prefix)):
        #         if prefix[j] == first[j]:
        #             count+=1
        # print(''.join(prefix[:count//len(string)]) if count > 0 else "" )
       
       
       # better  use these one :)
       #time complexcirt is O(n*m) may be 
        prefix = string[0]
        for i in string:
            while prefix and prefix != i[:len(prefix)]:
                prefix = prefix[:-1]
        print(prefix)
                
    def anagram(self,string1,string2):
        alphabets = [0]*26
        
        for i in string1: 
            alphabets[ord(i) - ord('a')]+=1
        
        for i in string2:
            alphabets[ord(i) - ord('a')] -=1
            
        print(True if all(i == 0 for i in alphabets) else False)
        
    # sort string by max count and after that print in order which are same values
    
    def max_count_ord_string(self,string):
        
        alphabets = [0]*26
        for i in string:
            alphabets[ord(i) - ord('a')]+=1
        
        ans = []
        value = max(alphabets)
        
        while value > 1:
            ans.append(chr(alphabets.index(value) + ord('a')))
            alphabets[alphabets.index(value)] = 0
            value =max(alphabets)
        
        for i in range(len(alphabets)):
            if alphabets[i] == 1:
                ans.append(chr(i + ord('a')))
        print(ans)
        
        #(or) Method 02:
        
        alphabets = Counter(string)
        sorted_alphabets = sorted(alphabets.items(),key= lambda x:(-x[1],x[0]))
        print(sorted_alphabets)
        
    @classmethod
    def class_method(cls):
        print(cls.a)
        
    @classmethod
    def class_modify(cls,num):
        cls.a= num
        print(cls.a)
        
    def rotate_string(self,input,goal):
        
        #method 01
        # flag =False
        # for i in range(len(input)):
        #     input = input[1:] + input[0]
        #     if input == goal:
        #         flag =True
        #         break
        # print(True if flag else False)
        
        #method 2
        print(True if goal in input+input else False )
        
        
    def isomorphic_string(self,s1,s2):
        ans = dict()
        
        for i,j in zip(s1,s2):
            if i in ans:
                if ans[i] != j:
                    return False
            else:
                if j in ans.values():
                    return False
                
                ans[i] = j
        return True
    
    
 

list1 = [1,2,3,4,5,67,37]
# list1 = [1,1,1,2,3]
obj = Day05(list1)
# print(obj.find_dup_in_list())
# obj.rotate_left_array()
# string_list =['flower','fly','flow','flight'] #list(input().split())
# string_list = ["dog","eat","in"]
# obj.longest_prefix(string_list)
#

# obj.anagram('dog','god')
# obj.max_count_ord_string("deepak")

# obj.class_method()
# obj.class_modify(100)

# obj.rotate_string("abcde","cdea")
print(obj.isomorphic_string('egg','addb'))
    
    #       __          ____  |      /\    ___   __
    # |\ | |__ | /\|   |      |     /__\  |___  |__
    # | \| |__ |/ \|  |____   |___ /    \ ___|  __|
    
class whatsapp:
    def __init__(self,messsage):
        self.message =messsage
        
        
    def printingmessage(self):
        print(self.message)
# SINGLE INHERITENCE    
class whatsapp1(whatsapp):
        
    def videocall(self):
        print("Incoming video call")
        
#mutilevel Inheritence      
class whatsapp2(whatsapp1):
    
    def __init__(self,message):
        super().__init__(message)
        
    def addstatus(self):
        print("added status")
        

# wtapp = whatsapp2("Hello world")
# wtapp.printingmessage()
# wtapp.videocall()
# wtapp.addstatus()
        
#multiple inheritence

class fly:
    def flyable(self):
        print("i can fly")
        
class swim:
    def swimmable(self):
        print("swimmable")
         
class fish(swim):    
    def swimmab(self):
        print("swims")
        
class bird(swim,fly):
    def swimmab(self):
        print("swims")
        
    def flyable(self):
        print("flys")
    
# duck = bird()
# duck.swimmable()
# duck.flyable()

# shark =fish()
# shark.swimmable()
# shark.flyable()


#hiererical inheritence

class Andriod:
    def calls(self):
        print("Ringiing......")
    
    def music(self):
        print("Music plays.....")
        
    def camera(self):
        print("click...:)")

class RedMi(Andriod):
    def name(self):
        print("red mi")
        
    def battery(self):
        print("new Feature 50000mah")
        
class IPhone(Andriod):
    def name(self):
        print("I phone")
    def battery(self):
        print("new Feature 30000mah")
        
# phone1 = RedMi()
# phone1.name()
# phone1.battery()
# phone1.calls()
# phone1.camera()

# phone2 = IPhone()
# phone2.name()
# phone2.battery()
# phone2.calls()
# phone2.camera()




        

        