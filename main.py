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
tello.move_forward(100)
time.sleep(1)

tello.move_down(20)

tello.move_left(20)

tello.move_right(40)

tello.move_back(100)

# Land
tello.land()

# Disconnect from the drone
tello.end()
