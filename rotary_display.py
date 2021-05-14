# Rotary Menu
from machine import Pin, I2C
from os import listdir
from ssd1306 import SSD1306_I2C

id = 0
sda = Pin(0)
scl = Pin(1)
width = 128
height = 64


i2c = I2C(id=id, scl=scl, sda=sda)

print("i2c scan - ", i2c.scan())

oled = SSD1306_I2C(width=width, height=height, i2c=i2c)
oled.init_display()
# oled.text("test",1,1)
# oled.show()

menu = []

files = listdir()
line = 1 
item = 1
highlight = 1
line_height = 10

for file in files:
    if file.endswith(".py"):
        menu.append(file)
print(menu)

def show_menu():
    """ Shows the menu on the screen"""
    
    # bring in the global variables
    global menu, line, line_height, width, height

    # oled.fill_rect(1,(line-1)*line_height, width,line_height,1)
    for item in menu:
        if highlight == line:
            oled.fill_rect(1,(line-1)*line_height, width,line_height,1)
            oled.text(">",1, (line-1)*line_height,0)
            oled.text(item, 10, (line-1)*line_height,0)
            print(line, "true")
            oled.show()
        else:
            oled.text(item, 10, (line-1)*line_height,1)
            print(line, "false")
            oled.show()
        line += 1 
    oled.show()

show_menu()
