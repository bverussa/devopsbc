class Car:

    def __init__(self, make, model, trim, year):
        INITIAL_KM = 0
        self.make = make
        self.model = model
        self.trim = trim
        self.year = year
        self.km = INITIAL_KM

    def getCar(self):
        print('Make:', self.make, '| Model:', self.model, '| Trim:', self.trim, '| Year:',  self.year)
        # another example:
        # print('Make: ' + self.make +  ' | Model: ' + self.model + ' | Trim: ' + self.trim + ' | Year:' + str(self.year))
        # one more example:
        # print('Make: %s | Model: %s | Trim: %s | Year: %d' %(self.make, self.model, self.trim, self.year))

    def addKm(self, km):
        self.km += km

    def showKm(self):
        print('Km:', self.km)

car = Car('BMW', 'X5', 'M40', 2020)
car2 = Car('Audi', 'Q5', 'Technik', 2019)
car.getCar()
car.addKm(1000)
car.addKm(500)
car.addKm(8000)
car.showKm()
print(60*'=')
car2.getCar()
car2.addKm(14000)
car2.showKm()

if (False or False or False or False or True):
    print('Here')