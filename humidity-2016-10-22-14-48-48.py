# This file has been written to your home directory for convenience. It is
# saved as "/home/pi/humidity-2016-10-22-14-48-48.py"

from sense_emu import SenseHat

sense = SenseHat()

green = (0, 255, 0)
white = (255, 255, 255)
red = (255, 0, 0)

while True:
    humidity = sense.humidity
    humidity_value = 64 * humidity / 100
    pixels = [green if i < humidity_value else red for i in range(64)]
    sense.set_pixels(pixels)
    red = (255 - int(humidity), 0, 0)

