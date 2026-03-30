import time, math
from gpiolibrary import *
import pygame.camera
import os
from powermonitor import *
import threading

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
    cam = pygame.camera.Camera(cams[0], (4000, 3000))  
    cam.start()
else:
    print("No camera found.")

def take_picture():
    global pic_count
    pic_count = pic_count + 1
    image = cam.get_image()
    pygame.image.save(image, "images/captured_img" + str(pic_count) + ".jpg")          
    #print("Picture taken and saved at images/captured_img" + str(pic_count) + ".jpg'.")

picture_count_per_rotation = 30

wait = 1

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

def power_monitor():
    ina219 = INA219(addr=0x40)
    while True:
        bus_voltage = ina219.getBusVoltage_V()             # voltage on V- (load side)
        shunt_voltage = ina219.getShuntVoltage_mV() / 1000 # voltage between V+ and V- ac>
        current = ina219.getCurrent_mA()                   # current in mA
        power = ina219.getPower_W()                        # power in W


        # INA219 measure bus voltage on the load side. So PSU voltage = bus_voltage + shu>
        #print("PSU Voltage:   {:6.3f} V".format(bus_voltage + shunt_voltage))
        #print("Shunt Voltage: {:9.6f} V".format(shunt_voltage))
        print("Load Voltage:  {:6.3f} V     ".format(bus_voltage))
        print("Current:       {:6.3f} A     ".format(current/1000))
        print("Power:         {:6.3f} W     ".format(power))
        print("\33[4A")

        time.sleep(0.1)



os.system(r"figlet 'Ancient Vision'")

print('The future of archeological databases and scanning software')

print(
f'''
Scanner Settings:
Pictures per rotation: {picture_count_per_rotation}
Wait time between pictures: {wait} seconds
Total pictures to take: {picture_count_per_rotation * 4}
'''
)

thread = threading.Thread(target=power_monitor)
thread.start()
print(f'Power monitor thread started: {thread.name}')

ring_turn(100, 'forward')
ring_turn(200, 'backward')
bevel_turn(100, 'forward')
ring_turn(200, 'forward')
bevel_turn(200, 'backward')
ring_turn(100, 'backward')
bevel_turn(100, 'forward')


cam.stop()
print("Scanning complete. Total pictures taken:", pic_count)
os.system('chromium http://localhost:1234/')