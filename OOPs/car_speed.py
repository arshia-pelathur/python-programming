import random

class Car():
    def __init__(self,model,make):
        self.__year_model = model
        self.__make = make
        self.__speed = 0
    
    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5
    
    def get_speed(self):
        return self.__speed


def main(action):
    car = Car('2015','Toyota Innova')
    print(f'{car._Car__make} - {car._Car__year_model}:')
    ans = input('Would you like to start (yes/no)')
    while str.lower(ans) == 'yes':
        option = random.randint(0,1)
        if action[option] == 'accelerate':
            print('The car is Accelerating')
            car.accelerate()
        else:
            print('The car is Braking')
            car.brake()
        ans = input('Continue (yes/no) ???? ')
    print(f'The final speed of the car is {car.get_speed()}')


if __name__ == '__main__':
    dict = {0:'accelerate',
            1:'brake'}
    main(dict)