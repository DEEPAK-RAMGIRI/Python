import math
class Day03:
    
    def __init__(self,dict1,list1,number):
        self.dict1 = dict1
        self.list1 = list1
        self.number = number
    
    def print_dict(self):
        print(self.dict1)
        
    # def modify
        
    def print_specific_ele(self,key,value):
        self.dict1[key] = value # modifying element 
        print(self.dict1[key])
        
    def print_missing(self):
        
        #method 1
        
        for i in range(1,len(self.list1)+1):
            if  i != self.list1[i-1] :
                print("Missing number is: ",i)
        
        # method 2
        # This method not work for every test cases but for only works for natural numbers 
        # max_no = max(self.list1)
        # maxsum = int((max_no *(max_no+1))//2) # (n*(n+1)) // 2
        # for i in self.list1:
        #     if maxsum >= i:
        #         maxsum -= i
        # print("Missing number is:",maxsum)
        
        #method 3
        max_no = max(self.list1)
        min_no = min(self.list1)
        missing_no = int (((max_no *(max_no+1))//2) - ((min_no * (min_no - 1))//2)) - sum(self.list1) 
        #  sum of first n natual numbers (n*(n+1)) // 2  
        # sum of first n-1 natural numbers (n*(n-1)) //2
        print(missing_no)
        
    # programme to check wheather given no is perfect no
    def perfect_no(self):
        sums = 1
        for i in range(2,int(math.sqrt(self.number))+1):
            
            if not self.number % i :
                sums+=i
                # if self.number // i < self.number: # just add everything and then subtract self.number at last
                #     sums+= self.number // i
                sums+= self.number // i  
        print("perfect no" if self.number == sums else "No perfect number")
        
    def multiples(self):
        # Multiplication table
        for i in range(1,11):
            print(f"{self.number} X {i} = {self.number * i}")           
        
    def duplicate_count(self,string):
        # using dict to find counts
        counting =dict()
        for i in string:
            if i not in counting: 
                counting[i]=1
            else:
                counting[i]+=1
                
        # l=sorted(counting.items(),key=lambda x:x[1]) #conver  ts it into tupl 
        # print(l[-1])
        
        # ans = [i for i in counting if counting[i] == max(counting.values())]        
        # print(string.count(*ans)) # count takes one parameter which help to count thevalues
        
        
    #printing string without duplicate
    def remove_duplicate_and_print(self,string):
        string2= ""
        for i in string:
            if i not in string2:
                string2+= i 
        print(string2)
        
    def upper_to_lower_and_lower_to_upper(self,string):
        
        # string2=""
        # for i in string:
        #     if i.isupper():
        #         string2+=i.lower()
        #     else:
        #          string2+=i.upper()
        
        string2 = "EXams".swapcase()  #MORE OPTMISED VERSION (KEYWORD swapcase)
        print(string2)
    
    #Addition of two digits
    def SumDigits(self,num1,num2):
        return num1+num2   
    
    def SubtractDigits(self,num1,num2):
        return num1-num2
    
    def MultDigits(self,num1,num2):
        return num1 * num2
    
    def divDigits(self,num1,num2):
        return num1 // num2
    
    def Odd_Or_Even(self,num1):
        return "Odd Number" if  num1 & 1 else "Even Number"    
    
    def prime_or_not(self,num1):
        
        for i in range(2,int(math.sqrt(num1))+1):
            if not num1 % i:
                return "Not prime Number"
        return "prime Number" if num1 != 1 else "it is neither composite nor prime"
    
    def Fizz_Buzz(self,no):
        
        for i in range(1,no):
            if not i%3 and not i%5:
                print("Fizz Buzz")
            elif not i%5:
                print("Buzz")
            elif not i%3: 
                print("Fizz")
            else:
                print(i)
        
   
        
dict1 = dict({
    'name':'Deepak',
    'color':'black', # it will not print
    'color':'white', # it will print
    'favcolor':"white" #  keys must unique value can be duplicate
})

list1 = [10,11,13,14]
number =10 #int(input())

obj1 = Day03(dict1,list1,number)
# obj1.print_dict()
# obj1.print_specific_ele('name','naruto')
# obj1.print_missing()
# obj1.perfect_no()
# obj1.multiples()

# string ="eeeeefgh"
# obj1.duplicate_count()
# obj1.remove_duplicate_and_print(string)

# string1= "EXams"
# obj1.upper_to_lower_and_lower_to_upper(string1)

# print(obj1.SumDigits(10,20))
# print(obj1.SubtractDigits(10,20))
# print(obj1.MultDigits(10,20))
# print(obj1.divDigits(10,20))

# print(obj1.Odd_Or_Even(23))

# print(obj1.prime_or_not(4))
# obj1.Fizz_Buzz(21)
