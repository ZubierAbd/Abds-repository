# class Dog():
#
#     def __init__(self,name,age):
#         '''These are defining the self and the attributes of this class'''
#         self.name = name
#         self.age = age
#     def sit(self):
#         print(self.name.title() + ' is now sitting')
#
#     def roll_over(self):
#         print(self.name.title() + ' Rolled over')
#
# Mydog = Dog('Willie',16)
# Mydog.sit()
# Mydog.roll_over()
#
#
# yourdog = Dog('Samara',4)
# yourdog.sit()
# yourdog.roll_over()

class Restaurant():

    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print('The restaurant is called ' + self.name.title())
        print('The restaurant serves '+ self.cuisine.title())

    def open_restaurant(self):
        print('The restaurant ' + self.name.title() + ' is now open')

Nandos = Restaurant('Nandos','crappy food')
StarKabab = Restaurant('Star Kabab', 'Great food')
PizzaPizza = Restaurant('Pizza Pizza','pizza')

Nandos.describe_restaurant()
Nandos.open_restaurant()
StarKabab.describe_restaurant()
PizzaPizza.describe_restaurant()

class User():

    def __init__(self,firstname,lastname,age,gender):

        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender

    def describe_user(self):

        print('The user is named ' + self.firstname.title() + self.lastname.title())
        print('The age of the user is ' + str(self.age))
        print('The gender of the user is ' + self.gender.title())

    def greet_user(self):
        print("Hello" + self.firstname.title() + " How are you doing? ")


Samara = User('Samara','Nice ass Rasul', 24, 'Female')

Samara.describe_user()
Samara.greet_user()


class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometerreader = 0

    def readodo(self):
        print('This car has ' + str(self.odometerreader) + ' miles on it')

    def get_descriptivename(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odo(self,mileage):
        if mileage >= self.odometerreader:
            self.odometerreader = mileage
        else:
            print('Fuck you buddy. You cant roll back an odometer')



mynewcar = Car('Audi','A400',1978)
print(mynewcar.get_descriptivename())
mynewcar.readodo()




