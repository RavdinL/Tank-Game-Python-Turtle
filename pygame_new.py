import turtle
import random
from abc import ABC, abstractmethod
import time
import os
turtle.Screen().colormode(255)
turtle.hideturtle()
#turtle.Screen().setup(width = 0.5, height = 0.5)

screen = turtle.Screen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)

field = turtle.Turtle()
field.hideturtle()
turtle.tracer(20)

t2 = turtle.Turtle()
t2.hideturtle()


t3 = turtle.Turtle()
t3.hideturtle()

t4 = turtle.Turtle()
t4.hideturtle()



def move(turt,x,y):
    turt.penup()
    turt.goto(x,y)
    turt.pendown()

move(field,-700,400)

def cell():
    field.color("lawn green")
    for i in range(4):
        field.forward(30)
        field.right(90)
def wall(x,y):
    move(field,x,y)
    field.color("chocolate1")
    field.begin_fill()
    for i in range(4):
        field.forward(30)
        field.right(90)
    field.end_fill()
wallplaces= [(28,1), (29,1), (30,1), (31,1), (28,2), (31,2), (15,3), (20,3), (21,3), (22,3), (23,3), (6,4), (7,4), (8,4), (15,4), (35,4), (36,4), (37,4), (6,5), (15,5), (35,5), (36,5), (6,6), (20,6), (26,6), (27,6), (28,6), (29,6), (20,7), (26,7), (20,8), (26,8), (20,9), (14,10), (15,10), (16,10), (20,10), (33,10), (34,10), (35,10), (36,10), (20,11), (24,11), (33,11), (34,11), (35,11), (36,11), (20,12), (3,13), (4,13), (5,13), (6,13), (9,13), (10,13), (20,13), (3,14), (6,14), (9,14), (10,14), (3,15), (17,15), (18,15), (31,15), (32,15), (3,16), (17,16), (18,16),(26,16), (24,17),  (25,17),  (26,17),  (8,18),  (8,19),  (13,19),  (32,19),  (13,20),  (22,20),  (32,20), (33,20)]
def makefield():
    for i in range(20):
        move(field,-700, 400 - 30 *i)
        for j in range(40):
            cell()
            field.forward(30)
    wallplaces= [(28,1), (29,1), (30,1), (31,1), (28,2), (31,2), (15,3), (20,3), (21,3), (22,3), (23,3), (6,4), (7,4), (8,4), (15,4), (35,4), (36,4), (37,4), (6,5), (15,5), (35,5), (36,5), (6,6), (20,6), (26,6), (27,6), (28,6), (29,6), (20,7), (26,7), (20,8), (26,8), (20,9), (14,10), (15,10), (16,10), (20,10), (33,10), (34,10), (35,10), (36,10), (20,11), (24,11), (33,11), (34,11), (35,11), (36,11), (20,12), (3,13), (4,13), (5,13), (6,13), (9,13), (10,13), (20,13), (3,14), (6,14), (9,14), (10,14), (3,15), (17,15), (18,15), (31,15), (32,15), (3,16), (17,16), (18,16),(26,16), (24,17),  (25,17),  (26,17),  (8,18),  (8,19),  (13,19),  (32,19),  (13,20),  (22,20),  (32,20), (33,20)]
    for i in wallplaces:
        wall(-730 + 30 * i[0], 430 - 30 * i[1])
makefield()
field.hideturtle()
t1 = turtle.Turtle()
t1.hideturtle()


def drawtank(x, y, color):
    t2.color(color)
    xcoord = -730 + 30 * x + 5
    ycoord = 430 - 30 * y - 5
    move(t2, xcoord, ycoord)
    t2.begin_fill()
    for i in range(4):
        t2.forward(20)
        t2.right(90)
    t2.end_fill()
    t2.color("white")

def drawitem(x,y, color):
    t1.color(color)
    xcoord = -720 + 30 * x + 5
    ycoord = 427 - 30 * y - 5
    move(t1, xcoord, ycoord)
    t1.begin_fill()
    t1.right(45)
    for i in range(4):
        t1.forward(10)
        t1.right(90)
    t1.end_fill()
    t1.left(45)
    t1.color("white")

