from random import randint
from colorama import Fore, Back, Style, init

init(autoreset=True)


class House:
    def __init__(self, money=100, food=50, dirt=0):
        self.money = money
        self.food = food
        self.dirt = dirt


class Person:
    def __init__(self, name, house, satiety, happiness):
        super().__init__()
        self.name = name
        self.house = house
        self.satiety = satiety
        self.happiness = happiness

    def __str__(self):
        return f'{self.__class__.__name__} {self.name}: satiety={self.satiety}, happiness={self.happiness}'

    def eat(self):
        if self.house.food >= 30:
            food_to_eat = randint(10, 30)
            self.satiety += food_to_eat
            self.house.food -= food_to_eat
        else:
            self.buy_food()

    def buy_food(self):
        buy_food = randint(50, 100)
        self.house.money -= buy_food
        self.house.food += buy_food

    def decrease_satiety(self):
        self.satiety -= 10

    def increase_happiness(self):
        self.happiness += 10


class Husband(Person):
    def act(self):
        actions = [self.eat, self.work, self.gaming]
        action = actions[randint(0, 2)]
        action()

    def eat(self):
        super().eat()

    def work(self):
        if self.satiety <= 10:
            self.eat()
        else:
            self.decrease_satiety()
            self.house.money += 150

    def gaming(self):
        if self.satiety <= 10:
            self.eat()
        else:
            self.decrease_satiety()
            self.increase_happiness()


class Wife:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def shopping(self):
        pass

    def buy_fur_coat(self):
        pass

    def clean_house(self):
        pass


def main():
    house = House()
    husband = Husband("John", house, satiety=30, happiness=100)
    # wife = Wife("Jane", house, 100, 100)
    # child = Child("Jimmy", house, 100, 100)

    # family = [husband, wife, child]

    for day in range(365):
        print(Back.GREEN + f'================== Day {day} ==================')
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + husband.name + f' (happiness: {husband.happiness})')
        husband.act()
        print(Fore.BLUE + Style.BRIGHT + f'House: money={house.money}, food={house.food}\n')


if __name__ == "__main__":
    main()
