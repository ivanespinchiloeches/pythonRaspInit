from gpiozero import Button
from time import sleep

button = Button(3)
numberOfTimes = 1

while True:
    button.wait_for_press()
    print ("You pushed me ", numberOfTimes, " times ")
    numberOfTimes = numberOfTimes + 1
    sleep(0.2)
