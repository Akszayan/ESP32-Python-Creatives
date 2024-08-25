"""
Project: ESP32 WiFi-Controlled Car
Author: [Akszayan V L]
Description:
This MicroPython script allows remote control of a car using the ESP32 microcontroller and WiFi.
The car is controlled through a Python-based socket connection, enabling commands to move 
the car forward, backward, left or right and stop. The script uses the `usocket` module for handling socket communication.

Features:
- WiFi connectivity for remote control
- Socket-based communication using Python's `usocket` module
- Control commands: 'F' for forward, 'B' for backward, 'L' for left, 'R' for right and S for stop

Components:
- ESP32 microcontroller
- Motor driver module for car control
- WiFi network for communication
- Python socket client for sending commands

Setup and Usage:
1. Connect the ESP32 to your car’s motor driver module according to the wiring diagram.
2. Flash MicroPython onto the ESP32 and upload this script using an IDE like Thonny or uPyCraft.
3. Configure the ESP32 to connect to your WiFi network by updating the script with your network credentials.
4. Use a Python socket client to connect to the ESP32’s IP address and send control commands.
5. Commands include: 'F' (forward), 'B' (backward), 'L' (left), 'R' (right).

Dependencies:
- MicroPython
- `usocket` module for socket communication

Credits:
- Developed by [Your Name]
- Utilizes MicroPython and ESP32 technologies


For further information, modifications, or contributions, please contact [Krishnakanthakszayan@gmail.com].
"""



# Micropython code 
# Excecute this code in Micropython Editor


from machine import Pin,PWM
import time as t
import network
import usocket

ssid = 'Your_SSID'
pwd = 'Your_Password'
ip_address = '192.168.137.155'

def wificonnect(ssid,pwd):
    ip_address = '192.168.137.155'
    subnet_mask = '255.255.255.0'
    gateway = '192.168.43.12'
    dns = '8.8.8.8'
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid,pwd)
    wlan.ifconfig((ip_address,subnet_mask,gateway,dns))
    print(wlan.ifconfig())
    while not wlan.isconnected():
        t.sleep(1)
    print('connected to %s'%ssid)
    print('IP address:', wlan.ifconfig()[0])
wificonnect(ssid,pwd)

s = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
s.bind((ip_address, 8080))
s.listen(1)
conn, addr = s.accept()
print('Client connected from', addr)

IN1 = Pin(13,Pin.OUT)#in1 & in4 front 
IN2 = Pin(12,Pin.OUT)
IN3 = Pin(14,Pin.OUT)
IN4 = Pin(27,Pin.OUT)
pwmA1 = PWM(IN1,freq=1000)#LEFT
pwmB2 = PWM(IN2,freq=1000)
pwmB1 = PWM(IN3,freq=1000)
pwmA2 = PWM(IN4,freq=1000)#RIGHT
pwmA1.duty(0)
pwmA2.duty(0)
pwmB2.duty(0)
pwmB1.duty(0)
    
try :
    while True :
        i = conn.recv(1024).decode()
        if i == 'F' :
            print('moving front')
            pwmA1.duty(500)
            pwmA2.duty(500)
            pwmB2.duty(0)
            pwmB1.duty(0)
            t.sleep(0.5)
            pwmA1.duty(0)
            pwmA2.duty(0)
            pwmB2.duty(0)
            pwmB1.duty(0)
        if i == 'B' :
            print('moving backward')
            pwmA1.duty(0)
            pwmA2.duty(0)
            pwmB2.duty(500)
            pwmB1.duty(500)
            t.sleep(0.5)
            pwmA1.duty(0)
            pwmA2.duty(0)
            pwmB2.duty(0)
            pwmB1.duty(0)
        if i == 'R' :
            print('moving towards right')
            pwmA1.duty(700)
            pwmA2.duty(0)
            pwmB2.duty(0)
            pwmB1.duty(0)
            t.sleep(0.5)
            pwmA1.duty(0)
            pwmA2.duty(0)
            pwmB2.duty(0)
            pwmB1.duty(0)
        if i == 'L' :
            print('moving towards left')
            pwmA1.duty(0)
            pwmA2.duty(700)
            pwmB2.duty(0)
            pwmB1.duty(0)
            t.sleep(0.5)
            pwmA1.duty(0)
            pwmA2.duty(0)
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
            t.sleep(0.5)
            pwmA1.duty(0)
            pwmA2.duty(0)
            pwmB2.duty(0)
            pwmB1.duty(0)
            print('BACKRIGHT')
        if i == 'M' :
            pwmA1.duty(0)
            pwmA2.duty(0)
            pwmB2.duty(0)
            pwmB1.duty(700)
            t.sleep(0.5)
            pwmA1.duty(0)
            pwmA2.duty(0)
            pwmB2.duty(0)
            pwmB1.duty(0)
            print('BACKLEFT')
        if i == 'E' :
            pwmA1.duty(0)
            pwmA2.duty(0)
            pwmB2.duty(0)
            pwmB1.duty(0)
            print('bye')
            break
except:
    print('error')
    pwmA1.duty(0)
    pwmA2.duty(0)
    pwmB2.duty(0)
    pwmB1.duty(0)
