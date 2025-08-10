import RPi.GPIO as GPIO
import time
import csv
import threading
from datetime import datetime
from datetime import date

s1_input_pin = 23
s2_input_pin = 24
s3_input_pin = 25
s4_input_pin = 17
s5_input_pin = 27
s6_input_pin = 22
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def callback_function(channel):
    print("Input changed!")


def write_time_to_csv(csv_file,s):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    data = [timestamp, s, "Detected"]
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def led_flash():
    led_pin = 21
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(21,True)
    time.sleep(0.5)
    GPIO.output(21,False)
    print("LED light")

class Inductive(threading.Thread):
    """A Thread that monitors a GPIO Port"""
    def __init__(self, channel):
        threading.Thread.__init__(self)
        self._pressed = False
        self.channel = channel
        # set up pin as input
        GPIO.setup(self.channel, GPIO.IN)
        # terminate this thread when main program finishes
        self.daemon = True
         # start thread running
        self.start()
    def pressed(self):
        if self._pressed:
        # clear the pressed flag now we have detected it
            self._pressed = False
            return True
        else:
            return False
      
    def run(self):
        previous = None
        while 1:
        # read gpio channel
            current = GPIO.input(self.channel)
            time.sleep(0.01) # wait 10 ms
            # detect change from 1 to 0 (a inductive press)
            if current == False and previous == True:
                self._pressed = True
                # wait for flag to be cleared
                while self._pressed:
                    time.sleep(0.05) # wait 50 ms
            previous = current

def output_csv_file(sensor,file):
   today = date.today()
   output_data_file = str(today) + "_" + sensor  + file
   return output_data_file

# define sensor function
def sensors_check():
    # GPIO.setup(gpio_pin, GPIO.IN)
    # GPIO.add_event_detect(gpio_pin, GPIO.BOTH, callback=callback_function, bouncetime=100)
    print("run sensors_check")
    file = '_data.csv'
    Inductive1_state = Inductive(23)
    Inductive2_state = Inductive(24)
    Inductive3_state = Inductive(25)
    Inductive4_state = Inductive(17)
    Inductive5_state = Inductive(27)
    Inductive6_state = Inductive(22)
    while True:
        if Inductive1_state.pressed():
            sensor="Sensor_1"
            csv_file=output_csv_file(sensor,file) 
            write_time_to_csv(csv_file,sensor)
            led_flash()
            print("Current state Inductive 1 On")
        elif Inductive2_state.pressed():
            sensor="Sensor_2"
            csv_file=output_csv_file(sensor,file) 
            write_time_to_csv(csv_file,sensor)
            led_flash()
            print("Current state Inductive 2 On")
        elif Inductive3_state.pressed():
           sensor="Sensor_3"
           csv_file=output_csv_file(sensor,file) 
           write_time_to_csv(csv_file,sensor)
           led_flash()
           print("Current state Inductive 3 On")
        elif Inductive4_state.pressed():
           sensor="Sensor_4"
           csv_file=output_csv_file(sensor,file) 
           write_time_to_csv(csv_file,sensor)
           led_flash()
           print("Current state Inductive 4 On")
        elif Inductive5_state.pressed():
           sensor="Sensor_5"
           csv_file=output_csv_file(sensor,file) 
           write_time_to_csv(csv_file,sensor)
           led_flash()
           print("Current state Inductive 5 On")
        elif Inductive6_state.pressed():
          sensor="Sensor_6"
          csv_file=output_csv_file(sensor,file) 
          write_time_to_csv(csv_file,sensor)
          led_flash()
          print("Current state Inductive 6 On")
 
try:
    print("run sensors_check")
    sensors_check()

except KeyboardInterrupt:
    print("Exiting...")


except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
