from colorama import Fore, Back, Style, init
init()
class House:

    def __init__(self, money, food, dirt):
        self.money = money
        self.food = food
        self.dirt = dirt


class Husband(House):
    satiety = 30
    happiness = 100

    def __init__(self, name, money, food, dirt):
        super().__init__(money, food, dirt)
        self.name = name

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def gaming(self):
        pass


class Wife:
    satiety = 30
    happiness = 100

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


home = House(money=100, food=50, dirt=0)
alex = Husband(name='Alex')
tanya = Wife(name='Nina')

for day in range(365):
    print(Back.GREEN + '================== Day {} =================='.format(day))
    alex.act()
    tanya.act()
    print(Fore.LIGHTMAGENTA_EX + alex)
    print(Fore.LIGHTBLUE_EX + tanya)
    print(Style.DIM + home)
