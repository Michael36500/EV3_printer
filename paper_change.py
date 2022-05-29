#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch

ev3 = EV3Brick()

M_pero = Motor(Port.C)
M_pero.run_target(200, 20)

M_papir = Motor(Port.A)
# M_pero.run_target(200, 20)
M_papir.run_until_stalled(120,duty_limit = 45)