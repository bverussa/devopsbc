try:
    random_number = int(input("Please enter an integer: "))

    if isinstance(random_number, (int)):
        if random_number < 0:
            print('Negative')
        elif random_number == 0:
            print('Zero')
        elif random_number == 1:
            print('Single')
        else:
            print('Higher value')
        
        print("The value of random_number is:", random_number)
except:
    print('This is not a number')