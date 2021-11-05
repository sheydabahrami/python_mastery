 # 13 The Object Class


class Animal:
    def __init__(self):
        self.age = 1
    
    def eat(self):
        print("eat")


class Mammal(Animal): 
    
    def walk(self):
        print("walk")


class Fish(Animal):     
    
    def swim(self):
        print("swim")

m = Mammal()
print(isinstance(m, Animal)) # We are checking if Mammal class  is a sub class of Animal. It will return True

# All classes that we have directly or indirectly derive from the "object" Class which is parent of all classes

print(isinstance(m, object))

print(issubclass(Mammal, Animal)) # With the built in function "issubclass" we can check if one class is a subclass of another.
print(issubclass(Mammal, object))