import threading
import time
import sys
import termios
import contextlib

import RPi.GPIO as GPIO
from time import sleep
import sys

 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 16
Motor1B = 18
Motor1E = 22
 
Motor2A = 23
Motor2B = 21
Motor2E = 19


GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)
 
def foward(tf):
	print ("FOWARD")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)
		 
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)
 
	sleep(tf)

def backward(tf):
	print ("BACKWARD")
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
	 
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)
	 
	sleep(tf)

def uTurnRight(tf):
	print ("U-TURN LEFT")
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
		 
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)
 
	sleep(tf)

def uTurnLeft(tf):
	print ("U-TURN RIGHT")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)
	 
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)
	 
	sleep(tf)

def left(tf):
	print ("RIGHT")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)
	 
	sleep(tf)

def right(tf):
	print ("LEFT")
	 
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)
	 
	sleep(tf)
 
def stop():
	print ("Now stop")
	GPIO.output(Motor1E,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.LOW)

@contextlib.contextmanager
def raw_mode(file):
    old_attrs = termios.tcgetattr(file.fileno())
    new_attrs = old_attrs[:]
    new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
    try:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
        yield
    finally:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)


def move_auto(val):
	sleep_time=3
	if val == 'w':
		print('Dans essaie')
		foward(sleep_time)
		stop()
	elif val == 's':
		backward(sleep_time)
		stop()
	elif val == 'a':
		left(sleep_time)
		stop()
	elif val == 'd':
		right(sleep_time)
		stop()
	elif val == 'q':
		uTurnLeft(sleep_time)
		stop()
	elif val == 'e':
		uTurnRight(sleep_time)
		stop()
  
class Loop(threading.Thread): 
    def __init__(self, nom = ''): 
        threading.Thread.__init__(self) 
        self.nom = nom 
        self.Terminated = False 
    def run(self): 
        i = 0 
        while not self.Terminated: 
            print (self.nom, i) 
            i += 1 
            time.sleep(0.03) 
        print ("le thread "+self.nom +" s'est termine proprement") 
    def stop(self): 
        self.Terminated = True


# class Affiche2(threading.Thread): 
#     def __init__(self, nom = ''): 
#         threading.Thread.__init__(self) 
#         self.nom = nom 
#         self._stopevent = threading.Event( ) 
#     def run(self): 
#         i = 0 
#         while not self._stopevent.isSet(): 
#             print (self.nom, i) 
#             i += 1 
#             self._stopevent.wait(2.0) 
#         print ("le thread "+self.nom +" s'est termine proprement") 
#     def stop(self): 
#         self._stopevent.set( ) 


class Move:
	"""docstring for Move"""
	def __init__(self):
		# super Move, self).__init__()
		self.move = ''
		
	def move_to(self, direction):
		if direction and direction != "stop":
			self.stop_move()
			self.move = Loop(direction)
			self.move.start()

		elif direction == "stop":
			self.stop_move()
			# self.direc = ''

	# def left(self):
	# 	self.stop_move()
	# 	self.move = Affiche("left")
	# 	self.move.start()

	# def right(self):
	# 	self.stop_move()
	# 	self.move = Affiche("right")
	# 	self.move.start()

	
	def stop_move(self):
		if self.move:
			self.move.stop()

	# def foward(self):
	# 	self.stop_move()
	# 	self.move = Affiche("forward")
	# 	self.move.start()

	# def backward(self):
	# 	self.stop_move()
	# 	self.move = Affiche("backward")
	# 	self.move.start()

		
# b = Affiche('Thread B')

# def left():
# 	b = Affiche('Thread B')
# 	b.start()

# def leftStop():

# def test(val):  
# 	# a = Affiche('Thread A')  
# 	# c = Affiche2('Thread C') 

# 	# a.start()
# 	if val == 1: 
# 		b.start()
# 	else:
# 		b.stop() 
	# c.start() 
	# # time.sleep(6.5) 
	# # a._Thread__stop() 
	# b.stop() 
	# c.stop()