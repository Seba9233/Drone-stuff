from djitellopy import Tello
import time

# Initialize the Tello drone
tello = Tello()

# Connect to the drone
tello.connect()

# Print battery percentage
print("Battery:", tello.get_battery(), "%")

# Take off
tello.takeoff()

# Fly forward for 100 cm
tello.move_forward(10)

# Turn clockwise by 90 degrees
tello.rotate_clockwise(90)

# Land
tello.land()

# Disconnect from the drone
tello.end()
