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
# touch_spust = TouchSensor(Port.S3)

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
zmena_p = 5
zmena_carka = zmena_p   #?s
zmena_radek = zmena_p * 1.5

# setup toho, co chci tisknout
robot = [0, 14, 8, 6, 3, 18, 6, 13, 12, 15, 10, 13, 14, 14, 4, -1, 0, 15, 7, 6, 3, 18, 5, 15, 10, 16, 8, 16, 11, 16, 4, -1, 0, 16, 6, 6, 3, 18, 4, 17, 8, 17, 7, 18, 9, 17, 4, -1, 0, 17, 5, 6, 3, 18, 3, 19, 6, 18, 7, 18, 8, 18, 4, -1, 0, 17, 5, 6, 3, 18, 3, 19, 6, 18, 7, 19, 6, 19, 4, -1, 11, 6, 5, 6, 9, 6, 9, 6, 7, 6, 5, 7, 7, 5, 7, 5, 8, 6, 6, 7, 6, 6, 4, -1, 11, 6, 5, 6, 9, 6, 9, 6, 7, 6, 5, 6, 8, 5, 7, 5, 8, 6, 6, 6, 7, 6, 4, -1, 11, 6, 5, 6, 9, 6, 9, 6, 7, 6, 5, 6, 8, 6, 6, 5, 8, 6, 6, 5, 8, 6, 4, -1, 11, 6, 5, 6, 9, 6, 9, 6, 7, 6, 6, 21, 4, 5, 8, 6, 6, 5, 8, 6, 4, -1, 11, 6, 5, 6, 9, 6, 9, 6, 7, 6, 6, 21, 4, 5, 8, 6, 6, 6, 7, 6, 4, -1, 11, 6, 5, 6, 9, 6, 9, 6, 7, 6, 6, 21, 4, 5, 8, 6, 6, 22, 1, -1, 11, 6, 5, 6, 9, 6, 9, 6, 7, 6, 5, 22, 4, 5, 8, 6, 7, 21, 1, -1, 11, 6, 5, 6, 9, 6, 9, 6, 7, 6, 5, 22, 4, 5, 8, 6, 7, 21, 1, -1, 11, 6, 5, 6, 9, 6, 9, 6, 7, 6, 4, 6, 9, 5, 7, 5, 8, 6, 7, 21, 1, -1, 11, 6, 5, 6, 9, 6, 9, 6, 7, 6, 4, 6, 9, 5, 7, 5, 8, 6, 6, 22, 1, -1, 11, 6, 5, 6, 9, 6, 9, 6, 7, 6, 4, 7, 7, 6, 7, 6, 7, 6, 5, 23, 1, -1, 0, 17, 5, 6, 9, 6, 9, 19, 5, 19, 7, 19, 4, 7, 8, 6, 4, -1, 0, 17, 5, 6, 9, 6, 9, 19, 5, 19, 7, 18, 4, 7, 9, 6, 4, -1, 0, 16, 6, 6, 9, 6, 10, 17, 7, 18, 7, 18, 4, 6, 10, 6, 4, -1, 0, 15, 7, 6, 9, 6, 11, 15, 9, 17, 8, 16, 4, 6, 11, 6, 4, -1, 0, 13, 9, 6, 9, 6, 12, 12, 13, 15, 10, 12, 6, 6, 12, 5, 4, -1, 150, -1, 150, -1, 150, -1, 150, -1, 150, -1, 150, -1, 150, -1, 150, -1, 150, -1, 150, -1, 150, -1, 115, 29, 6, -1, 1, 5, 8, 6, 12, 4, 22, 14, 42, 30, 6, -1, 1, 6, 7, 6, 9, 10, 16, 17, 42, 30, 6, -1, 1, 6, 7, 6, 7, 13, 13, 19, 42, 30, 6, -1, 1, 6, 7, 6, 6, 15, 11, 20, 42, 4, 21, 5, 6, -1, 1, 6, 7, 6, 6, 16, 9, 21, 41, 5, 5, 2, 6, 2, 6, 4, 7, -1, 1, 6, 7, 6, 5, 8, 1, 9, 7, 10, 6, 6, 41, 4, 5, 4, 3, 6, 4, 4, 7, -1, 1, 6, 7, 6, 5, 6, 5, 7, 7, 7, 9, 6, 41, 4, 4, 5, 2, 8, 3, 4, 7, -1, 1, 6, 7, 6, 4, 6, 7, 6, 6, 7, 10, 6, 41, 4, 4, 5, 1, 10, 2, 4, 7, -1, 1, 19, 4, 6, 8, 5, 6, 6, 11, 6, 41, 4, 3, 5, 1, 11, 1, 4, 8, -1, 1, 19, 4, 6, 8, 5, 6, 6, 11, 6, 40, 4, 4, 4, 2, 5, 2, 4, 1, 4, 8, -1, 1, 18, 5, 6, 7, 7, 5, 6, 11, 6, 40, 4, 3, 5, 2, 4, 3, 4, 1, 4, 8, -1, 1, 17, 6, 22, 3, 6, 11, 6, 40, 4, 3, 4, 3, 4, 2, 5, 1, 4, 8, -1, 1, 16, 7, 22, 3, 6, 11, 6, 40, 4, 2, 5, 3, 4, 1, 5, 2, 4, 8, -1, 1, 6, 17, 22, 3, 6, 11, 6, 40, 4, 2, 4, 4, 10, 1, 4, 9, -1, 1, 6, 17, 22, 4, 6, 10, 6, 39, 4, 2, 5, 4, 9, 2, 4, 9, -1, 1, 7, 16, 22, 4, 8, 8, 6, 39, 4, 3, 3, 6, 7, 3, 4, 9, -1, 1, 17, 6, 6, 8, 5, 8, 21, 39, 4, 3, 2, 9, 3, 5, 4, 9, -1, 2, 16, 6, 6, 8, 5, 9, 20, 39, 4, 21, 5, 9, -1, 3, 15, 6, 6, 8, 5, 10, 19, 38, 5, 21, 4, 10, -1, 4, 14, 6, 6, 8, 5, 11, 18, 38, 30, 10, -1, 6, 12, 6, 6, 8, 5, 13, 16, 38, 30, 10, -1, 110, 29, 11, -1, 111, 27, 9, 2, 1, -1, 144, 5, 1, -1, 142, 8, -1, 140, 10, -1, 109, 39, 2, -1, 107, 38, 5, -1, 105, 38, 7, -1, 103, 38, 9, -1, 101, 9, 40, -1, 100, 8, 39, 2, 1, -1, 98, 8, 38, 5, 1, -1, 96, 8, 38, 8, -1, 3, 13, 8, 13, 8, 12, 10, 13, 15, 8, 37, 10, -1, 2, 14, 7, 14, 6, 15, 7, 15, 14, 54, 2, -1, 1, 15, 6, 15, 6, 16, 6, 15, 12, 53, 5, -1, 1, 15, 6, 15, 5, 17, 5, 16, 11, 52, 7, -1, 1, 15, 5, 16, 5, 18, 4, 15, 11, 51, 9, -1, 1, 6, 14, 6, 15, 6, 6, 6, 4, 6, 80, -1, 1, 6, 14, 6, 15, 6, 6, 6, 4, 6, 80, -1, 1, 6, 14, 7, 14, 6, 6, 6, 4, 6, 80, -1, 1, 14, 7, 14, 6, 6, 6, 6, 4, 15, 18, 4, 10, 4, 10, 4, 10, 4, 7, -1, 1, 15, 6, 15, 5, 6, 6, 6, 4, 16, 16, 6, 7, 7, 7, 7, 7, 7, 6, -1, 1, 16, 5, 16, 4, 6, 6, 6, 5, 15, 15, 8, 6, 8, 6, 8, 6, 8, 5, -1, 2, 15, 6, 15, 4, 6, 6, 6, 6, 15, 13, 9, 5, 9, 5, 9, 5, 9, 5, -1, 4, 14, 6, 14, 4, 6, 6, 6, 7, 14, 13, 10, 3, 11, 3, 10, 4, 10, 5, -1, 12, 6, 15, 5, 4, 6, 6, 6, 15, 6, 12, 5, 2, 4, 3, 5, 2, 4, 3, 4, 2, 5, 3, 4, 2, 4, 5, -1, 12, 6, 15, 5, 4, 6, 6, 6, 15, 6, 12, 4, 3, 4, 3, 4, 2, 5, 3, 4, 2, 5, 2, 5, 2, 4, 5, -1, 12, 6, 15, 5, 4, 6, 6, 6, 15, 6, 12, 4, 2, 5, 3, 4, 2, 4, 4, 4, 2, 4, 3, 4, 3, 4, 5, -1, 1, 17, 3, 17, 4, 18, 4, 17, 12, 4, 1, 5, 4, 4, 1, 5, 4, 4, 1, 5, 3, 5, 1, 5, 5, -1, 1, 17, 3, 17, 4, 17, 5, 17, 12, 10, 4, 10, 4, 9, 5, 9, 6, -1, 1, 17, 3, 17, 5, 16, 5, 17, 12, 9, 5, 9, 5, 9, 5, 9, 6, -1, 1, 17, 3, 17, 6, 14, 6, 17, 13, 7, 7, 7, 7, 7, 7, 7, 7, -1, 1, 17, 3, 17, 7, 11, 8, 17, 14, 5, 9, 4, 10, 4, 10, 4, 9, -1, 0]   #roboden.jpg
sirka = 98


