from machine import Pin
import utime
num_of_leds = 4
leds = [Pin(i,Pin.OUT) for i in range(num_of_leds)]
t = 0.2
while True:
  for led in leds[:2]:
    led.value(1)
  utime.sleep(t)
  for led in leds[:2]:
    led.value(0)
  for led in leds[2:]:
    led.value(1)
  utime.sleep(t)
  for led in leds[2:]:
    led.value(0)

