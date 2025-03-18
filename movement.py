import RPi.GPIO as GPIO
import time

# GPIO setup
PIR_PIN = 17  # GPIO pin connected to PIR sensor OUT
GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbering
GPIO.setup(PIR_PIN, GPIO.IN)

print("PIR Motion Sensor Test (CTRL+C to exit)")
time.sleep(2)  # Allow PIR sensor to initialize

try:
    while True:
        if GPIO.input(PIR_PIN):  # Check if PIR sensor output is HIGH
            print("Motion detected!")
        else:
            print("No motion")
        time.sleep(1)  # Delay to reduce CPU usage
except KeyboardInterrupt:
    print("Exiting program...")
finally:
    GPIO.cleanup()  # Clean up GPIO settings
