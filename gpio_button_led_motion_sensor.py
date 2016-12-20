from gpiozero import Button, LED, MotionSensor
from time import sleep

button = Button(3)
led = LED(17)
greenLed = LED(18)
pir = MotionSensor(14)
numberOfTimes = 0
encendido = False

#button.when_pressed = led.on
#button.when_released = led.off
#pause()


while True:
    if button.is_pressed:
        numberOfTimes += 1
        sleep(0.5)

    if(numberOfTimes % 2 == 0):
        led.on()
        greenLed.off()
        encendido = False
        #print("Apagado!")
    else:
        led.off()
        encendido = True
        #print("Encendido!")

    if encendido:
        sleep(0.1)
        #print ("Entro a encendido")
        if pir.motion_detected:
            greenLed.on()
            #print("Motion detected!")
        else:
            greenLed.off()
            #print("Good Bye!!")




