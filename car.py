class Car:
    def __init__(self, price, speed, fuel, mileage, tax):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax
        if self.price > 10000:
            self.tax = .15
        elif self.price < 10001:
            self.tax = .12
    def display_all(self):
        print("Price:", self.price)
        print("Speed:", self.speed)
        print("Fuel:", self.fuel)
        print("Mileage:", self.mileage)
        print("Tax:", self.tax)
Car1 = Car(5000, "120 mph", "87 UL", "15 mpg", 0).display_all()
Car2 = Car(50000, "200 mph", "91 UL", "30 mpg", 0).display_all()
Car3 = Car(10000, "160 mph", "89 UL", "25 mpg", 0).display_all()
Car4 = Car(1000, "60 mph", "87 UL", "15 mpg", 0).display_all()
Car5 = Car(200000, "260 mph", "95 UL", "30 mpg", 0).display_all()
Car6 = Car(100000, "140 mph", "Diesel", "20 mpg", 0).display_all()