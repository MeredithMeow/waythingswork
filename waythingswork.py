import machine
import time
import random

from machine import Pin, ADC, PWM
from time import sleep_ms

leda = machine.Pin(13, machine.Pin.OUT)
ledb = machine.Pin(12, machine.Pin.OUT)
ledc = machine.Pin(27, machine.Pin.OUT)
ledd = machine.Pin(33, machine.Pin.OUT)
lede = machine.Pin(15, machine.Pin.OUT)

button_w = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP)
button_o = machine.Pin(25, machine.Pin.IN, machine.Pin.PULL_UP)

potPin = Pin(34)

motorPin = Pin(21)
pwm = PWM(motorPin, freq=20000, duty=0)

count = 0

anim = False

pot = ADC(potPin)
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_10BIT) # 0 - 1023

while True:
    print(count)
    sensor_val = pot.read()
    if sensor_val >= 700:
        if count <= 0:
            count = 0
        if count <= 4:
            count = count - 1
        print (sensor_val)
        print ("too bright")
        print(count)
        sleep_ms(5000)
    else:
        if button_w.value()!= True:
            n = random.randint(-1,1)
            if((count>=1) and (count<=4)):
                count = count + n
            elif(count>=5):
                print("win!")
                anim = True
                count = 0
            else:
                count=1
            time.sleep_ms(200) 
        if button_o.value()!= True:
            n = random.randint(-1,1)
            if((count>=1) and (count<=4)):
                count = count + n
            elif(count>=5):
                print("win!")
                anim = True
                count = 0
            else:
                count=1
            time.sleep_ms(200)           
    if count == 0:
        leda.value(0)
        ledb.value(0)
        ledc.value(0)
        ledd.value(0)
        lede.value(0)
        pwm.duty(170)
        time.sleep_ms(200)
        pwm.duty(0)
        '''time.sleep_ms(200)'''
    if count == 1:
        leda.value(1)
        ledb.value(0)
        ledc.value(0)
        ledd.value(0)
        lede.value(0)
        pwm.duty(340)
        time.sleep_ms(200)
        pwm.duty(0)
        '''time.sleep_ms(200)'''
    if count == 2:
        leda.value(1)
        ledb.value(1)
        ledc.value(0)
        ledd.value(0)
        lede.value(0)
        pwm.duty(510)
        time.sleep_ms(200)
        pwm.duty(0)
        '''time.sleep_ms(200)'''
    if count == 3:
        leda.value(1)
        ledb.value(1)
        ledc.value(1)
        ledd.value(0)
        lede.value(0)
        pwm.duty(680)
        time.sleep_ms(200)
        pwm.duty(0)
        '''time.sleep_ms(200)'''
    if count == 4:
        leda.value(1)
        ledb.value(1)
        ledc.value(1)
        ledd.value(1)
        lede.value(0)
        pwm.duty(850)
        time.sleep_ms(200)
        pwm.duty(0)
        '''time.sleep_ms(200)'''
    if count == 5:
        leda.value(1)
        ledb.value(1)
        ledc.value(1)
        ledd.value(1)
        lede.value(1)
        pwm.duty(1020)
        time.sleep_ms(200)
        pwm.duty(0)
        '''time.sleep_ms(200)'''
    if anim == True:
        leda.value(0)
        ledb.value(0)
        ledc.value(0)
        ledd.value(0)
        lede.value(0)
        for i in range(3):
            leda.value(1)
            ledb.value(1)
            ledc.value(1)
            ledd.value(1)
            lede.value(1)
            pwm.duty(1023)
            time.sleep_ms(200) 
            leda.value(0)
            ledb.value(0)
            ledc.value(0)
            ledd.value(0)
            lede.value(0)
            pwm.duty(0)
            time.sleep_ms(200)
        for i in range(3):
            leda.value(1)
            time.sleep(0.3)
            leda.value(0)
            ledb.value(1)
            time.sleep(0.3)
            ledb.value(0)
            ledc.value(1)
            time.sleep(0.3)
            ledc.value(0)
            ledd.value(1)
            time.sleep(0.3)
            ledd.value(0)
            lede.value(1)
            time.sleep(0.3)
            lede.value(0)
        for i in range(3):
            leda.value(1)
            ledb.value(1)
            ledc.value(1)
            ledd.value(1)
            lede.value(1)
            pwm.duty(1023)
            time.sleep_ms(200) 
            leda.value(0)
            ledb.value(0)
            ledc.value(0)
            ledd.value(0)
            lede.value(0)
            pwm.duty(0)
            time.sleep_ms(200)
        anim = False
