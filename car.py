# Practices exercise 

class Car: 
    def start(self):
        return "I start all cars"
    
class Bmw(Car):
    def start(self):
        return "I start all BMW cars"
    
class X6(Bmw):
    def start(self): # ADD self
        return 'I start the Bmw X6 model'


car = X6()
print(car.start())