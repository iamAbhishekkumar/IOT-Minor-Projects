from machine import Pin
from utime import sleep

led = Pin(25, Pin.OUT)
led.low()
while True:
    led.toggle()
    sleep(1)