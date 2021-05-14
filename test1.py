from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep

id = 0
sda = Pin(0)
scl = Pin(1)

i2c = I2C(id=id, scl=scl, sda=sda)

oled = SSD1306_I2C(width=128, height=64, i2c=i2c)

oled.init_display()
oled.text("Test 1",1,1)
oled.show()
sleep(1)