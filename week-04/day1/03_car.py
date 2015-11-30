# lada = {
#     'color': 'red',
#     'type': 'Lada 1200',
#     'km': 400000
# }
#
# tesla = {
#     'color': 'pink',
#     'type': 'Tesla S',
#     'km': 1200
# }
#
# def ride(car, km):
#     car['km'] += km
#
# ride(tesla,220)
# print(tesla)
#
# def initCar(color, type, km):
#     car = {'color':'', 'type':'', 'km': 0}
#     car['color'] = color
#     car['type'] = type
#     car['km'] = km
#     return car
#
# skoda = initCar('green', 'Skoda SuperB', 12000)
# print(skoda)


# with Class
class Car:
    def __init__(self, color, type, km):
        self.color = color
        self.type = type
        self.km = km

    def ride(self, km):
        self.km += km

toyota = Car('black', 'Toyota Corolla', 136000)
toyota.ride(220)
print(toyota.km)
