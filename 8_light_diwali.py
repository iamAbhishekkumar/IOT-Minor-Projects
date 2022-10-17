
from machine import Pin
import utime
import random

def work(led,binary,index):
  if int(binary[index]) == 0:
    led.value(0)
  else:
    led.value(1)


num_of_leds = 8
leds = [Pin(i,Pin.OUT) for i in range(num_of_leds)]
binary_numbers = ["{:08d}".format(int(str(bin(i))[2:])) for i in range(256)]

while True:
  bn = random.choice(binary_numbers)
  for index, led in enumerate(leds):
    work(led,bn,index)
  utime.sleep(0.25)



  
