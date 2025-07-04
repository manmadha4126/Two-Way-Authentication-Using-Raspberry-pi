import time
import serial
import Adafruit_DHT
import RPi.GPIO as GPIO
import firebase_admin
from firebase_admin import credentials, db

# Firebase setup
cred = credentials.Certificate("firebase_key.json")  # Your Firebase service account key
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://<your-database-name>.firebaseio.com/'  # Replace with your Firebase DB URL
})

# Pin configuration
DHT_PIN = 4            # GPIO4 for DHT22
BUZZER_PIN = 17        # GPIO17
LED_PIN = 27           # GPIO27
RELAY_PIN = 22         # GPIO22

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(RELAY_PIN, GPIO.OUT)

# Fingerprint sensor over UART
fp = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

# Threshold values
TEMP_THRESHOLD = 35
HUM_THRESHOLD = 80

# Authentication function
def read_dht22():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, DHT_PIN)
    return round(temperature, 2), round(humidity, 2)

def trigger_access():
    print("Access Granted")
    GPIO.output(LED_PIN, True)
    GPIO.output(RELAY_PIN, True)
    GPIO.output(BUZZER_PIN, False)
    time.sleep(5)
    GPIO.output(LED_PIN, False)
    GPIO.output(RELAY_PIN, False)

def check_fingerprint():
    fp.write(b'\x55\xAA\x01\x00\x01\x00\x00\x01\x01')  # Command to capture fingerprint
    time.sleep(2)
    data = fp.read_all()
    return b'\x00\x00' in data  # Simulate success

def verify_otp():
    otp_ref = db.reference('auth/otp')
    current_otp = otp_ref.get()
    user_input = input("Enter OTP from mobile app: ").strip()
    return user_input == current_otp

try:
    while True:
        print("Waiting for fingerprint...")
        if check_fingerprint():
            print("Fingerprint matched.")
            temp, hum = read_dht22()
            print(f"Temperature: {temp}°C | Humidity: {hum}%")
            
            if temp <= TEMP_THRESHOLD and hum <= HUM_THRESHOLD:
                print("Environmental check passed.")
                if verify_otp():
                    trigger_access()
                else:
                    print("Invalid OTP.")
                    GPIO.output(BUZZER_PIN, True)
                    time.sleep(1)
                    GPIO.output(BUZZER_PIN, False)
            else:
                print("Environmental conditions failed.")
                GPIO.output(BUZZER_PIN, True)
                time.sleep(1)
                GPIO.output(BUZZER_PIN, False)
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()
    fp.close()
