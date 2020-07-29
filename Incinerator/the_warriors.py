#!/usr/bin/env checkio --domain=py run the-warriors

# 
# END_DESC

class Warrior:

    h: int = 50
    a: int = 5
    is_alive: bool = True

    def ju(self):
        if self.h > 0:
            self.is_alive = True
        else:
            self.is_alive = False
    pass

class Knight(Warrior):

    a: int = 7


    c=[]

    pass

def fight(unit_1, unit_2):
    while unit_1.is_alive  and unit_2.is_alive:
        unit_2.h = unit_2.h - unit_1.a
        unit_2.ju()
        if unit_2.is_alive:
            unit_1.h = unit_1.h - unit_2.a
            unit_1.ju()

    return unit_1.is_alive

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True

    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert fight(dave, carl) == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")