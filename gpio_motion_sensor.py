from gpiozero import MotionSensor
from time import sleep


pir = MotionSensor(18)
contadorLineas = 1

while True:
    if pir.motion_detected:
        print ("You moved!")
    else:
        print ("You not, fucking lazy OOOOOOOOOOOOOOOOOOOOOOOO!")
    sleep(0.2)
