class Stack:
    def __init__(self):
        self.__elements = []
    
    def push(self, element):
        self.__elements.append(element)
    
    def pop(self):
        try:  
            element = self.__elements.pop()
        except IndexError:
            element = None 
        return element 
          
    def get_len_stack(self):
        return len(self.__elements)
       
    # def get_all_stack(self):
    #     return self.__elements
    

from collections import deque
class Queue_1:
    def __init__(self):
        self.__elements = deque()
   
    def enqueue(self, element):
        self.__elements.append(element)

    def dequeue(self):
        try:
            element = self.__elements.popleft()
        except IndexError:
            element = None    
        return element
    
    def get_len_queue(self):
        return len(self.__elements)


class Queue_2:
    def __init__(self):
        self.__elements = []
   
    def add(self, element):
        self.__elements.insert(0, element)

    def remove(self):
        try:
            element = self.__elements.pop()
        except IndexError:
            element = None    
        return element
    
    def get_len_queue(self):
        return len(self.__elements)
        
    # def get_all_queue(self):
    #     return self.__elements

class Queue_3:
    def __init__(self):
        self.__elements = []
   
    def add(self, element):
        self.__elements.append(element)

    def remove(self):
        try:
            element = self.__elements.pop(0)
        except IndexError:
            element = None    
        return element
    
    def get_len_queue(self):
        return len(self.__elements)
        
    # def get_all_queue(self):
    #     return self.__elements
    
                
            
    