# посилання на сайт з Karel - https://compedu.stanford.edu/karel-reader/docs/python/en/ide.html
from karel.stanfordkarel import *

# 🟢 Початковий рівень (основи руху та команд)
# 1. Рух до стіни – рухайся вперед, поки не впрешся у стіну.
# 2. Перенести цукерку по діагоналі  #setup_world1()
# 3. Покласти один цукерок – поставити цукерку (beeper) у поточному місці.
# 4. Підняти один цукерок – забрати цукерку з поточного місця. #setup_world1()
# 5. Рух поки не знайдеш цукерку – рухайся вперед, доки не знайдеш цукерку #setup_world2()
# 6. Зібрати всі цукерки в одному ряді – пройти ряд і підняти всі цукерки. #setup_world2()
# 7. Поставити лінію з цукерок – пройти ряд і поставити цукерки на кожній пустій клітинці. #setup_world2()
# 8. Побудувати прямокутну рамку з цукерок – викласти цукерки по периметру прямокутника.
# 9. Патрулювання коридору – пройти вперед-назад між двома стінами.

# 🟡 Середній рівень (цикли та умови)
# 1. Заповнити ряд цукерками (горизонтально) – на кожній клітинці ряду поставити по цукерці.
# 2. Заповнити колонку цукерками (вертикально) – поставити цукерки у вертикальному стовпчику.
# 3. Заповнити всю сітку цукерками – поставити цукерки у кожній клітинці світу.
# 4. Розкласти цукерки через одну клітинку (шахівниця) – поставити цукерки в клітинках через одну.
# 5. Розкласти цукерки по діагоналі – поставити цукерки на головній діагоналі світу.
# 6. Побудувати сходи з цукерок – викласти цукерки сходинками вгору.
# 7. Піднятися та спуститися сходами – пройти вгору сходами і повернутися вниз.
# 8. Будувати колони через одну вулицю – викладати вертикальні ряди цукерок лише на парних/непарних вулицях.
# 9. Йти по доріжці з цукерок – рухатися по шляху, позначеному цукерками #setup_world4()
# 10. Повернутися на старт після руху – дійти до певного місця і повернутися на початок #setup_world5()/#setup_world6()
# 11. Прибрати всі цукерки зі світу – пройти всі клітинки й зібрати кожну цукерку #setup_world4()

def main():
    setup_world1()

def setup_world1():
    move()
    put_beeper()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()

def setup_world2():
    move()
    put_beeper()
    move()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    move()
    move()
    put_beeper()
    turn_left()
    turn_left()
    for i in range(7):
        move()
    turn_left()
    turn_left()

def setup_world4():
    move()
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_left()
    turn_left()
    turn_left()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    turn_left()
    move()
    move()
    move()
    move()
    turn_left()
    move()
    move()
    move()
    move()
    turn_left()
 
def setup_world5():
    move()
    move()
    turn_left()
    move()
    move()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    move()
    turn_left()
   
def setup_world6():
    move()
    move()
    turn_left()
    move()
    move()
    move()
    move()
    turn_left()
    turn_left()
    move()
    turn_left()
    move()
    turn_left()
    move()
    move()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
   
