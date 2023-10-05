from machine import Pin
from time import sleep_ms

# Check the LED pin on your board, usually it is GPIO2
print("Configure output pin #2... ", end="")
led = Pin(2, Pin.OUT)
print("Done")
print("Start blinking...")

# Forever loop
while True:
    led.on()
    sleep_ms(125)
    led.off()
    sleep_ms(125)