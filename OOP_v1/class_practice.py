#Define a class // pass Keyword is a placeholder for the behavior of the class.
class Dog:
    pass

#.__init__() is the instantiator of the class that must be used to define the parameters to pass and the attributes (self.arg) to associate the params value with in the class
class Dog1:
    #class attribute
    species = "Canis Familiaris"
    #every class must have its init method to parse the dynamic properties assigned to each instance of the class.
    def __init__(self, name, age):
        #instance attribute
        self.name=name
        self.age=age

#Object instance with the properties for this class instance.
a = Dog1(name="doggy", age=10)
a.name = "peru"


class Dog2:
    species = "Canis Familiaris"
    def __init__(self, name, age) -> None:
        self.name=name
        self.age=age

    #instance method
    def description(self):
        return (f'{self.name} is a {self.age} year old dog')

    #another instance method that requires an additional parameter to perform the specific method as opposed to description () method
    def speak(self, sound):
        return f"{self.name} says {sound}"

name=input("Enter the dog's name: ")
age=input("Enter the dog's age: ")
sound=input("Enter the sound of the dog: ")
a = Dog2(name=name, age=age)
b=a.description()
c=a.speak(sound=sound)
#d= a.speak("Bow WOw")
print(f"{b} and {c} when it barks")




#print(f'{a.name}\n{a.age}\n{a.species}')
