from control.control4 import *

from django import template


register = template.Library()

move = Move()

@register.filter
def control(direction):
	#move_auto(direction)
	print("je suis ici")
	listKey = ["left", "right", "down", "up", "stop"]

	if direction in listKey:
		move.move_to(direction)
	return direction