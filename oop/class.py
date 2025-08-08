class Car:
    total_car =0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car+=1
    def fullname(self):
        return f"{self.__brand} {self.model}"    
    def get_brand(self):
        return self.__brand
    def fuel_type(self):
        return "petrol or diesel"
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric charge"
my_car = Car("toyota", "corolla")
print(my_car.get_brand)
print(my_car.model)
print(my_car.fullname())
print(my_car.fuel_type())
my_electric_car = ElectricCar("tesla", "cybertruck","85 kWh")
# print(my_electric_car.battery_size)
# print(my_electric_car.brand)
# print(my_electric_car.model)
print(my_electric_car.fullname())
print(my_electric_car.fuel_type())
print(Car.total_car)
print(Car.general_description())
# print(my_car.general_description())