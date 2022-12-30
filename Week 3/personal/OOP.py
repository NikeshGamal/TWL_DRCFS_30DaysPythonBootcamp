# __init__ -- is similar to constructor that initialize some instance variable and is called as soon as class instance is created 

#attribute--> they are simply variable that belong to certain class

#class call--> initialize

class Animal:

    #attributes
    #class attribute
    name = "Kaali"
    age = 6

    def __init__(self, name: str, age: int , type: str)-> None:
        #instance attribute
        self.name = name
        self.age = age
        self.type = type
    
    #instance method
    #instance ma data pass hunxa instance hunxa pass the value
    def __str__(self):
        return f"My name is {self.name} and my age is {self.age} . I'm a {self.type}"

    # def __str__(self)-> str:
    #     return 'aksdjfalksdjfa'
    
    def can_fly(self):
        if self.type == 'BIRD':
            return True
        return False

#whereas instance ma self bhanni value pass hunxa
#class method--> blueprint bata real data ma lagni method
#cls --> kaley= Animal--> initialize nabhayeko value pass hunxa
#class method le instance banauuxa 
#i.e instance xaina banaxa

#cls.abc = 'abc' can change directly change the class attribute
    @classmethod
    def from_bird(cls, name: str , age: int )-> 'Animal':
        bird_instance = cls(name, age , 'BIRD')
        return bird_instance
    
    #decorator
    @classmethod
    def from_dog(cls, name: str, age:int) -> 'Animal':
        dog_instance = cls(name, age , 'DOG')
        return dog_instance


# print(Animal.name)
# print(Animal().name)

# a = Animal()
# print(a.name)

kaley = Animal("Kaley",22,'DOG')
details = kaley.__str__()
print(details)

#self--> instance chai self ma pass hunxa   

print('-'*100)
print('-'*100)

# print(str(kaley))

pattu = Animal("Pattu",22,'BRID')

#previously
#pattu = Animal('Paattu',1,'BIRD')
pattu = Animal.from_bird('Pattu',1)
rupi = Animal.from_dog('Kallu',2)

#pattu --> instance reutn bhayera pattu ma basxa then it is the case that pass by reference
print(pattu.__str__(),pattu.can_fly())
print(str(rupi),rupi.can_fly())




#static method--> takes nothing , just when we want to wrap but values chahiyeko xaina bhane static method
