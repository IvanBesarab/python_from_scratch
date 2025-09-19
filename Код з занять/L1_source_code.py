# write any code you want
from karel.stanfordkarel import *

def main():
   # your code here...
   move()
   move()
   put_beeper()
   turn_left()
   turn_left()
   move()
   move()
   turn_left()
   turn_left()
  

# write any code you want
from karel.stanfordkarel import *

def main():
   # your code here...
   hid_po_diagonali()
   hid_po_diagonali()
   
def hid_po_diagonali():
   move()
   turn_left()
   move()
   turn_right()
  
def turn_right():
   turn_left()
   turn_left()
   turn_left()


# write any code you want
from karel.stanfordkarel import *

def main():
   # your code here...
   move()
   move()
   move()
   if front_is_clear():
      move()
   else:
      put_beeper()

# write any code you want
from karel.stanfordkarel import *

def main():
   # your code here...
   setup_world()
   
   move()
   
   if beepers_present():
      pick_beeper()
      turn_left()   
      move()
      put_beeper()
   else:
      move()
   
   turn_left()   
   turn_left()   
   
   
def setup_world():
   move()
   put_beeper()
   
   turn_left()
   turn_left()
   move()
   turn_left()
   turn_left()
   
# write any code you want
from karel.stanfordkarel import *

def main():
   # your code here...
   for i in range(7):
      hid_po_diagonali()
   
   
def hid_po_diagonali():
   move()
   turn_left()
   move()
   turn_right()
  
def turn_right():
   turn_left()
   turn_left()
   turn_left()
   
   
# write any code you want
from karel.stanfordkarel import *

def main():
   
   put_beeper()
   
   while front_is_clear():
      move()
      put_beeper()
   
   
def hid_po_diagonali():
   move()
   turn_left()
   move()
   turn_right()
  
def turn_right():
   turn_left()
   turn_left()
   turn_left()