class Tank:

    def __init__(self, speed = 5, health = 10, ammo = 0, damage = 3, x = 1, y = 1, type = "None", color = "grey"):
        self._speed = speed
        self._health = health
        self._ammo = ammo
        self._damage = damage
        self._x = x
        self._y = y
        self._type = type
        self._color = color
        drawtank(self._x, self._y, self._color)

    def getx(self):
        return self._x
    def gety(self):
        return self._y
    def gethealth(self):
        return self._health
    def getdamage(self):
        return self._damage
    def getspeed(self):
        return self._speed
    def getammo(self):
        return self._ammo
    def gettype(self):
        return self._type
    def getcolor(self):
        return self._color

    def setx(self, x):
        if type(x) == int:
            self._x = x
    def sety(self, y):
        if type(y) == int:
            self._y = y
    def sethealth(self, health):
        if type(health) == int:
            self._health = health
    def setdamage(self, damage):
        if type(damage) == int:
            self._damage = damage
    def setspeed(self, speed):
        if type(speed) == int:
            self._speed = speed
    def setammo(self, ammo):
        if type(ammo) == int:
            self._ammo = ammo
    def settype(self, type):
        self._type = type
    def setcolor(self, color):
        self._color = color

    def move(self, x, y):
        def erasetank(x,y):
            t2.color("white")
            xcoord = -730 + 30 * x + 5
            ycoord = 430 - 30 * y - 5
            move(t2, xcoord, ycoord)
            t2.begin_fill()
            for i in range(4):
                t2.forward(20)
                t2.right(90)
            t2.end_fill()
        erasetank(self.getx(),self.gety())
        drawtank(x,y, self._color)
        self._x = x
        self._y = y
class Light_Tank(Tank):
    def __init__(self, speed = 8, health = 4, ammo = 2, damage = 2, x = 1, y = 1, type = "Лёгкий", color = "grey"):
        self._speed = speed
        self._health = health
        self._ammo = ammo
        self._damage = damage
        self._x = x
        self._y = y
        self._type = type
        self._color = color
        drawtank(self._x, self._y, self._color)


class Medium_Tank(Tank):
    def __init__(self, speed = 6, health = 6, ammo = 2, damage = 3, x = 1, y = 1, type = "Средний", color = "grey"):
        self._speed = speed
        self._health = health
        self._ammo = ammo
        self._damage = damage
        self._x = x
        self._y = y
        self._type = type
        self._color = color
        drawtank(self._x, self._y, self._color)

class Heavy_Tank(Tank):
    def __init__(self, speed = 4, health = 8, ammo = 1, damage = 5, x = 1, y = 1, type = "Тяжёлый" ,color = "grey"):
        self._speed = speed
        self._health = health
        self._ammo = ammo
        self._damage = damage
        self._x = x
        self._y = y
        self._type = type
        self._color = color
        drawtank(self._x, self._y, self._color)

class Item:
    def __init__(self, x = 1, y = 1, color = "grey", type = "None", taken = False):
        self._x = x
        self._y = y
        self._color = color
        self._type = type
        self._taken = taken
        drawitem(self._x, self._y, self._color)

    def getx(self):
        return self._x
    def gety(self):
        return self._y
    def gettype(self):
        return self._type
    def getcolor(self):
        return self._color
    def gettaken(self):
        return self._taken

    def setx(self, x):
        if type(x) == int:
            self._x = x
    def sety(self, y):
        if type(y) == int:
            self._y = y
    def settype(self, type):
        self._type = type
    def setcolor(self, color):
        self._color = color
    def settaken(self, taken):
        if type(taken) == bool:
            self._taken = taken

    #Абстрактный метод
    @abstractmethod
    def itemtake(self):
        pass


class Ammo_Item(Item):
    def __init__(self, x = 1, y = 1, color = "black", type = "Ammo", taken = False):
        self._x = x
        self._y = y
        self._color = color
        self._type = type
        self._taken = taken
        drawitem(self._x, self._y, self._color)

    def itemtake(self):
        if self._taken == False:
            self._taken = True
            print("Item take!")
            return {"ammo": 1, "health": 0, "speed": 0, "damage" : 0}

        else:
            return {"ammo": 0, "health": 0, "speed": 0, "damage" : 0}

class Health_item(Item):
    def __init__(self, x = 1, y = 1, color = "green", type = "Health", taken = False):
        self._x = x
        self._y = y
        self._color = color
        self._type = type
        self._taken = taken
        drawitem(self._x, self._y, self._color)

    def itemtake(self):
        if self._taken == False:
            self._taken = True
            print("Item take!")
            return {"ammo": 0, "health": 2, "speed": 0, "damage" : 0}

        else:
            return {"ammo": 0, "health": 0, "speed": 0, "damage" : 0}

