#Program to blink all LED's


import RPi.GPIO as GPIO
import time
in1 = 14
in2 = 15
en = 18
in3 = 24
in4 = 23

def init():
    GPIO.setmode(GPIO.BCM)          #To use GPIO numbering system
    GPIO.setup(in1,GPIO.OUT)         #Set pin no 24 as an output pin
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(en,GPIO.OUT)
    GPIO.output(en,True)
def fwd():
    GPIO.output(in1,GPIO.HIGH)   #Set pin no 24 to HIGH 
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def rev():
    GPIO.output(in1,GPIO.LOW)   #Set pin no 24 to HIGH 
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def right():
    GPIO.output(in1,GPIO.HIGH)   #Set pin no 24 to HIGH 
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def left():
    GPIO.output(in1,GPIO.LOW)   #Set pin no 24 to HIGH 
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def stp():
    GPIO.output(in1,GPIO.LOW)   #Set pin no 24 to HIGH 
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

    
