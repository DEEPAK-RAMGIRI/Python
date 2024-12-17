class Day02:
    
    def __init__(self,lists,tuples,sets,dictionary):
        self.lists = lists
        self.tuples = tuples
        self.sets = sets
        self.dictionary = dictionary
    
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
    
        
lists = [1,2,4.0, "Deepak kumar"] 
tuples = ("Optimus prime",True,20,20.00)
sets = {"Naruto",10.0,2,False}

dictionary = {
            "name":"Deepak",
            "age":20,
            "place" : "NZB"
        }


obj1 = Day02(lists,tuples,sets,dictionary)
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

obj1.print_odd_and_even(10)