class Damage_Item(Item):
    def __init__(self, x = 1, y = 1, color = "red", type = "Damage", taken = False):
        self._x = x
        self._y = y
        self._color = color
        self._type = type
        self._taken = taken
        drawitem(self._x, self._y, self._color)

    def itemtake(self):
        if self._taken == False:
            self._taken = True
            print("Item take!")
            return {"ammo": 0, "health": 0, "speed": 0, "damage" : 1}

        else:
            return {"ammo": 0, "health": 0, "speed": 0, "damage" : 0}

class Speed_Item(Item):
    def __init__(self, x = 1, y = 1, color = "blue", type = "Speed", taken = False):
        self._x = x
        self._y = y
        self._color = color
        self._type = type
        self._taken = taken
        drawitem(self._x, self._y, self._color)

    def itemtake(self):
        if self._taken == False:
            self._taken = True
            print("Item take!")
            return {"ammo": 0, "health": 0, "speed": 2, "damage" : 0}

        else:
            return {"ammo": 0, "health": 0, "speed": 0, "damage" : 0}

itemplaces = [ (10,20), (17,8), (18,2), (18,19), (22,15), (23,6), (28,11), (28,19), (13,8), (26,13), (32,8), (13,8), (15,15), (19,6), (19,9), (19,13), (21,6), (21,9), (21,13), (23,1), (26,4), (26,13), (32,8)]
allitems = []


for i in itemplaces:
    R = random.randint(1,100)
    if R <= 60:
        allitems.append(Ammo_Item(x = i[0], y = i[1]))
    elif R > 60 and R <= 80:
        allitems.append(Health_item(x=i[0], y=i[1]))
    elif R > 80 and R <= 100:
        allitems.append(Damage_Item(x=i[0], y=i[1]))
    #else:
        #allitems.append(Speed_Item(x=i[0], y=i[1]))



tank1 = Light_Tank(x = 1, y = 1, color = "deep sky blue")
tank2 = Medium_Tank(x = 1, y = 10, color = "RoyalBlue1")
tank3 = Heavy_Tank(x = 1, y = 20, color = "medium blue")
tank4 = Light_Tank(x = 40, y = 1, color = "VioletRed1")
tank5 = Medium_Tank(x = 40, y = 10, color = "firebrick2")
tank6 = Heavy_Tank(x = 40, y = 20, color = "red4")




turtle.listen()
k = 0
remainmoves = tank1.getspeed() + 1
shooters = [False, False, False, False, False, False]
dead = [False, False, False, False, False, False]

whoturn = [[tank1.getspeed(), dead[0]], [tank2.getspeed(), dead[1]], [tank3.getspeed(), dead[2]], [tank4.getspeed(), dead[3]], [tank5.getspeed(), dead[4]], [tank6.getspeed(), dead[5]]]
j = 0
localj = 1

def k_to_turntank():
    global j, whoturn, localj, dead, shooters
    print(whoturn)
    while whoturn[j][1] == True:
        print("&&")
        j += 1
        if j == 6:
            j = 0

    d = {0: tank1, 1: tank2, 2: tank3, 3: tank4, 4: tank5, 5: tank6}
    ans = d[j]
    for i in range(6):
        if i != j:
            shooters[i] = False
    if localj == whoturn[j][0] or localj >= 8:
        j += 1
        localj = 0
    if j == 6:
        j = 0
    print(localj)
    return ans

onetime = 1
def k_to_writeturn():
    global j, remainmoves, localj, onetime
    d = {0: "Синий 1", 1: "Синий 2", 2: "Синий 3", 3: "Красный 1", 4: "Красный 2", 5: "Красный 3"}
    turntank = k_to_turntank()
    remainmoves = turntank.getspeed() - localj + onetime
    onetime = 0
    return d[j]


def playerturn():
    global remainmoves
    move(t3, 510, 300)
    t3.color("white")
    t3.begin_fill()
    for i in range (4):
        t3.forward(300)
        t3.right(90)
    t3.end_fill()
    move(t3, 520, 200)
    t3.color("black")
    t3.write("Ходит: " + k_to_writeturn(), align='left', font=('italic', 20, 'bold'))
    move(t3, 555, 60)
    t3.write("Осталось \n ходов: " + str(remainmoves), align='left', font=('italic', 20, 'bold'))


