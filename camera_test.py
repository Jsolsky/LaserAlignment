from picamera2 import Picamera2
import io

# Initialize the camera
# This uses the default camera (usually index 0)
picam2 = Picamera2()

# Configure the camera for a standard image capture
# config = picam2.create_preview_configuration()
# picam2.configure(config)

# Start the camera (this initializes the sensor)
picam2.start()

stream = io.BytesIO()
picam2.capture_file(stream, format="jpeg")
stream.seek(0) # move to start of stream
image_jpeg_data = stream.read() 
print(f"Captured image size: {len(image_jpeg_data)} bytes")
picam2.stop()

with open("gaussian_none.jpg", "wb") as f:
    f.write(image_jpeg_data)

print("Image captured successfully")