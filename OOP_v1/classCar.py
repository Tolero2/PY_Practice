class Car():
    color = None
    mileage = None

    def __init__(self, color, mileage) -> None:
        self.color=color
        self.mileage=mileage

    def __str__(self) -> str:
        return f"The {self.color} car has {self.mileage:,} miles."


a=Car(color="blue", mileage=20000)
b=Car(color="red", mileage=30000)

print(a)
print(b)
