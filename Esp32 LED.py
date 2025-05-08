from machine import Pin, PWM
from time import sleep
import math

# Define RGB LED pins (adjust these based on your ESP32 wiring)
red_pin = PWM(Pin(15), freq=1000)   # GPIO 15 for Red
green_pin = PWM(Pin(2), freq=1000)  # GPIO 2 for Green
blue_pin = PWM(Pin(4), freq=1000)   # GPIO 4 for Blue

def rainbow_cycle(step):
    # Calculate RGB values for a smooth rainbow transition
    r = int(255 * abs(math.sin(step * 0.01)))
    g = int(255 * abs(math.sin((step * 0.01) + 2)))
    b = int(255 * abs(math.sin((step * 0.01) + 4)))
    return r, g, b

def set_rgb(r, g, b):
    # Set PWM duty cycle (0-1023 for ESP32)
    # Adjust for common anode or cathode LED
    red_pin.duty(r * 4)    # Multiply by 4 to scale 0-255 to 0-1023
    green_pin.duty(g * 4)
    blue_pin.duty(b * 4)

try:
    step = 0
    while True:
        # Get rainbow colors
        r, g, b = rainbow_cycle(step)
        # Apply colors to LED
        set_rgb(r, g, b)
        # Increment step for color transition
        step = (step + 1) % 628  # Cycle through 2π (approx 628 steps)
        sleep(0.02)  # Adjust speed of color change (20ms delay)

except KeyboardInterrupt:
    # Turn off LED on interrupt
    set_rgb(0, 0, 0)
    print("Rainbow stopped")