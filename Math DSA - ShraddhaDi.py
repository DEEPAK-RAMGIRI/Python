import math

class prime:
    def __init__(self,no):
        self.no = no
        
    # Checking a number is prime or not
    def primeOrNot(self):
        for i in range(2,int(math.sqrt(self.no)) +1):
            if self.no % i == 0:
                return "Not Prime"
        return "Prime"
    
    # cheking in the range of prime number
    #SIEVE OF ERATOSTHENES
    def PrimeOrNotRange(self):
        
        array=[True]*self.no
        array[0],array[1] = False,False
        count = 0
        
        for i in range(2,self.no):
            if array[i]:
                count+=1
                for j in range(i*2,self.no,i):
                    array[j] = False
                    
        for i in range(len(array)):
            if array[i] == True:
                print(i,end=" ")
        print("\n",count , "are the no of prime numbers present in the range")
                    
                
                
if __name__ == "__main__":
    primenumber = prime(41)
    print(primenumber.primeOrNot())
    primenumber.PrimeOrNotRange()