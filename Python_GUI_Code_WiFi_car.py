#Python code 
#Execute this code in a python editor

"""
Project: WiFi Car Controller
Author: [Akszayan V L]
Description:
This script provides a graphical user interface (GUI) for controlling a WiFi car using Tkinter and socket communication.
The interface includes buttons for connecting to the car, controlling its movement, and stopping or closing the connection.

Dependencies:
- Tkinter for GUI
- socket for network communication

Imports:
- `tkinter` and `ttk` for creating the GUI
- `socket` for handling network communication

Functions:
- `connect_to_car()`: Establishes a socket connection to the car using the provided IP address and port.
- `stop_car()`: Sends a 'S' command to the car to stop its movement.
- `move_forward()`: Sends a 'B' command to move the car forward.
- `move_backward()`: Sends an 'F' command to move the car backward.
- `turn_left()`: Sends an 'L' command to turn the car left.
- `turn_right()`: Sends an 'R' command to turn the car right.
- `conclose()`: Sends an 'E' command to end the connection and closes the socket.

GUI Setup:
- The main window is created with a title and specified dimensions.
- Buttons are added to the window for connecting to the car, stopping, moving forward, moving backward, turning left, turning right, and closing the connection.
- Each button is linked to its corresponding function to perform the desired action.

Notes:
- Replace `'192.168.137.155'` and `8080` with the appropriate IP address and port of your car.
- Ensure that the car's server is running and listening for connections on the specified port.

For further customization or issues, please contact [krishnakanthakszayan@gmail.com].
"""



import tkinter as tk
from tkinter import ttk
import socket

def connect_to_car():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.137.155', 8080))
def stop_car():
    msg = 'S'.encode()
    s.sendall(msg)

def move_forward():
    msg = 'B'.encode()
    s.sendall(msg)

def move_backward():
    msg = 'F'.encode()
    s.sendall(msg)

def turn_left():
    msg = 'L'.encode()
    s.sendall(msg)

def turn_right():
    msg = 'R'.encode()
    s.sendall(msg)
def conclose():
    msg = 'E'.encode()
    s.sendall(msg)
    s.close()

window = tk.Tk()
window.title("RC Car Controller")
window.geometry("1000x500")  # Set the window size here

# Connect button
connect_button = ttk.Button(window, text="Connect", command=connect_to_car)
connect_button.grid(row=0, column=0, padx=10, pady=10)

# Stop button
stop_button = ttk.Button(window, text="Stop", command=stop_car)
stop_button.grid(row=1, column=0, padx=10, pady=10)

# Forward button
forward_button = ttk.Button(window, text="Forward", command=move_forward)
forward_button.grid(row=2, column=0, padx=10, pady=10)

# Backward button
backward_button = ttk.Button(window, text="Backward", command=move_backward)
backward_button.grid(row=3, column=0, padx=10, pady=10)

# Left button
left_button = ttk.Button(window, text="Left", command=turn_left)
left_button.grid(row=4, column=0, padx=10, pady=10)

# Right button
right_button = ttk.Button(window, text="Right", command=turn_right)
right_button.grid(row=5, column=0, padx=10, pady=10)

close_button = ttk.Button(window, text="close", command=conclose)
close_button.grid(row=6, column=0, padx=10, pady=10)

window.mainloop()
