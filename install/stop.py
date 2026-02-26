import time, math
from DRV8825 import DRV8825
import pygame.camera
import os

pic_count = 0
pygame.camera.init()
Motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))
Motor1.SetMicroStep('softward','fullstep')
Motor2.SetMicroStep('hardward' ,'halfstep')


def Motor1_Turn(degrees, direction):
    steps = int(math.floor((degrees  / 360) * 2400)* 5)  
    Motor1.TurnStep(Dir=direction, steps=steps, stepdelay = 0.0000001)
    Motor1.Stop()


def Motor2_Turn(degrees, direction):
    steps = int(math.floor((degrees /360) * 4800)* 15)  
    Motor2.TurnStep(Dir=direction, steps=steps, stepdelay = 0.000000001)
    Motor2.Stop()

Motor1_Turn(1, 'forward')
Motor2_Turn(1, 'forward')