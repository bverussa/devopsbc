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

addNewCar = True
addNewKm = True

while addNewCar == True:
    addNewKm = True
    make = input('Make name? ')
    model = input('Model? ')
    trim = input("Trim? ")
    year = input('Year? ')
    car = Car(make, model, trim, year)
    
    while addNewKm == True:
        km = int(input('Add KM: '))
        car.addKm(km)
        userKm = input('Add more KM? (Y/N) ')
        
        if (userKm in 'Nn'):
            addNewKm = False

    car.getCar()
    car.showKm()
    print(60*'=')

    userCar = input('Add another car? (Y/N) ')

    if (userCar in 'Nn'):
            addNewCar = False