# setup aktuální číslo řádku, celkem dopočítáno, pro procenta
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
        M_pero.run_target(200, 20)
        is_up = True

        
# chytrá funukce na dolů propisky (testuje, jestli není)
def push_down(): 
    global is_up
    if is_up == True:
        M_pero.run_target(200, 0)
        is_up = False

# dojede na začátek 
def jdi_na():
    M_vozik.run(150)                # >>>>>>>>>>>>>>>>>>>>>>>>>> když jsem s, tak 400, jinak 200
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
    procenta = round((cislo_radku/pocet_radku) * 100, 2)
    cas = round((stop_w.time()/60000), 5)
    print (cislo_radku,". radek", procenta,"%", cas, "min")

    zbyv_cas = (cas / cislo_radku) * (pocet_radku - cislo_radku)
    print("zbývající čas:", zbyv_cas, "min")
    print()

    jdi_na()
    paper = paper - (zmena_radek)
    M_papir.run_target(60, paper)

# posune vozikem o jednu jednotku
def carka(move, fast = False):
    global dal
    dal = dal - (zmena_carka * move)
    if fast == True:
        M_vozik.run_target(240, dal) # DOLADIT !!!!!!!
    elif fast == False:
        M_vozik.run_target(120, dal) # DOLADIT !!!!!!!
    else:
        print("Error, už zase? Jinak, máš problém s rychlopohybem, a tím, co do něj posíláš (fast)")
