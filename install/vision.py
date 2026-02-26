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
    Motor1.TurnStep(Dir=direction, steps=steps, stepdelay = 0.0000000)
    Motor1.Stop()


def Motor2_Turn(degrees, direction):
    steps = int(math.floor((degrees /360) * 4800)* 15)  
    Motor2.TurnStep(Dir=direction, steps=steps, stepdelay = 0.00000000)
    Motor2.Stop()
cams = pygame.camera.list_cameras()
print('Available cameras:', cams)

if cams:
    cam = pygame.camera.Camera(cams[0], (1920, 1080))  
    cam.start()
else:
    print("No camera found.")

def take_picture():
    global pic_count
    pic_count = pic_count + 1
    image = cam.get_image()
    pygame.image.save(image, "images/captured_img" + str(pic_count) + ".jpg")          
    print("Picture taken and saved at images/captured_img" + str(pic_count) + ".jpg'.")

picture_count_per_rotation = 1

wait = 0

pic_count = 0

def ring_turn(degrees, direction):
        global picture_count_per_rotation, wait
        for i in range(picture_count_per_rotation):
            Motor2_Turn(math.floor(degrees/picture_count_per_rotation), direction)
            time.sleep(wait/2)
            take_picture()
            time.sleep(wait/2)

def bevel_turn(degrees, direction):
     global picture_count_per_rotation, wait
     Motor1_Turn(degrees, direction)
     time.sleep(wait)
     Motor1.Stop()

ring_turn(100, 'forward')
ring_turn(200, 'backward')
bevel_turn(100, 'forward')
ring_turn(200, 'forward')
bevel_turn(200, 'backward')
ring_turn(100, 'backward')
bevel_turn(100, 'forward')


cam.stop()
print("Scanning complete. Total pictures taken:", pic_count)
os.system('chromium http://localhost:5000/meta/')