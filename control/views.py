from django.shortcuts import render
from django.http import HttpResponse
from control.control4 import *
# Create your views here.

# def index(request):
# 	#move_auto('w')
# 	if request.method == 'POST':
# 	    if 'pieFact' in request.POST:
# 	        pieFact = request.POST['pieFact']
# 	        print(pieFact)
# 	a = "test"
# 	# if request.method == 'POST':
# 	# 	key = 'esdras'
# 	# 	if key in request.POST:
# 	# 		print(key)

# 	# 	print(POST['name'])
# 	# 	a = "Esdrassssssssssssssssssss"
# 	# 	print("test")
# 		#return render(request, "control/index.html", {'text': a})

# 	return render(request, "control/index.html", {'text': a})
# d = ""
move = Move()
def index(request):
	a = "text"
	d = 0
	if request.method == 'POST':
		# print(request.POST['name'])
		if "left" in request.POST:
			# if not move.isRunning('left'):
			move.move_to('left')
			# print(request.POST)
		if "right" in request.POST:
			# if not move.isRunning('right'):
			move.move_to('right')
			# print(request.POST)

		if "up" in request.POST:
			# if not move.isRunning('up'):
			move.move_to('up')
			# print(request.POST)

		if "down" in request.POST:
			# if not move.isRunning('left'):
			move.move_to('down')
			# print(request.POST)

		if "stop" in request.POST:
			# if not move.isRunning('left'):
			move.move_to('stop')
			# print(request.POST)

	# 	if "right" in request.POST:
	# 		print("je suis dans right")
	# 		# move.right()

	# 	if "up" in request.POST:
	# 		print(request.POST)
	# 		print("je suis dans foward")
	# 		# move.foward()

	# 	if "down" in request.POST:
	# 		print("je suis dans backward")
	# 		# move.backward()

	# 	if "stop" in request.POST:
	# 		print("je suis dans stop")
	# 		# move.stop_move()
	return render(request, "control/index.html", {'text': a})