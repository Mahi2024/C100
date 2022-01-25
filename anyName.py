class Car(object):
    def __init__(self, model, colour, company, speedLimit, mileage):
        self.model=model
        self.colour=colour
        self.company=company
        self.speedLimit=speedLimit
        self.mileage=mileage
    def start(self):
        print('Car has started')
    def stop(self):
        print('Car has stopped')
Audi=Car("A2A4","Black","Audi",150,30)
Chiron=Car("M2M0","White","Buggati",200,50)
print(Audi.start())
print(Audi.colour)