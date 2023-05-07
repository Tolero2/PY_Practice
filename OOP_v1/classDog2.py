class Dog2:
    species = "Canis Familiaris"
    def __init__(self, name, age) -> None:
        self.name=name
        self.age=age

    #instance method
    #def description(self):
    # Replace .description() with __str__() to call the dunda method for displaying info about your class instance and its object// usually a string to describe the paticukar passed object 
    def __str__(self):
        return (f'{self.name} is a {self.age} year old dog')

    #another instance method that requires an additional parameter to perform the specific method as opposed to description () method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
print(Dog2("james", 2))