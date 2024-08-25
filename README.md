# Rotary Display Menu

This is a simple menu program for use with small OLED displays such as the SSD1306. It is designed to be used with a rotary encoder and a push button.

The menu is displayed on the OLED and the user can navigate through the menu using the rotary encoder. The push button is used to select an item in the menu.

The app will show all the micropython files on the device and allow the user to select one to run.

---

## Installation

To install the program, copy the following files to the MicroPython device:

- `rotary_display.py` - The main program file
- `ssd1306.py` - The OLED display driver
- `test1.py` - A test file to run
- `test2.py` - A test file to run
- `test3.py` - A test file to run

---

## Usage

To use the program, connect the OLED display and rotary encoder to the MicroPython device. Then run the `rotary_display.py` program.

---

## Wiring

The wiring for the OLED display and rotary encoder is as follows:

- OLED Display:
  - VCC -> 3.3V
  - GND -> GND
  - SDA -> Pin 0
  - SCL -> Pin 1

- Rotary Encoder:
  - button -> Pin 16
  - direction -> Pin 17
  - step -> Pin 18

---
