class Bike:
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
        self.miles = 0
    def displayInfo(self):
        print(self.price)
        print(self.max_speed)
        print(self.miles)
        return self
    def ride(self):
        print("Riding")
        self.miles+= 10
        return self
    def reverse(self):
        print("Reversing")
        self.miles-= 5
        if self.miles < 0:
            self.miles = 0
        return self
bike1 = Bike(200, "25 mph", 0).ride().ride().ride().reverse().displayInfo()
bike2 = Bike(150, "20 mph", 0).ride().ride().reverse().reverse().displayInfo()
bike3 = Bike(250, "30 mph", 0).reverse().reverse().reverse().displayInfo()