from machine import Pin
from machine import I2C,SoftI2C
from VL53L0X import VL53L0X  
from time import sleep
from ipstw import SSD1306
import ipstw

w = ipstw.IPSTW()
w.begin()

#i2c = I2C(1, scl = Pin(22), sda = Pin(21), freq = 400000)
I2C_bus = SoftI2C(sda=Pin(21), scl=Pin(22)) 
tof = VL53L0X(I2C_bus) 

while True: 
    tof.start()
    distance = tof.read()
    
    di = (distance/10)
    print(str(di)+" cm")
    
    w.fill(0)
    w.text(str(di)+ " cm",0,0,1)
    w.show()
    sleep(0.5)
    

    