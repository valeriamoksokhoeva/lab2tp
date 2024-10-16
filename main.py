from abc import ABC, abstractmethod
class GameObject:
    def __init__(self, id, name, x, y):
        self._id = id
        self._name = name
        self._x = x
        self._y = y
    def getId(self):
        return self._id
    def getName(self):
        return self._name
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    
class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass

class Moveable(ABC):
    @abstractmethod
    def move(self, x, y):
        pass

class Building(GameObject):
    def __init__(self, id, name, x, y):
        super().__init__(id, name, x, y)
        self._built = False
    def isBuilt(self):
        return self._built
    def build(self):
        self._built = True
        print(f"Building {self._name} was built")


class Unit(GameObject):
    def __init__(self, id, name, x, y, xp, power):
        super().__init__(id, name, x, y)
        self._alive = True
        self._xp = xp
        self._power = power
    def isAlive(self):
        return self._alive
    def getHp(self):
        return self._xp
    def receiveDamage(self, damage):
        if self._xp - damage >= 0:
            self._xp -= damage
        else:
            self._alive = False
            self._xp = 0
            print(f"Unit {self._name} died")


class Fort(Building, Attacker):
    def __init__(self, id, name, x, y, power):
        super().__init__(id, name, x, y)
        self._power = power
    def attack(self, unit):
        unit.receiveDamage(self._power)
        print(f"Fort '{self._name}' attacked {unit._name}")
    
class MobileHome(Building, Moveable):
    def move(self, x, y):
        self._x += x
        self._y += y
        print(f"MobileHome '{self._name}' moved to {self._x, self._y}")



class Archer(Unit, Attacker, Moveable):
    def attack(self, unit):
        unit.receiveDamage(self._power)
        print(f"{self._name} attacked {unit._name}")
    def move(self, x, y):
        self._x += x
        self._y += y
        print(f"{self._name} moved to {self._x, self._y}")




archer = Archer(123, "Mike", 1, 1, 100, 10)
unit = Unit(456, 'Bob', 3, 4, 55, 4)

fort = Fort(789, 'SuperFort', 5, 8, 12)
mobilehome = MobileHome(999, 'SuperMobileHome', 10, 10)

fort.attack(unit)
archer.attack(unit)

mobilehome.move(4, 4)
archer.move(3, 5)
house = Building(333, 'Home', 0, 0)
house.build()

fort.attack(archer)
print(house.isBuilt())
print(unit.getHp())
print(archer.getHp())

