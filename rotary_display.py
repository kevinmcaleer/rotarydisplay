# Rotary Menu
# Kevin McAleer
# May 2021

from machine import Pin, I2C
from os import listdir
from ssd1306 import SSD1306_I2C
from time import sleep

# I2C variables
id = 0
sda = Pin(0)
scl = Pin(1)
i2c = I2C(id=id, scl=scl, sda=sda)

# Screen Variables
width = 128
height = 64
line = 1 
highlight = 1
shift = 0
list_length = 0
total_lines = 6

# create the display
oled = SSD1306_I2C(width=width, height=height, i2c=i2c)
oled.init_display()

# Setup the Rotary Encoder
button_pin = Pin(16, Pin.IN, Pin.PULL_UP)
direction_pin = Pin(17, Pin.IN, Pin.PULL_UP)
step_pin  = Pin(18, Pin.IN, Pin.PULL_UP)

# for tracking the direction and button state
previous_value = True
button_down = False


def get_files():
    """ Get a list of Python files in the root folder of the Pico """
    
    files = listdir()
    menu = []
    for file in files:
        if file.endswith(".py"):
            menu.append(file)

    return(menu)


def show_menu(menu):
    """ Shows the menu on the screen"""
    
    # bring in the global variables
    global line, highlight, shift, list_length

    # menu variables
    item = 1
    line = 1
    line_height = 10

    # clear the display
    oled.fill_rect(0,0,width,height,0)

    # Shift the list of files so that it shows on the display
    list_length = len(menu)
    short_list = menu[shift:shift+total_lines]

    for item in short_list:
        if highlight == line:
            oled.fill_rect(0,(line-1)*line_height, width,line_height,1)
            oled.text(">",0, (line-1)*line_height,0)
            oled.text(item, 10, (line-1)*line_height,0)
            oled.show()
        else:
            oled.text(item, 10, (line-1)*line_height,1)
            oled.show()
        line += 1 
    oled.show()


def launch(filename):
    """ Launch the Python script <filename> """
    global file_list
    # clear the screen
    oled.fill_rect(0,0,width,height,0)
    oled.text("Launching", 1, 10)
    oled.text(filename,1, 20)
    oled.show()
    sleep(3)
    exec(open(filename).read())
    show_menu(file_list)


# Get the list of Python files and display the menu
file_list = get_files()
show_menu(file_list)

# Repeat forever
while True:
    if previous_value != step_pin.value():
        if step_pin.value() == False:

            # Turned Left 
            if direction_pin.value() == False:
                if highlight > 1:
                    highlight -= 1  
                else:
                    if shift > 0:
                        shift -= 1  

            # Turned Right
            else:
                if highlight < total_lines:
                    highlight += 1
                else: 
                    if shift+total_lines < list_length:
                        shift += 1

            show_menu(file_list)
        previous_value = step_pin.value()   
        
    # Check for button pressed
    if button_pin.value() == False and not button_down:
        button_down = True

        print("Launching", file_list[highlight-1+shift]) 

        # execute script
        launch(file_list[(highlight-1) + shift])
        
        print("Returned from launch")

    # Decbounce button
    if button_pin.value() == True and button_down:
        button_down = False