from random import randint
from colorama import Fore, Back, Style, init

init(autoreset=True)


class House:
    def __init__(self, money, food, dirt):
        self.money = money
        self.food = food
        self.dirt = dirt

    def __str__(self):
        return f'{self.__class__.__name__} money: {self.money}, food: {self.food}, dirt: {self.dirt}'

    def add_dirt(self, amount):
        self.dirt += amount

class Person:
    def __init__(self, name, house, satiety, happiness):
        super().__init__()
        self.name = name
        self.house = house
        self.satiety = satiety
        self.happiness = happiness

    def eat(self):
        if self.house.food >= 10:
            food_to_eat = randint(10, 30)
            self.satiety += food_to_eat
            self.house.food -= food_to_eat


    def decrease_satiety(self):
        self.satiety -= 10

    def increase_happiness(self, value):
        self.happiness += value


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
            self.increase_happiness(20)


class Wife(Person):
    def act(self):
        actions = [self.eat, self.shopping, self.clean_house, self.buy_fur_coat]
        action = actions[randint(0, 3)]
        action()

    def eat(self):
        super().eat()

    def shopping(self):
        self.decrease_satiety()
        buy_food = randint(10, 100)
        if self.house.money >= buy_food:
            self.house.money -= buy_food
            self.house.food += buy_food
        else:
            super().eat()

    def buy_fur_coat(self):
        if self.house.money >= 350:
            self.decrease_satiety()
            self.increase_happiness(60)
            self.house.money -= 350

    def clean_house(self):
        if self.satiety >= 10:
            self.decrease_satiety()
            self.increase_happiness(5)
            self.house.dirt -= min(self.house.dirt, 100)
        else:
            super().eat()

def main():
    house = House(money=100, food=50, dirt=0)
    husband = Husband("John", house, satiety=30, happiness=100)
    wife = Wife("Jane", house, satiety=30, happiness=100)
    # child = Child("Jimmy", house, 100, 100)

    for day in range(365):
        print(Back.GREEN + f'================== Day {day} ==================')
        husband.act()
        wife.act()
        house.add_dirt(5)
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + husband.name + f' (happiness: {husband.happiness}, {husband.satiety})')
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + wife.name + f' (happiness: {wife.happiness}, {wife.satiety})')
        print(house)


if __name__ == "__main__":
    main()
