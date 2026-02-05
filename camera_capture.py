from picamera2 import Picamera2
import io
from PIL import Image
import numpy as np
import time

picam2 = Picamera2()

def get_pi_temperature():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            # The value is in millidegrees (e.g., 45000 for 45°C)
            temp_raw = int(f.read())
            return temp_raw / 1000.0
    except FileNotFoundError:
        # Useful for when you're testing on your desktop (which won't have this file)
        return 0.0

# temp = get_pi_temperature()
# print("t: ", temp)


# current_temp = get_pi_temperature()
# print(f"Core Temperature: {current_temp}°C - {i}")

picam2.start()

i = 1
while i <= 1000:
    image_array = picam2.capture_array()
    image = Image.fromarray(image_array, 'RGBA')
    image.convert('RGB').save(f"dirty_signal_stream_smudge/image{i}.jpg")
    time.sleep(0.033)
    i+=1

picam2.stop()

# print(f"Captured image size: {len(image_jpeg_data)} bytes")

