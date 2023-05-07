# #PARENT class
# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

#     def speak(self, sound):
#         return f"{self.name} says {sound}"
# #CHILD classes extends parent class Dog by including class name in the parenthesis
# class JackRussellTerrier(Dog):
#     pass

# class Dachshund(Dog):
#     pass

# class Bulldog(Dog):
#     pass


# miles = JackRussellTerrier("Miles", 4)
# buddy = Dachshund("Buddy", 9)
# jack = Bulldog("Jack", 3)
# jim = Bulldog("Jim", 5)

# print(jack, "\n",jim.speak("woof"),"\n",buddy.name,"\n",miles.species)




#CLASS(PARENT)
class Dog():
    name=None
    age=None

    def __init__(self, name, age) -> None:
        self.age=age
        self.name=name

    def __str__(self) -> str:
        return f" {self.name} is {self.age} years old."
    
    def speak(self,sound):
        return f"{self.name} speak like {sound}"

#SUBCLASS(CHILD)
class GoldenRetriever(Dog):
    #hybrid implementation: override speak method in parent class to add new logic to the class(i.e.speak method logic); but use the output of the speak method from parent class to display exactly the logic of parent class only
    def speak(self,sound="Bark"):
        return super().speak(sound)



#ONE INSTANCE of GoldenRetriever subclass of Dog class
a=GoldenRetriever("Ray",7)
b=a.speak()
print(a,"\n",b)
print("is this an instance of the Dog class? : {}".format(isinstance(a,Dog)))
















