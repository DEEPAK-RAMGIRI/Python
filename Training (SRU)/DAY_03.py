class Day03:
    
    def __init__(self,dict1,list1):
        self.dict1 = dict1
        self.list1 = list1
    
    def print_dict(self):
        print(self.dict1)
        
    # def modify
        
    def print_specific_ele(self,key,value):
        self.dict1[key] = value # modifying element 
        print(self.dict1[key])
        
    def print_missing(self):
        
        #method 1
        
        # for i in range(1,len(self.list1)+1):
        #     if  i != self.list1[i-1] :
        #         print("Missing number is: ",i)
        
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
        
                
    
                
    
dict1 = dict({
    'name':'Deepak',
    'color':'black', # it will not print
    'color':'white', # it will print
    'favcolor':"white" #  keys must unique value can be duplicate
})

list1 = [10,11,13,14]

obj1 = Day03(dict1,list1)
# obj1.print_dict()
# obj1.print_specific_ele('name','naruto')
obj1.print_missing()