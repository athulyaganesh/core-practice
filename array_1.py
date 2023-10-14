class Array:
    def __init__(self):
        self.elements = {} # dictionary 
        self.length = 0
        
    def shift(self, index): # shift elements in an array-like data structure
        #(possibly an instance variable @elements) towards the beginning by one
        # position, starting from the provided index until the second-to-last element.
        counter = index 
        while counter < self.length - 1:
            self.elements[counter] = self.elements[counter + 1]
            counter += 1 
            
    
    def count(self): #count of elements 
        return self.length 
    
    def push(self, element): #add element to the end of the array
        self.elements[self.length ] = element
        self.length += 1 
    
    def at(self, index): #check if element exists 
        return self.elements[index] if self.elements[index] else None 

    def pop(self): #remove element from the end of the array
        last = self.elements[self.length - 1 ]
        del self.elements[self.length - 1]
        self.length -= 1
        return last 
    
    def delete(self, index): #remove specific element
        if index < self.length:
            element = self.elements[index]
        self.shift(index)
        return element  
    
    def delete_element(self, element): #deletes specific element in the array 
        in_loop = False 
        for i in range(0, self.length):
            if self.elements[i] == element:
                in_loop = True 
                self.shift(i) 
        return element if in_loop else None 
        
    def includes(self, element):#returns True if element exists in Array, else False 
        includes = False
        for i in range(0, self.length): 
            if element == self.elements[i]:
                return True     
        return False 
    
    def print(self):
        for i in range(0, self.length):
            print(self.elements[i])
        
print("Hello")
a = Array()
print(a.count()) 
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
a.print() 
print("")
a.pop() 
a.print() 
        
    
