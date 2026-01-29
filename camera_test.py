# Initialize the camera
# This uses the default camera (usually index 0)
picam2 = Picamera2()

# Configure the camera for a standard image capture
config = picam2.create_preview_configuration()
picam2.configure(config)

# Start the camera (this initializes the sensor)
picam2.start()

# Capture an image and save it to the current directory
picam2.capture_file("my_photo.jpg")

# Stop the camera to release the resource
picam2.stop()

print("Image captured successfully as 'my_photo.jpg'!")