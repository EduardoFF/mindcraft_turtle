from mc import *
from time import sleep
sleep(0.5)


place_square(100,500, "red",label="2")
place_square(100,300, "red", label="1")
place_square(400,500, "red", label="4")
place_square(400,300, "red", label="3")

id = scan_for_squares(180)
if id == False:
	# cant find
	say("Error, can't find any square")
else:
	go_to_square_by_id(id)
	align_with_left_post()
	angle=acos(300/360.55)
	rotate(angle/2)
	move_forward(316)





























sleep(5)
