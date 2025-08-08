class Car:
    total_car =0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car+=1
    def fullname(self):
        return f"{self.__brand} {self.__model}"    
    def get_brand(self):
        return self.__brand
    def fuel_type(self):
        return "petrol or diesel"
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric charge"
my_car = Car("toyota", "corolla")
# my_car.model = "city"
# print(my_car.get_brand)
# print(my_car.model)
# print(my_car.fullname())
# print(my_car.fuel_type())
print(my_car.model)
my_tesla = ElectricCar("tesla", "cybertruck","85 kWh")
print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))
# print(my_electric_car.battery_size)
# print(my_electric_car.brand)
# print(my_electric_car.model)
# print(my_electric_car.fullname())
# print(my_electric_car.fuel_type())
# print(Car.total_car)
# print(Car.general_description())
# print(my_car.general_description())

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCar2(Battery,Engine,Car):
    pass

my_new_tesla = ElectricCar2("tesla", "model s")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())