from random import randint
from CONSTANTS import *
class Food:
    def __init__(self) -> None:
        self._x=randint(FOOD_SIZE,HEIGHT-FOOD_SIZE)
        self._y=randint(FOOD_SIZE,WIDTH-FOOD_SIZE)
        self.position=(self._y,self._x)
        self.isEaten=False
        self.color=FOOD_COLOR
        self.size=FOOD_SIZE
    def __str__(self) -> str:
        return f"""
        Position : {self.position}
        isEaten : {self.isEaten}
        """