#!/usr/bin/env pybricks-micropython
# tohole musí být 1. rádek

# importy
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch
import sys
# import img2num as imgnm



# setup kostka, stopky
ev3 = EV3Brick()
stop_w = StopWatch()

# setup touch senzory
touch_sensor = TouchSensor(Port.S4)
touch_spust = TouchSensor(Port.S3)

# setup motory 
M_papir = Motor(Port.A)
M_vozik = Motor(Port.B)
M_pero = Motor(Port.C)

# setup is_up (pro řádek), cerna (is_up pro sloupce)
is_up = True
cerna = False
docasna = 0

# setup odsazení od okraje, zespodu
set_dal = 0
dal = set_dal
paper = 0

# setup velikost obrázku, potřeba vyladit k sobě
zmena_p = 2
zmena_carka = zmena_p

# setup toho, co chci tisknout
# robot = imgnm.Nums()
robot = [0, 1, 39, -1, 0, 2, 37, 1, -1, 0, 2, 2, 33, 2, 1, -1, 0, 2, 2, 33, 2, 1, -1, 0, 2, 2, 3, 12, 4, 11, 3, 2, 1, -1, 0, 2, 2, 3, 11, 6, 10, 3, 2, 1, -1, 0, 2, 2, 3, 10, 8, 9, 3, 2, 1, -1, 0, 2, 2, 3, 10, 8, 9, 3, 2, 1, -1, 0, 2, 2, 3, 10, 8, 9, 3, 2, 1, -1, 0, 2, 2, 3, 10, 8, 9, 3, 2, 1, -1, 0, 2, 2, 3, 10, 8, 9, 3, 2, 1, -1, 0, 2, 2, 3, 10, 8, 9, 3, 2, 1, -1, 0, 2, 2, 3, 10, 8, 9, 3, 2, 1, -1, 0, 2, 2, 3, 10, 8, 9, 3, 2, 1, -1, 0, 2, 2, 3, 10, 8, 9, 3, 2, 1, -1, 0, 2, 2, 3, 10, 20, 2, 1, -1, 0, 2, 2, 3, 10, 20, 2, 1, -1, 0, 2, 2, 3, 10, 20, 2, 1, -1, 0, 2, 2, 3, 10, 2, 15, 3, 2, 1, -1, 0, 2, 2, 3, 10, 2, 15, 3, 2, 1, -1, 0, 2, 2, 3, 10, 2, 15, 3, 2, 1, -1, 0, 2, 2, 3, 10, 2, 15, 3, 2, 1, -1, 0, 2, 2, 3, 10, 2, 15, 3, 2, 1, -1, 0, 2, 2, 3, 10, 2, 15, 3, 2, 1, -1, 0, 2, 2, 3, 10, 8, 9, 3, 2, 1, -1, 0, 2, 2, 3, 10, 8, 9, 3, 2, 1, -1, 0, 2, 2, 3, 10, 8, 9, 3, 2, 1, -1, 0, 2, 2, 3, 10, 8, 9, 3, 2, 1, -1, 0, 2, 2, 3, 10, 8, 9, 3, 2, 1, -1, 0, 2, 2, 3, 10, 8, 9, 3, 2, 1, -1, 0, 2, 2, 3, 10, 8, 9, 3, 2, 1, -1, 0, 2, 2, 4, 9, 8, 9, 3, 2, 1, -1, 0, 2, 2, 4, 9, 8, 8, 4, 2, 1, -1, 0, 2, 2, 5, 8, 8, 7, 4, 2, 2, -1, 0, 3, 2, 5, 7, 8, 6, 5, 1, 3, -1, 0, 4, 2, 5, 6, 8, 6, 4, 2, 3, -1, 0, 4, 2, 6, 5, 8, 5, 4, 2, 4, -1, 0, 5, 2, 6, 4, 8, 4, 4, 2, 5, -1, 0, 6, 2, 6, 3, 8, 3, 4, 2, 6, -1, 0, 7, 2, 6, 2, 7, 3, 4, 2, 7, -1, 0, 8, 3, 5, 2, 5, 3, 4, 2, 8, -1, 0, 10, 2, 16, 3, 9, -1, 0, 11, 3, 13, 3, 10, -1, 0, 12, 3, 10, 3, 12, -1, 0, 14, 4, 5, 3, 14, -1, 0, 16, 8, 16, -1, 0, 18, 4, 18, -1, 0]

# setup aktuální číslo řádku, celkem (potřeba dopočítat), pro procenta
cislo_radku = 0
pocet_radku = 0
for a in robot:
    if a == -1:
        pocet_radku = pocet_radku + 1
print(pocet_radku)


# chytrá funukce na zvednutí propisky (testuje, jestli není)
##################################################################
# how_much může dělat problémy
def push_up():
    global is_up
    #global M_pero
    if is_up == False:
        M_pero.run_target(200, 40)
        is_up = True

        
# chytrá funukce na dolů propisky (testuje, jestli není)
def push_down(): 
    global is_up
    if is_up == True:
        M_pero.run_target(200, 0)
        is_up = False

# dojede na začátek 
def jdi_na():
    M_vozik.run(120)
    while True:
        if touch_sensor.pressed():
            M_vozik.brake()
            M_vozik.reset_angle(0)
            break 

# udělá nový řádek
def NRadek():
    global paper
    global dal
    global cislo_radku
    dal = set_dal
    push_up()
    #push_up()
    cislo_radku = cislo_radku + 1
    #M_pero.run_target(100, 0)
    # print ("\x1b[K",  2(cislo_radku/pocet_radku)*100,"%", cislo_radku, ". radek", stop_w.time()/60000, "ETA:", (1-(cislo_radku/pocet_radku)) * (stop_w.time() / 60000), end="\r" )
    procenta = (cislo_radku/pocet_radku)*100
    print (procenta,"%", cislo_radku, ". radek", stop_w.time()/60000)
    zbyv_cas = ((stop_w.time()/60000) / cislo_radku) * (pocet_radku - cislo_radku)
    print("zbývající čas:", zbyv_cas)
    print()
    jdi_na()
    paper = paper - (zmena_p * 2)
    M_papir.run_target(60, paper)

# posune vozikem o jednu jednotku
def carka(move):
    global dal
    dal = dal - (zmena_carka * move)

    M_vozik.run_target(100, dal)

# main loop
def Print_Color(color):
    global cerna 
    for e in color:
        if e == -1:
            push_up()
            NRadek()
            cerna = False
            continue
        if cerna == True:
            push_down()
        else:
            #cerna == False:
            push_up()

        carka(e)
        cerna = not cerna

        
# udělá nový řádek
def NDRadek():
    global paper
    global dal
    global cislo_radku
    dal = set_dal
    push_up()
    #push_up()
    # cislo_radku = cislo_radku + 1
    #M_pero.run_target(100, 0)
    print("odseknuto", end = "\r")
    # jdi_na()
    paper = paper - (zmena_p * 1)
    M_papir.run_target(60, paper)




# aby se uvolnil M_paper
for a in range(5):
    NDRadek()

# start všeho
M_papir.reset_angle(0)
M_pero.run_target(200, 40)
jdi_na()

# tisk
Print_Color(robot)
push_up(400)


# po dokončení píp
ev3.speaker.beep(frequency=440, duration=10000)
