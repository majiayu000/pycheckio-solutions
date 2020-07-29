#!/usr/bin/env checkio --domain=py run army-battles
# Taken from mission The Warriors


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
class Army:
    def __init__(self):
        self._units = []

    def __getitem__(self, index):
            return self._units[index]

    def __len__(self):
            return len(self._units)

    def add_units(self, unit, count):
            self._units.extend(unit() for _ in range(count))


    



class Battle:

    def fight(self,a1,a2):
        i1 = i2 = 0
        try:
            while True:
                u1, u2 = a1[i1], a2[i2]
                fight(u1, u2)
                i1 += not u1.is_alive
                i2 += not u2.is_alive
        except IndexError:
            return any(u.is_alive for u in reversed(a1))





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
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