def drawcrosses():
    global dead
    def cross(x,y):
        move(t1,x,y)
        t1.width(10)
        t1.color("red")
        t1.goto(x + 150, y - 170)
        move(t1, x + 150, y)
        t1.goto(x, y - 170)
        t1.width(1)
    for i in range(6):
        if dead[i] == True:
            cross(-700 + 250 * i, -230)



def playerinfo():
    global dead
    move(t4, -715, -210)
    t4.color("MediumOrchid1")
    t4.begin_fill()
    for i in range(4):
        t4.forward(200 + 1270 * ((i - 1) % 2))
        t4.right(90)
    t4.end_fill()
    t4.color("black")
    alltanks = [tank1, tank2, tank3, tank4, tank5, tank6]
    for ij in range(6):
        move(t4, -700 + 250 * ij, -250)
        if ij <= 2:
            t4.write("Синий " + str(ij % 3 + 1), font=('italic', 18, 'bold'))
            movelittleright = 0
        else:
            t4.write("Красный " + str(ij % 3 + 1), font=('italic', 18, 'bold'))
            movelittleright = 25
        move(t4, -700 + 250 * ij, -280)
        t4.write("Здоровье: " + str(alltanks[ij].gethealth()), font=('italic', 18, 'bold'))
        move(t4, -700 + 250 * ij, -310)
        t4.write("Боеприпасы: " + str(alltanks[ij].getammo()), font=('italic', 18, 'bold'))
        move(t4, -700 + 250 * ij, -340)
        t4.write("Скорость: " + str(alltanks[ij].getspeed()), font=('italic', 18, 'bold'))
        move(t4, -700 + 250 * ij, -370)
        t4.write("Урон: " + str(alltanks[ij].getdamage()), font=('italic', 18, 'bold'))
        move(t4, -700 + 250 * ij, -400)
        t4.write("Тип: " + alltanks[ij].gettype(), font=('italic', 18, 'bold'))

        move(t4, -580 + 250 * ij + movelittleright, -225)
        t4.color(alltanks[ij].getcolor())
        t4.begin_fill()
        for b in range(4):
            t4.forward(20)
            t4.right(90)
        t4.end_fill()
        t4.color("black")
    drawcrosses()

def checktake(turntank):
    global allitems, itemplaces
    #turntank = k_to_turntank()

    if (turntank.getx(), turntank.gety()) in itemplaces:
        for i in allitems:
            if i.getx() == turntank.getx() and i.gety() == turntank.gety():
                d = i.itemtake()
                print(d)
                if d["ammo"] != 0 or d["health"] != 0 or d["damage"] != 0 or d["speed"] != 0:
                    turntank.setammo(turntank.getammo() + d["ammo"])
                    turntank.sethealth(turntank.gethealth() + d["health"])
                    turntank.setdamage(turntank.getdamage() + d["damage"])
                    #turntank.speed += d["speed"]
                    playerinfo()
stopgame = False
def checkwin():
    global dead, stopgame
    def win(team):
        move(t4, -100, 0)
        if team == "Blue":
            t4.color("blue")
        else:
            t4.color("red")
        t4.write(team + " won!", font=('italic',200, 'bold'), align = "center")
        stopgame = True

    if dead[0] == True and dead[1] == True and dead[2] == True:
        win("Red")
    if dead[3] == True and dead[4] == True and dead[5] == True:
        win("Blue")

def checkdeath():
    global dead, k, whoturn
    d = {tank1: 0, tank2: 1, tank3: 2, tank4: 3, tank5: 4, tank6: 5}
    for turntank in d.keys():
        if turntank.gethealth() <= 0:
            turntank.sethealth(0)
            if dead[d[turntank]] == False:
                k -= turntank.getspeed()

            dead[d[turntank]] = True
            whoturn[d[turntank]][1] = True
            turntank.setspeed(0)
            turntank.setammo(0)
            turntank.setdamage(0)
            turntank.setcolor("white")
            turntank.settype("Уничтожен")
            turntank.move(-10, -10)
            turntank.setx(-10)
            turntank.sety(-10)
            checkwin()

