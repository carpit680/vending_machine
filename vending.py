import sys
import RPi.GPIO as gpio
import time
import serial

gpio.setwarnings(False)
product_number = int(sys.argv[1])

ser = serial.Serial(

    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

counter = 0

# primary input pins to all motors in order from 1 to 8.
gpio.setmode(gpio.BOARD)
#gpio.setup(32, gpio.OUT)
gpio.setup(32, gpio.OUT)
gpio.setup(7, gpio.OUT)
gpio.setup(12, gpio.OUT)
gpio.setup(15, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(21, gpio.OUT)
gpio.setup(23, gpio.OUT)
gpio.setup(36, gpio.OUT)

# secondary input pins to all motors in order from 1 to 8.
gpio.setup(5, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(16, gpio.OUT)
gpio.setup(19, gpio.OUT)
gpio.setup(31, gpio.OUT)
gpio.setup(38, gpio.OUT)
gpio.setup(29, gpio.OUT)


while 1:
    x=ser.readline()
    #print(x)
    if x.decode('ascii')=="5600942E37DB" or x.decode('ascii')=="5600942ED03C" or x.decode('ascii')=="560051D9558B" or x.decode('ascii')=="5600942E34D8":
       #print(x)
        counter = 1
        break
    if x.decode('ascii')=="560051D93FE1":
        counter = 2
        break
if counter == 1:
   # gpio.output(32,True)
    if product_number == 1:
        gpio.output(32,True)
        gpio.output(5,False)
        time.sleep(3)
        gpio.output(32,False)
        gpio.output(5,False)

    elif product_number == 2:
        gpio.output(7,True)
        gpio.output(11,False)
        time.sleep(3)
        gpio.output(7,False)
        gpio.output(11,False)

    elif product_number == 3:
        gpio.output(12,True)
        gpio.output(13,False)
        time.sleep(3)
        gpio.output(12,False)
        gpio.output(13,False)

    elif product_number == 4:
        gpio.output(15,True)
        gpio.output(16,False)
        time.sleep(3)
        gpio.output(15,False)
        gpio.output(16,False)

    elif product_number == 5:
        gpio.output(18,True)
        gpio.output(19,False)
        time.sleep(3)
        gpio.output(18,False)
        gpio.output(19,False)

    elif product_number == 6:
        gpio.output(31,True)
        gpio.output(21,False)
        time.sleep(3)
        gpio.output(21,False)
        gpio.output(31,False)

    elif product_number == 7:
        gpio.output(23,True)
        gpio.output(38,False)
        time.sleep(3)
        gpio.output(23,False)
        gpio.output(38,False)

    elif product_number == 8:
        gpio.output(36,True)
        gpio.output(29,False)
        time.sleep(3)
        gpio.output(36,False)
        gpio.output(29,False)
    #gpio.output(32,False)
    time.sleep(1)
    print("Thank you. Your card number: ",x)

if counter == 2:
    #gpio.output(32,True)
    if product_number == 1:
        print("1")
        gpio.output(32,False)
        gpio.output(5,True)
        time.sleep(3)
        gpio.output(32,False)
        gpio.output(5,False)

    elif product_number == 2:
        gpio.output(7,False)
        gpio.output(11,True)
        time.sleep(3)
        gpio.output(7,False)
        gpio.output(11,False)

    elif product_number == 3:
        gpio.output(12,False)
        gpio.output(13,True)
        time.sleep(3)
        gpio.output(12,False)
        gpio.output(13,False)

    elif product_number == 4:
        gpio.output(15,False)
        gpio.output(16,True)
        time.sleep(3)
        gpio.output(15,False)
        gpio.output(16,False)

    elif product_number == 5:
        gpio.output(18,False)
        gpio.output(19,True)
        time.sleep(3)
        gpio.output(18,False)
        gpio.output(19,False)

    elif product_number == 6:
        gpio.output(31,False)
        gpio.output(21,True)
        time.sleep(3)
        gpio.output(21,False)
        gpio.output(31,False)

    elif product_number == 7:
        gpio.output(23,False)
        gpio.output(38,True)
        time.sleep(3)
        gpio.output(23,False)
        gpio.output(38,False)

    elif product_number == 8:
        gpio.output(36,False)
        gpio.output(29,True)
        time.sleep(3)
        gpio.output(36,False)
        gpio.output(29,False)
    #gpio.output(32,False)
    time.sleep(1)
    print("The item has been loaded. You are using admin card.")

gpio.cleanup()
