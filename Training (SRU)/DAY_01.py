#(16-12-24)

# a=[1,1,1,1,1,2,3,33,3,3]
# for i in range(len(a)):
#     flag= True
#     for j in range(len(a)):
#         if i!=j and a[i]^a[j] == 0:
#             flag = False
#             break
#     if flag:
#         print(a[i])    
        
# count = [0]*(max(a)+1)
# # print(len(count))
# for i in range(len(a)):
#     count[a[i]]+=1
# for i in range(len(count)):
#     if count[i] == 1:
#         print(i)


# sum of first n natural numbers
# no = int(input())
# i=0
# sums =0 
# while no >= i:
#     sums+=i
#     i+=1
    
# print(sums)

# sums =0 
# for i in range(no+1):
#     sums+=i
# print(sums)


# find the given no is odd or even

#Method 1

# for i in range((int(input()))  + 1):
#     #Bitwise and 
#     if not i&1:
#         print("odd:",i)
#     else:
#         print("Even:",i)

#Method 2
# a = int(input())
# print("Odd" if a % 2  else "Even")


#method 3
# i = int(input()) 
# if i % 2:
#     print(f"{i} is odd")
# else:
#     print(f"{i} is Even")
    
# leap year
# year = 248
# # if year % 100 != 0 or year % 400 == 0 and year % 4 == 0:
# #     print("Leap year")
# # else:
# #     print("Not Leap year")
    
# #method 2 Correct
# if not (year % 4) and (year % 100 or not (year % 400)) :
#     print(f"{year} Leap Year")
# else:
#     print(f"{year} not Leap year")  


 
# Total =0 
# for i in range(6):
#     sub_marks = int(input())
#     Total += sub_marks
    
# avg = Total/6

# print(f"Averaeg of 6 sub: {avg}")

# if avg >=90:
#     print("O")
# elif avg >= 80:
#     print("A+")
# elif avg >= 70:
#     print("B+")
# elif avg >= 60:
#     print("B")
# elif avg >= 50:
#     print("C")
# else:
#     print("Fail")
    
    
    
    
#Factorial of no
#using for loop
# a =int(input())
# fact = 1
# for i in range(1,a+1):
#      fact *= i
# print(fact)


#using recursion
# class fact:
#     def __init__(self,a):
#         self.a =a
        
#     def printing(self):
#         if self.a == 1:
#             return 1
#         return self.a * fact(self.a - 1).printing()
            
        
        
# a =int(input())       
# obj1 = fact(a)
# ans = obj1.printing()
# print(ans)



#printing prime number
    
class prime:
    
    def __init__(self,number,array,number2):
        self.number = number
        self.array = array
        self.number2 = number2
        
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
            print(f"{self.number} is not a prime number")
    
    def prime_range(self):
        for i in range(2,self.number):
            flag =True
            for j in range(2,i//2+1):
                if not i%j:
                    flag = False
                    break
            if flag:
                print(i)
                
    def largestnumber(self):
        print(f"The largest number in the array is:{max(self.array)}")
        
    def swap_method1(self):
        self.number,self.number2 = self.number2,self.number
        print(self.number,self.number2)
    
    def swap_method2(self):
        self.number = self.number ^ self.number2
        self.number2 = self.number ^ self.number2
        self.number = self.number ^ self.number2
        
        print(self.number,self.number2)
    
    def sum_digits(self):
        sums = sum(int(i) for i in self.number2)
        print(sums)
        
        
            
            
a = 10 #int(input())
array = [1,3,-100]
swapb =input()

obj1 = prime(a,array,swapb)
# obj1.primeornot()
# obj1.prime_range()
# obj1.largestnumber()
# # obj1.swap_method1()
# obj1.swap_method2()
obj1.sum_digits()

