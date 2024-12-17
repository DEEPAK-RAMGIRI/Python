class Day02:
    
    def __init__(self,lists,tuples,sets,dictionary,number):
        self.lists = lists
        self.tuples = tuples
        self.sets = sets
        self.dictionary = dictionary
        self.number = number
    
    #lists  
      
    def appending(self,value):
        self.lists.append(value)
        
    def inserting(self,value,index):
        self.lists.insert(index,value)
        
    def sliceing(self,start = 0):
        print(self.lists[start:len(self.lists)])
        
         
    def printing(self):
        print(self.lists)
        
          
    #tuples 
    
    def tuples_appending(self,value):
        #we can't directly add so just type cast to list and append using list operations
        new_list = list(self.tuples)
        new_list.append(value)
        self.tuples = tuple(new_list)
        
    def tuple_printing(self):
        print(self.tuples)
        
    #sets

    def sets_printing(self):
        print(self.sets)
        
    #dictionary
    
    def dict_adding(self,moviename,animename):
        self.dictionary.update({'movie':moviename,'anime':animename})
        
    def dict_popitem(self):
        self.dictionary.popitem()
        
    def dict_clear(self):
        #clearing the whole dictionary
        self.dictionary.clear()
    
    def dict_printing(self):
        print(*self.dictionary.keys())
        print(*self.dictionary.values())
    
    def print_odd_and_even(self,no):
        no+=1
        print("even numbers: ",end=" ")
        for i in range(0,no,2):
            print(i,end=" ")
        
        print("\nOdd numbers: ",end=" ")
        for i in range(1,no,2):
            print(i,end=" ")
    
    # Programe for vote eligibility
    def eligible(self,age):
        # print("u r not eligible" if age < 18 else "u r eligible to vote")
        
        if age < 18:
            print("u r not eligible to vote")
        else:
            print("u r eligible to vote")
        
    
    # programe passenger = female must have aadhar  if she is Ts then 100% concession 
    def female_passenger(self,gender,aadhar ,address):
        
        if gender == "FEMALE" and aadhar:
            
            if address == "TS":     
                print("100 percentage Concession\nNo need to buy ticket Please enter :)")
            elif address == "AP":
                print("50 percentage Conession")
            else:
                print("10 percentage Conession")
        else:
            print("Sorry! :( \nNo concession please buy ticket :)")
            
    def taxpayers(self,salary):
        
        if salary >=50000 and salary <=100000:
            print(f"10% tax for u which is {salary/10}")
        elif  salary >= 25000 and salary < 50000:
            print(f"5% tax for u which is {salary/20}")
        elif salary < 25000:
            print(f"No tax for u :)")
        else:
            print("enter valid number which rangees between 0 to 100000")  
            
            
    # find a number is  prime or not
    
    def primeornot(self):
        
        flag = True
        for i in range(2,self.number // 2 + 1):
            if not self.number % i: 
                flag =False
                break
        if flag:
            if self.number == 1:
                print("1 is neither composite nor prime number")
            else:
                print(f"{self.number} Prime number")
        else:
            print(f"Contradiction! {self.number} is not a prime number, it is a Composite number")        
     
    def prime_range(self):
        
        for i in range(2,self.number):
            flag =True
            for j in range(2,i//2+1):
                if not i%j:
                    flag = False
                    break
            if flag:
                print(i,end=" ")
                    
    def palindrome(self,string):
        return string == string[::-1]
    
    def spy_number(self,no):
        sums = 0  
        prod = 1
        for i in no:
            sums+=int(i)
            prod*=int(i)
        print("spy number" if sums == prod else "not spy number") 
    
lists = [1,2,4.0, "Deepak kumar"] 
tuples = ("Optimus prime",True,20,20.00)
sets = {"Naruto",10.0,2,False}

dictionary = {
            "name":"Deepak",
            "age":20,
            "place" : "NZB"
        }

number = 10#int(input("Ente number: "))
obj1 = Day02(lists,tuples,sets,dictionary,number)

# obj1.appending(10)
# obj1.inserting(12,0)
# # obj1.sliceing()
# obj1.printing()

# obj1.tuples_appending(1000)
# obj1.tuple_printing()

# obj1.sets_printing()

# obj1.dict_adding("Harry Potter","One piece")
# # obj1.dict_popitem()
# # obj1.dict_clear()
# obj1.dict_printing()

# obj1.print_odd_and_even(10)
# obj1.eligible(18)
# obj1.female_passenger("FEMALE",True,"TS")
# salary = int(input())
# obj1.taxpayers(salary)

# obj1.primeornot()
# obj1.prime_range()

# string =input()
# if obj1.palindrome(string):
#     print("palindrome")
# else:
#     print("Not palindrome")

obj1.spy_number(str(1124))
