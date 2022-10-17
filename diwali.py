from machine import Pin
import utime
num_of_leds = 4
leds = [Pin(i,Pin.OUT) for i in range(num_of_leds)]
while True:
  for led in leds:
    led.value(1)
    utime.sleep(0.2)
    led.value(0)
  
