import RPi.GPIO as GPIO
import time

# Pin configuration
LDR_PIN = 18  # GPIO pin connected to the LDR

# Setup GPIO
GPIO.setmode(GPIO.BCM)
#GPIO.setup(LDR_PIN, GPIO.OUT)
GPIO.setup(LDR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def measure_light():
    #print("Discharging capacitor...")
    GPIO.setup(LDR_PIN, GPIO.OUT)
    GPIO.output(LDR_PIN, GPIO.LOW)
    time.sleep(0.1)

    #print("Measuring time...")
    GPIO.setup(LDR_PIN, GPIO.IN)
    start_time = time.time()
    while GPIO.input(LDR_PIN) == GPIO.LOW:
        pass
    end_time = time.time()

    duration = end_time - start_time
    #print(f"Measured duration: {duration:.6f} seconds")
    return duration

try:
    while True:
        light_level = measure_light()
        print(f"Light Level: {light_level:.6f} seconds")
        time.sleep(0.1)  # Wait 1 second before the next reading

except KeyboardInterrupt:
    print("Exiting program...")

finally:
    GPIO.cleanup()
