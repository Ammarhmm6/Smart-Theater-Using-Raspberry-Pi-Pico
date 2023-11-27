from machine import Pin,PWM,UART, I2C
from time import sleep
import utime
from ir_rx import NEC_16
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd



buzzer = PWM(Pin(2))
buzzer.freq(500)

ppstatistic = int(0)
ppincrement = int(0)

#LCD screen.............................................................................................................................................

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20
i2c=I2C(1,sda=Pin(26),scl=Pin(27),freq=400000)

lcd=I2cLcd(i2c,I2C_ADDR,I2C_NUM_ROWS,I2C_NUM_COLS)

#Infrared receiver ........................................................................................................................................

ir_data = 0 

def ir_callback(data, addr, ctrl):
    global ir_data
    if data > 0:
        ir_data = data
        ir_addr = addr
        
ir = NEC_16(Pin(13, Pin.IN), ir_callback)
 
#ULTRsonic.......................................................................................................................................
 
trigger = Pin(21, Pin.OUT)
echo = Pin(20, Pin.IN)
trigger2 = Pin(18, Pin.OUT)
echo2 = Pin(19, Pin.IN)

def ultra ():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() ==0:
        Soff = utime.ticks_us()
    while echo.value() ==1:
        Son = utime.ticks_us()
    timepa = (Son - Soff)
    distance = (timepa * 0.0343) / 2
    return distance

def ultra2 ():
    trigger2.low()
    utime.sleep_us(2)
    trigger2.high()
    utime.sleep_us(5)
    trigger2.low()
    while echo2.value() ==0:
        Soff = utime.ticks_us()
    while echo2.value() ==1:
        Son = utime.ticks_us()
    timepa = (Son - Soff)
    distance = (timepa * 0.0343) / 2
    return distance

#SERVO.....................................................................................................................................................

MID =1500000
MIN =1000000   
MAX = 1800000

def opeen():
    F=MAX
    L=MIN
    while F>MIN:
        Servo.duty_ns (F)
        Servo2.duty_ns (L)
        F=F-5000
        L=L+5000
        sleep(0.0045)
    sleep(2.5)
    while F<MAX:
        Servo.duty_ns (F)
        Servo2.duty_ns (L)
        F=F+5000
        L=L-5000
        sleep(0.0045)
Servo=PWM(Pin(6))
Servo.freq(50)
Servo2=PWM(Pin(7))
Servo2.freq(50)

#LED..........................................................................................................................................................

led1 =Pin(14, Pin.OUT)
led2 = Pin(15, Pin.OUT)
def led():
    global ppincrement
    if (ppincrement==0):
        led1.low()
        led2.low()

    elif ppincrement > 0:
        led1.high()
        led2.high()

    
    elif ppincrement < 0:
        ppincrement = 0

#from here the code starts ......................................................................................................................................
while True:
    ir_data = 0 
    led()
    Dist1=ultra()
    Dist2=ultra2()

    lcd.clear()
    lcd.move_to(3,0)
    lcd.putstr("Welcome to")
    lcd.move_to(2,1)
    lcd.putstr("BASA Theater")
    
    Servo.duty_ns (MAX)
    Servo2.duty_ns (MIN)
    
    if (Dist1 <= 10):
        if(ppincrement < 5):
            opeen()
            ppincrement = ppincrement+1
            ppstatistic = ppstatistic+1
            print("\n\nNumber of people inside the room:\t",ppincrement)
            print("\nThe of people who have entered the room:\t",ppstatistic)
        elif(ppincrement>=5):
            print("\n\nThe number of people in the room has reached the limit, ")
            print("therefore, you are not allowed in")
            lcd.clear()
            lcd.move_to(3,0)
            lcd.putstr("The room is full")
            lcd.move_to(2,1)
            lcd.putstr("for your health please wait")
            buzzer.duty_u16(1000)
            sleep(1)
            buzzer.duty_u16(0)
            sleep(1)
        else:
            pass

# this is independent if (distance 2) 
    if(Dist2 <= 10):
        opeen()
        ppincrement = ppincrement-1
        if (ppincrement < 0):
            ppincrement=0
        print("\n\nNumber of people inside the room:\t",ppincrement)
        print("\nThe of people who have entered the room:\t",ppstatistic)
        lcd.clear()
        lcd.move_to(3,0)
        lcd.putstr("Come Again")
        lcd.move_to(0,1)
        lcd.putstr("Have a nice day!")
        lcd.clear()
        lcd.move_to(3,0)
        lcd.putstr("Welcome")
        lcd.move_to(2,1)
        lcd.putstr("to BASA theater")
    sleep(0.1)

    if ir_data != 0 :
        print("This is emergency mode press button number 9 to back to normal mode")
        if ir_data == 0x0c:
            while True:
                if ir_data == 0x4a:
                    ir_data = 0 
                    break
                
                if ir_data == 0x18:
                    led1.high()
                    led2.high()
                
                if ir_data == 0x5e:
                    led1.low()
                    led2.low()
                    
                if ir_data == 0x08:
                    F=MAX
                    L=MIN
                    while F>MIN:
                        Servo.duty_ns (F)
                        Servo2.duty_ns (L)
                        F=F-5000
                        L=L+5000
                        sleep(0.0045)
                        ir_data = 0 
                if ir_data == 0x1c:
                    while F<MAX:
                        Servo.duty_ns (F)
                        Servo2.duty_ns (L)
                        F=F+5000
                        L=L-5000
                        sleep(0.0045)
                        ir_data = 0
            