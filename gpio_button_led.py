from gpiozero import Button
from gpiozero import LED
from time import sleep

button = Button(3)
led = LED(17)
blueLed = LED(18)
numberOfTimes = 0
#button.when_pressed = led.on
#button.when_released = led.off
#pause()


while True:
    button.wait_for_press()
    if(numberOfTimes % 2 == 0):
        led.on()
        blueLed.off()
    else:
        led.off()
        blueLed.on()
    sleep(0.2)
    numberOfTimes += 1


