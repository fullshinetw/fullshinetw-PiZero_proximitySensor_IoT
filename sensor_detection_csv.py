import RPi.GPIO as GPIO
import time
import csv
from datetime import datetime
from datetime import date

input_pin = 23

def callback_function(channel):
    print("Input changed!")


def write_time_to_csv(csv_file):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    data = [timestamp, "Sensor 1", "Detected"]
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(input_pin, GPIO.IN)
    GPIO.add_event_detect(input_pin, GPIO.BOTH, callback=callback_function, bouncetime=100)
    today = date.today()
    file = '_Sensor1.csv'
    csv_file = str(today) + file

    while True:
        state = GPIO.input(input_pin)
        if state == GPIO.LOW:
            write_time_to_csv(csv_file)
        print(f"Current state: {'HIGH' if state == GPIO.HIGH else 'LOW'}")
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
