import tellopy
import time

# Connect to the Tello drone
drone = tellopy.Tello()
drone.connect()

# Start the video stream (optional)
drone.start_video()

# Takeoff
drone.takeoff()

# Move forward 50 centimeters
drone.move_forward(50)

# Wait for a few seconds
time.sleep(5)

# Land
drone.land()

