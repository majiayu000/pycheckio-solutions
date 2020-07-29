#!/usr/bin/env checkio --domain=py run the-lancers
# Taken from mission The Vampires

# Taken from mission The Defenders

# Taken from mission Army Battles

# Taken from mission The Warriors


class Warrior:

    health: int = 50
    attack: int = 5
    d: int = 0
    vampirism: float = 0
    p :float =0
    is_alive: bool = True

    def ju(self):
        if self.health > 0:
            self.is_alive = True
        else:
            self.is_alive = False
    pass

class Knight(Warrior):

    attack: int = 7

    pass
class Defender(Warrior):
    health: int = 60
    attack: int = 3
    d: int = 2

    pass
class Vampire(Warrior):
    health: int = 40
    attack: int = 4
    vampirism: float= 0.5

    pass
class Lancer(Warrior):
    health: int = 50
    attack: int = 6
    vampirism: float= 0.5
    p : float = 0.5

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
                if i1 <  a1.__len__() - 1:
                    u3 = a1[i1+1]
                    if i2 < a2.__len__() - 1:
                          u4 = a2[i2+1]
                          fight1(u1,u2,u3,u4)
                    else:
                        fight2(u1,u2,u3)
                elif i2 < a2.__len__() - 1:
                    u4 = a2[i2 + 1]
                    fight3(u1,u2,u4)

                else:
                    fight(u1, u2)
                i1 += not u1.is_alive
                i2 += not u2.is_alive
        except IndexError:
            return any(u.is_alive for u in reversed(a1))





def fight(unit_1, unit_2):
    while unit_1.is_alive  and unit_2.is_alive:
        if unit_1.attack > unit_2.d:
          unit_2.health = unit_2.health - unit_1.attack + unit_2.d
          unit_1.health = unit_1.health + (unit_1.attack - unit_2.d) * unit_1.vampirism
          unit_2.ju()
        if unit_2.is_alive:
            if unit_2.attack > unit_1.d:
                unit_1.health = unit_1.health - unit_2.attack +unit_1.d
                unit_2.health = unit_2.health + (unit_2.attack - unit_1.d) * unit_2.vampirism
                unit_1.ju()


    return unit_1.is_alive


def fight1(unit_1, unit_2,unit_3,u4):
    while unit_1.is_alive and unit_2.is_alive:
        if unit_1.attack > unit_2.d:
            unit_2.health = unit_2.health - unit_1.attack + unit_2.d
            unit_1.health = unit_1.health + (unit_1.attack - unit_2.d) * unit_1.vampirism
            unit_2.ju()
        if unit_1.attack * unit_1.p > unit_3.d:
            unit_3.health = unit_3.health + unit_3.d - unit_1.attack * unit_1.p
        if unit_2.is_alive:
            if unit_2.attack > unit_1.d:
                unit_1.health = unit_1.health - unit_2.attack + unit_1.d
                unit_2.health = unit_2.health + (unit_2.attack - unit_1.d) * unit_2.vampirism
                unit_1.ju()
        if unit_2.attack * unit_2.p > u4.d:
            u4.health = u4.health + u4.d - unit_2.attack * unit_2.p    

    return unit_1.is_alive

def fight3(unit_1, unit_2,u4):
    while unit_1.is_alive and unit_2.is_alive:
        if unit_1.attack > unit_2.d:
            unit_2.health = unit_2.health - unit_1.attack + unit_2.d
            unit_1.health = unit_1.health + (unit_1.attack - unit_2.d) * unit_1.vampirism
            unit_2.ju()
        
        if unit_2.is_alive:
            if unit_2.attack > unit_1.d:
                unit_1.health = unit_1.health - unit_2.attack + unit_1.d
                unit_2.health = unit_2.health + (unit_2.attack - unit_1.d) * unit_2.vampirism
                unit_1.ju()
        if unit_2.attack * unit_2.p > u4.d:
            u4.health = u4.health + u4.d - unit_2.attack * unit_2.p

    return unit_1.is_alive

def fight2(unit_1, unit_2,u3):
    while unit_1.is_alive and unit_2.is_alive:
        if unit_1.attack > unit_2.d:
            unit_2.health = unit_2.health - unit_1.attack + unit_2.d
            unit_1.health = unit_1.health + (unit_1.attack - unit_2.d) * unit_1.vampirism
            unit_2.ju()
        if unit_1.attack * unit_1.p > u3.d:
            u3.health = u3.health + u3.d - unit_1.attack * unit_1.p
        if unit_2.is_alive:
            if unit_2.attack > unit_1.d:
                unit_1.health = unit_1.health - unit_2.attack + unit_1.d
                unit_2.health = unit_2.health + (unit_2.attack - unit_1.d) * unit_2.vampirism
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
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")