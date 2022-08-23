import rotatescreen     #if we give the python's file as module name, it may show attribute error.
import time


screen = rotatescreen.get_primary_display()
#screen.rotate_to(0)
for i in range(10):
    time.sleep(1)
    screen.rotate_to(i*90 % 360)