class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5 

    def brake(self):
        self.speed -= 5 

    def get_speed(self):
        return self.speed

my_car = Car("Porsche", "911", 2020)

# розганяємось 5 разів
print("Прискорення:")
for i in range(5):
    my_car.accelerate()
    print("Поточна швидкість: ",my_car.get_speed(),"км/год")

# гальмуємо 5 разів
print("\nГальмування:")
for i in range(5):
    my_car.brake()
    print("Поточна швидкість: ",my_car.get_speed(),"км/год")
