from random import randint
from CONSTANTS import *
class Creature:
    def __init__(self) -> None:
        self._x= randint(CREATURE_SIZE,HEIGHT-CREATURE_SIZE)
        self._y=randint(CREATURE_SIZE,WIDTH-CREATURE_SIZE)
        self.position=(self._y,self._x)
        self.color=(0, 255, 0)
        self.size= CREATURE_SIZE
        self.direction= [randint(-1,1),randint(-1,1)]
        self.energy=randint(50,1000)
        self.isAlive=True
    def __str__(self) -> str:
        return f"""
        Position :{self.position}
        Color : {self.color}
        Crature Size : {self.size}
        """
    def move(self)->None:
        if self._x==HEIGHT-CREATURE_SIZE and self.direction[0]>0 or self._x==CREATURE_SIZE and self.direction[0]<0:
            self.direction[0]=self.direction[0]*-1
        if self._y==WIDTH-CREATURE_SIZE and self.direction[1]>0 or self._y==CREATURE_SIZE and self.direction[1]<0:
            self.direction[1]=self.direction[1]*-1
        self._x+=self.direction[0]
        self._y+=self.direction[1]
        self.position=(self._y,self._x)
        self.energy-=1
        if self.energy<=0:
            self.isAlive=False

