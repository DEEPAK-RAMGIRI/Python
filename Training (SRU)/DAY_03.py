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

string ="eeeeefgh"
# obj1.duplicate_count()
obj1.remove_duplicate_and_print(string)
