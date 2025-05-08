# ESP32 RGB LED Rainbow Effect

This MicroPython project creates a smooth rainbow effect on an RGB LED connected to an ESP32. The LED cycles through colors using PWM for vibrant transitions.

## Features
- Smooth rainbow color cycling with sine wave calculations.
- Configurable GPIO pins for RGB LED.
- Safe shutdown with `Ctrl+C` to turn off the LED.
- Adjustable transition speed.

## Hardware Requirements
- ESP32 board (e.g., ESP32 DevKitC).
- RGB LED (common cathode or anode).
- 3x resistors (220-330Ω for each LED pin).
- Breadboard and jumper wires.

## Wiring
| RGB LED Pin | ESP32 GPIO | Resistor |
|-------------|------------|----------|
| Red         | GPIO 15    | 220-330Ω |
| Green       | GPIO 2     | 220-330Ω |
| Blue        | GPIO 4     | 220-330Ω |
| Common      | GND (cathode) or 3.3V (anode) | - |

> **Note**: For common anode LEDs, modify the `set_rgb` function (see [Customization](#customization)).

## Software Requirements
- [MicroPython](https://micropython.org/) installed on the ESP32.
- Tool for uploading code:
  - [Thonny IDE](https://thonny.org/)
  - `ampy` or `esptool.py`

## Installation
1. **Flash MicroPython**:
   - Follow [MicroPython's ESP32 guide](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html).
2. **Upload Code**:
   - Save the provided code as `rainbow_led.py`.
   - Upload using Thonny or `ampy`:
     ```bash
     ampy --port /dev/ttyUSB0 put rainbow_led.py
     ```
     (Replace `/dev/ttyUSB0` with your serial port.)
3. **Run**:
   - In Thonny, run `rainbow_led.py`, or use the REPL:
     ```python
     import rainbow_led
     ```

## Code
The `rainbow_led.py` script:
- Uses PWM on GPIO 15 (Red), 2 (Green), and 4 (Blue).
- Generates rainbow colors with sine waves.
- Scales RGB values (0-255) to PWM duty cycles (0-1023).
- Stops and turns off the LED on `Ctrl+C`.

### File
- `rainbow_led.py`: Main script for the rainbow effect.

## Customization
- **GPIO Pins**:
  Update pin assignments in `rainbow_led.py`:
  ```python
  red_pin = PWM(Pin(15), freq=1000)  # Adjust GPIO
  green_pin = PWM(Pin(2), freq=1000)
  blue_pin = PWM(Pin(4), freq=1000)
