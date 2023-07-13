import BlynkLib
import RPi.GPIO as GPIO
from BlynkTimer import BlynkTimer


device = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(device, GPIO.OUT)
GPIO.output(device, GPIO.LOW)

blynk = BlynkLib.Blynk("api key")

@blynk.on("V0")
def v0_write_handler(value):

    if int(value[0]) is not 0:
        GPIO.output(device, GPIO.HIGH)
    
    else:
        GPIO.output(device, GPIO.LOW)


@blynk.on("connected")
def blynk_connected():
    print("Conn")

while 1:
    blynk.run()