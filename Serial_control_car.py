"""
Project: [Esp32 - serial_control_car]
Author: [Akszayan V L]
Description: [This MicroPython script enables control of a car using serial communication with an ESP32 microcontroller. 
              The code handles commands sent via a serial connection to control the car's movements,
              such as forward, backward, left,right and stop.]
Version: [Version 1.0]

Credits:
- Developed using MicroPython on ESP32
- Code written by [Akszayan V L]

Feel free to use, modify, or distribute this code as needed. For any inquiries or contributions, please contact [krishnakanthakszayan@gmail.com].
"""

# Micropython code
# Execute this code in micropython code editor 



from machine import Pin,PWM 
import time as t

IN1 = Pin(13,Pin.OUT)   #IN1 & IN4 FORWARD MOVE
IN2 = Pin(12,Pin.OUT)   #IN2 & IN3 BACKWARD MOVE
IN3 = Pin(14,Pin.OUT)
IN4 = Pin(27,Pin.OUT)

'''
IN1.value(1)#front
IN4.value(1)
t.sleep(5)
IN1.value(0)
IN4.value(0)
t.sleep(5)
'''
'''
IN2.value(1)#back
IN3.value(1)
t.sleep(5)
IN2.value(0)
IN3.value(0)
'''
# You can increase or decrease the speed of each motors using PWM duty function.
pwmA1 = PWM(IN1,freq=1000)#LEFT
pwmB2 = PWM(IN2,freq=1000)
pwmB1 = PWM(IN3,freq=1000)
pwmA2 = PWM(IN4,freq=1000)#RIGHT
pwmA1.duty(0)                         
pwmA2.duty(0)
pwmB2.duty(0)
pwmB1.duty(0)

'''pwmA1.duty(700)
pwmA2.duty(700)
pwmB2.duty(0)
pwmB1.duty(0)
t.sleep(5)
print('off')
pwmA1.duty(0)
pwmA2.duty(0)
pwmB1.duty(0)
pwmB2.duty(0)
t.sleep(1)'''

while True :
    i = input('enter the direction FBRL: ')
    if i == 'F' :
        print('moving front')
        pwmA1.duty(0)
        pwmA2.duty(0)
        pwmB2.duty(500)
        pwmB1.duty(500)
    if i == 'B' :
        print('moving backward')
        pwmA1.duty(500)
        pwmA2.duty(500)
        pwmB2.duty(0)
        pwmB1.duty(0)
    if i == 'L' :
        print('moving towards right')
        pwmA1.duty(700)
        pwmA2.duty(0)
        pwmB2.duty(0)
        pwmB1.duty(0)
    if i == 'R' :
        print('moving towards left')
        pwmA1.duty(0)
        pwmA2.duty(700)
        pwmB2.duty(0)
        pwmB1.duty(0)
    if i == 'S' :
        pwmA1.duty(0)
        pwmA2.duty(0)
        pwmB2.duty(0)
        pwmB1.duty(0)
        print('vehicle stopped')
    if i == 'K' :
        pwmA1.duty(0)
        pwmA2.duty(0)
        pwmB2.duty(700)
        pwmB1.duty(0)
        print('BACKRIGHT')
    if i == 'M' :
        pwmA1.duty(0)
        pwmA2.duty(0)
        pwmB2.duty(0)
        pwmB1.duty(700)
        print('BACKLEFT')
    if i == 'E' :
        break
        print('bye')
# Thank you
        



