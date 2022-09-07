# No "working" code here today. But here is the code you can paste on the Website. Please keep in mind that it won't
# work 100% of the time. It can get stuck in an endless loop. I may come back and debug this at another point in my
# journey! :)


def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

