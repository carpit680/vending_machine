import RPi.gpio as gpio 
import time

gpio.setwarnings(False) 
gpio.setmode(gpio.BOARD) 

# primary input pins to all motors in order from 1 to 8.
gpio.setmode(gpio.BOARD)
gpio.setup(3, gpio.OUT)
gpio.setup(7, gpio.OUT)
gpio.setup(12, gpio.OUT)
gpio.setup(15, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(21, gpio.OUT)
gpio.setup(23, gpio.OUT)
gpio.setup(26, gpio.OUT)

# secondary input pins to all motors in order from 1 to 8.
gpio.setup(5, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(16, gpio.OUT)
gpio.setup(19, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(24, gpio.OUT)
gpio.setup(29, gpio.OUT)

gpio.output(3,False)
gpio.output(5,False)
gpio.output(7,False)
gpio.output(11,False)
gpio.output(12,False)
gpio.output(13,False)
gpio.output(15,False)
gpio.output(16,False)
gpio.output(18,False)
gpio.output(19,False)
gpio.output(21,False)
gpio.output(22,False)
gpio.output(23,False)
gpio.output(24,False)
gpio.output(26,False)
gpio.output(29,False)

gpio.cleanup()