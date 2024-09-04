import bme280
import smbus2
from time import sleep
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)


print("1- Tomate")
print("2- Carotte")
print("3- Concombre")
saisi = int(input("Quel plentation choisiser vous? "))

def verification(minTem, maxTem, minHum, maxHum):
    while True:
        bme280_data = bme280.sample(bus,address)
        humidity  = bme280_data.humidity
        ambient_temperature = bme280_data.temperature 
        print(humidity, ambient_temperature)

        if ambient_temperature < minTem and ambient_temperature > maxTem :
            GPIO.output(24, GPIO.LOW)
        else:
            GPIO.output(24, GPIO.HIGH)
        
        if humidity < minHum and humidity > maxHum :
            GPIO.output(23, GPIO.LOW)
        else:
            GPIO.output(23, GPIO.HIGH)
        time.sleep(1)
    
    

if saisi == 1:
    verification(20,25,50,70)
elif saisi == 2:
    verification(16,23,45,65)
elif saisi == 3:
    verification(18,26,60,70)
else :
    print("Choix invalide")