# main loop
def Print_Color(color):
    global cerna 
    for e in color:
        if e == -1:
            push_up()
            NRadek()
            cerna = False
            continue
        if e == sirka:
            push_up()
            NRadek()
            cerna = False
            continue
        
        if cerna == True:
            push_down()
        else:
            #cerna == False:
            push_up()
        if cerna == False and e > 10:
            carka(e, True)
        else:
            carka(e, False)
        cerna = not cerna

        
# udělá nový řádek
def NDRadek():
    global paper
    global zmena_radek
    # global dal
    # global cislo_radku
    dal = set_dal
    push_up()
    #push_up()
    # cislo_radku = cislo_radku + 1
    #M_pero.run_target(100, 0)
    # print("odseknuto", end = "\r")
    # jdi_na()
    paper = paper - (zmena_radek)
    M_papir.run_target(60, paper)


# paper = 0

# aby se uvolnil M_paper
for a in range(10):
    NDRadek()
# cislo_radku = 0
# start všeho
M_papir.reset_angle(0)
M_pero.run_target(200, 40)
jdi_na()

# tisk
Print_Color(robot)
push_up()


# po dokončení píp
ev3.speaker.beep(frequency=1760, duration=500)
ev3.speaker.beep(frequency=440, duration=500)
ev3.speaker.beep(frequency=1760, duration=500)
ev3.speaker.beep(frequency=440, duration=500)
ev3.speaker.beep(frequency=1760, duration=1000)
