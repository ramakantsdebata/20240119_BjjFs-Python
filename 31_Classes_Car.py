class Car:
    # Class variables
    __total_cars = 0

    def __init__(self, make, model, year, color):
        # Instance variables
        self.__make = make
        self.__model = model
        self.__year = year
        self.__color = color
        ## Increment the car count
        Car.__total_cars += 1
        
    @classmethod
    def car_count(cls):
        return cls.__total_cars
    
    def start(self):
        print(f"{self.__year} {self.__make} {self.__model} is starting")

    @staticmethod  # This could easily be a global function without affecting any behaviour change
    def aboutType():
        return "This is a Car class"
        
    ## String Representations of class objects
    # str(obj)  --->  obj.__str__() ---> repr(obj) ---> obj.__repr__()
        
    def __str__(self):
        return f"{self.__color} {self.__model}"
        
    def __repr__(self):
        return f"{self.__year} {self.__make} {self.__model} {self.__color}"
    
    def __add__(self, other):
        return self.__year + other.year
        
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, value):
        self.__color = value

class GearedCar(Car):
    # Class variables
    total_cars = 0
    car_options = 10

    def __init__(self, make, model, year, color, gears):
        # Instance variables
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.gears = gears
        ## Increment the car count
        GearedCar.total_cars += 1

    

if __name__ == "__main__":
    c1 = Car("Honda", "Accord", 2019, "Black")
    c2 = Car("Toyota", "Camry", 2018, "White")
    c3 = Car("Honda", "Civic", 2017, "Red")
    c4 = Car("Toyota", "Corolla", 2016, "Blue")
    c5 = Car("Honda", "CRV", 2015, "Green")

    print(c1.color)
    c1.color = "Yellow"
    print(c1)

    # print(f"We have now created {Car.car_count()} cars")

    # # lst = [1, 2, 3]
    # # # print(lst)
    # # # print(str(lst))
    # # print(lst.__str__())

    # print(c1.__str__())
    # print(c2)
    # print(repr(c3))


    # # print(c1)
    # # print(c2)
    # # print(c3)
    # # print(c4)
    # # print(c5)
    
    # # c1.start()
    # # c2.start()
    # # c3.start()
    # # c4.start()
    # # c5.start()
    
    # print("Done!")

    # print("\n\n", "-"*10, "Geared Car", "-"*10)
    # gc1 = GearedCar("Honda", "Accord", 2019, "Black", 5)
    # gc2 = GearedCar("Toyota", "Camry", 2018, "White", 5)

    # print(f"We have now created {GearedCar.car_count()} cars")
    # print(f"We have now created {GearedCar.total_cars} cars")

    # print("Result:", c1 + c2) ## c1.__add__(c2) -> int(year1 + year2)