def shot():
    global shooters

    turntank = k_to_turntank()
    maxshotdistance = 5
    d = {tank1: 0, tank2: 1, tank3: 2, tank4: 3, tank5: 4, tank6: 5}
    if turntank.getammo() > 0 and shooters[d[turntank]] == False:
        shooters[d[turntank]] = True
        print("shot")
        turntank.setammo(turntank.getammo() - 1)
        if turntank in [tank1, tank2, tank3]:
            r1 = abs(turntank.getx() - tank4.getx()) + abs(turntank.gety() - tank4.gety())
            r2 = abs(turntank.getx() - tank5.getx()) + abs(turntank.gety() - tank5.gety())
            r3 = abs(turntank.getx() - tank6.getx()) + abs(turntank.gety() - tank6.gety())
            if r1 <= maxshotdistance + 1 or r2 <= maxshotdistance + 1 or r3 <= maxshotdistance + 1:
                r = min(r1,r2,r3)
                if r == r1:
                    tank4.sethealth(tank4.gethealth() - turntank.getdamage())

                elif r == r2:
                    tank5.sethealth(tank5.gethealth() - turntank.getdamage())

                else:
                    tank6.sethealth(tank6.gethealth() - turntank.getdamage())
                print("good shot")
                checkdeath()

        if turntank in [tank4, tank5, tank6]:
            r1 = abs(turntank.getx() - tank1.getx()) + abs(turntank.gety() - tank1.gety())
            r2 = abs(turntank.getx() - tank2.getx()) + abs(turntank.gety() - tank2.gety())
            r3 = abs(turntank.getx() - tank3.getx()) + abs(turntank.gety() - tank3.gety())
            if r1 <= maxshotdistance + 1 or r2 <= maxshotdistance + 1 or r3 <= maxshotdistance + 1:
                r = min(r1,r2,r3)
                if r == r1:
                    tank1.sethealth(tank1.gethealth() - turntank.getdamage())
                elif r == r2:
                    tank2.sethealth(tank2.gethealth() - turntank.getdamage())
                else:
                    tank3.sethealth(tank3.gethealth() - turntank.getdamage())
                checkdeath()
                print("good shot")
        playerinfo()
def right():
    global k, localj, stopgame
    #checktake()
    turntank = k_to_turntank()
    checkdeath()
    playerturn()


    if (turntank.getx() + 1, turntank.gety()) not in wallplaces and turntank.getx() >= 1 and turntank.getx() + 1 <= 40 and turntank.gety() >= 1 and turntank.gety() <= 20:
        turntank.move(turntank.getx() + 1, turntank.gety())
        k+=1
        localj += 1

    if stopgame == True:
        turtle.done()
    #playerturn()
    checktake(turntank)
    #print(k)


def left():
    global k, localj, stopgame
    #checktake()
    turntank = k_to_turntank()
    checkdeath()
    playerturn()

    if (turntank.getx() - 1 , turntank.gety()) not in wallplaces and turntank.getx() - 1 >= 1 and turntank.getx() <= 40 and turntank.gety() >= 1 and turntank.gety() <= 20:
        turntank.move(turntank.getx() - 1, turntank.gety())
        k += 1
        localj += 1

    if stopgame == True:
        turtle.done()

    checktake(turntank)
    #print(k)
def up():
    global k, localj, stopgame
    #checktake()
    turntank = k_to_turntank()
    checkdeath()
    playerturn()

    if (turntank.getx() , turntank.gety() - 1) not in wallplaces and turntank.getx() >= 1 and turntank.getx() <= 40 and turntank.gety() - 1 >= 1 and turntank.gety() <= 20:
        turntank.move(turntank.getx(), turntank.gety() - 1)
        k += 1
        localj += 1

    if stopgame == True:
        turtle.done()
    #playerturn()
    checktake(turntank)
    #print(k)

def down():
    global k, localj, stopgame
    #checktake()
    turntank = k_to_turntank()
    checkdeath()
    playerturn()


    if (turntank.getx() , turntank.gety() + 1) not in wallplaces and turntank.getx() >= 1 and turntank.getx() <= 40 and turntank.gety() >= 1 and turntank.gety() + 1 <= 20:
        turntank.move(turntank.getx(), turntank.gety() + 1)
        k += 1
        localj += 1

    if stopgame == True:
        turtle.done()
    #playerturn()
    checktake(turntank)
    #print(k)
turtle.onkey(right, "Right")
turtle.onkey(left, "Left")
turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(playerinfo, "Tab")
turtle.onkey(shot, "space")
playerturn()
playerinfo()
turtle.done()

print(k)