from machine import Pin,PWM
import time
import utime
motor1=Pin(10,Pin.OUT)
motor2=Pin(11,Pin.OUT)
motor3=Pin(12,Pin.OUT)
motor4=Pin(13,Pin.OUT)

enable1=PWM(Pin(6))
enable2=PWM(Pin(7))
trig=Pin(3,Pin.OUT)
echo=Pin(2,Pin.IN)

servoPin=Pin(15)
servo=PWM(servoPin)
duty_cycle=0
servo.freq(50)
enable1.freq(1000)
enable2.freq(1000)
enable1.duty_u16(65025)
enable2.duty_u16(65025)
def move_forward():
    motor1.low()
    motor2.high()
    motor3.high()
    motor4.low()


def move_backward():
    motor1.high()
    motor2.low()
    motor3.low()
    motor4.high()
def move_right():
    motor1.low()
    motor2.high()
    motor3.low()
    motor4.high()

def move_right():
    motor1.low()
    motor2.high()
    motor3.low()
    motor4.high()

def move_left():
    motor1.high()
    motor2.low()
    motor3.high()
    motor4.low()

def stop():
    motor1.low()
    motor2.low()
    motor3.low()
    motor4.low()

def get_distance:
    trig.low()
    utime.sleep_us(2)
    trig.high()
    utime.sleep_us(5)
    trig.low()

    while echo.value() ==0:
        signaloff=utime.ticks_us()
    while echo.value()==1:
        signalon=utime.ticks_us()
    timepassed=signalon-signaloff
    dist=(timepassed*0..0343)/2
    return dist

def setservo(angle):
    duty_cycle=int(angle*(7803-1950)/180)+1950
    servo.duty_u16(duty_cycle)
    setservo(90)

    while True:
        distance=get_distance()
        if distance<15:
            stop()
            move_backward()
            time.sleep(1)
            stop()
            time.sleep(0.5)
            setservo(30)
            time.sleep(1)
            right_distance=get_distance()
            time.sleep(0.5)







