import random
import time
import board
import pwmio 
import digitalio
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull

pwm = pwmio.PWMOut(board.GP6, duty_cycle=2 ** 15, frequency=50)
hand = servo.Servo(pwm)
items = ['rock', 'paper', 'scissors']
led = digitalio.DigitalInOut(board.GP5)
led.direction = digitalio.Direction.OUTPUT
led.value = False
#win led
winled = digitalio.DigitalInOut(board.GP22)
winled.direction = digitalio.Direction.OUTPUT
winled.value = False

rockbutton = DigitalInOut(board.GP11)
rockbutton.direction = Direction.INPUT
rockbutton.pull = Pull.UP
paperbutton = DigitalInOut(board.GP14)
paperbutton.direction = Direction.INPUT
paperbutton.pull = Pull.UP
scissorsbutton = DigitalInOut(board.GP15)
scissorsbutton.direction = Direction.INPUT
scissorsbutton.pull = Pull.UP

def blink_led(times, delay=0.5):
    for i in range(times):
        led.value = not led.value
        time.sleep(delay)
    led.value = False


while True:
    
    # Hand motion
    for i in range(3):
        for angle in range(80, 0, -5):
            hand.angle = angle
            time.sleep(0.05)
        for angle in range(10, 0, 5):
            hand.angle = angle
            time.sleep(0.05)

    
    print("rock (1), paper (2) or scissors? (3)")
    while True:
        if not rockbutton.value:
            player = '1'
            bot = random.choice(items)
            break
        if not paperbutton.value:
            player = '2'
            bot = random.choice(items)
            break
        if not scissorsbutton.value:
            player = '3'
            bot = random.choice(items)
            break 
    if bot == items[int(player) - 1]:
        print("Tie")
    elif player == '1':
        if bot == 'paper':
           # print("I chose paper!")
            print("You lose")
            blink_led(10)
        else:
           # print("I chose paper!")
            print("You win")
            winled.value = True
        break
    elif player == '2':
        if bot == 'scissors':
           # print("I chose scissors!")
            print("You lose")
            blink_led(10)
        else:
           # print("I chose scisscors!")
            print("You win")
            winled.value = True
        break
    elif player == '3':
        if bot == 'rock':
           # print("I chose rock!")
            print("You lose")
            blink_led(10)
        else:
          #  print("I chose rock!")
            print("You win")
            winled.value = True
        break
    else:
        print("Invalid input")
