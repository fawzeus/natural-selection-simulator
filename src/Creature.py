from random import randint,choice,random
from CONSTANTS import *
from math import pi,sin,cos,exp,atan2
import utils
class Creature:
    def __init__(self,X=None,Y=None,color=None,speed=None,size=None,type=None,sensation=None) -> None:
        self.age=0
        if sensation:
            self.sensation_area=sensation
        else:
            self.sensation_area = 50
        self.target=None
        self.moving_to_target=False
        if type:
            self.type=type
        else:
            self.type=0
        if size:
            self.size=size
        else:
            self.size= CREATURE_SIZE
        self.angle=random()*2*pi
        if speed:
            self.speed=speed
        else:
            self.speed=1
        if X:
            self._x=X
        else:
            self._x= randint(self.size,HEIGHT-self.size)
        if Y:
            self._y=Y
        else:
            self._y=randint(self.size,HEIGHT-self.size)
        self.position=(self._y,self._x)
        if color:
            self.color=color
        else:
            self.color=(0, 255, 0)
        self.direction= [sin(self.angle),cos(self.angle)]
        self.energy=randint(50,1000)
        self.isAlive=True
        self.reproduce_probability=0.4
        self.foodEaten=0
    def __str__(self) -> str:
        return f"""
        Position :{self.position}
        Color : {self.color}
        Crature Size : {self.size}
        """
    def move(self)->None:
        if self._x>=HEIGHT-self.size and self.direction[0]>0 :
            self.angle= random()*pi+pi
            self.direction= [sin(self.angle),cos(self.angle)]
        if self._x<=self.size and self.direction[0]<0:
            self.angle= random()*pi
            self.direction= [sin(self.angle),cos(self.angle)]
        if self._y>=WIDTH-self.size and self.direction[1]>0 :
            self.angle= random()*pi/2+pi
            self.direction= [sin(self.angle),cos(self.angle)]
        if self._y<=self.size and self.direction[1]<0:
            self.angle= random()*pi/2*choice([-1,1])
            self.direction= [sin(self.angle),cos(self.angle)]
        self._x+=self.speed*self.direction[0]
        self._y+=self.speed*self.direction[1]
        self.position=(self._y,self._x)
        #self.energy-=1
        #if self.energy<=0:
        #    self.isAlive=False
    def multiply(self):
        size=None
        speed=None
        color=None
        type=None
        sensation=None
        if self.type==0:
            if random()>0.2:
                size=randint(12,15)+int(0.1*self.size)
                speed=(0.15*random()+0.9)*self.speed
                color=(0,255,0)
                type=0
                sensation=(0.35*random()+0.9)*self.sensation_area
            else:
                size=randint(12,15)
                speed=(0.2*random()+0.9)*self.speed
                color=(int(255*exp(-speed/5)),0,0)
                type=1
                sensation=(0.25*random()+0.9)*self.sensation_area
        else:
            size=randint(12,15)
            speed=(0.2*random()+0.9)*self.speed
            color=(int(255*exp(-speed/5)),0,0)
            sensation=(0.25*random()+0.9)*self.sensation_area
            type=1
        return Creature(self._x,self._y,color=color,speed=speed,size=size,type=type,sensation=sensation)
    def scan(self,foods):
        if len(foods) == 0 or self.moving_to_target==True:
            return
        myy, myx = self.position
        targeted_Food=[]
        for food in foods:
            if utils.distance(self.position, food.position) <= self.sensation_area:
                targeted_Food.append(food)
        if len(targeted_Food)==0:
            return
        nearest_food = min(targeted_Food, key=lambda food: utils.distance(self.position, food.position))
        y, x = nearest_food.position
        y_diff, x_diff = y - myy, x - myx

        angle = atan2(x_diff, y_diff)  # Use atan2 for more accurate angle calculation
        self.moving_to_target=True
        self.angle = angle
        self.target=[y,x]
        self.direction = [sin(angle), cos(angle)]
    def check_for_target_existance(self,foods):
        if self.moving_to_target==False:
            return
        existed=False
        for food in foods:
            y,x=food.position
            #print(self.target)
            if y==self.target[0] and x==self.target[1]:
                existed=True
        if not existed:
            self.target=None
            self.moving_to_target=False