import cv2
import threading
import time
from djitellopy import Tello

# Initialize the Tello drone
tello = Tello()
tello.connect()
tello.streamon()

tello.takeoff()

# Create a VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (960, 720))

# Function to receive and record video
def receive_video():
    start_time = time.time()
    while True:
        try:
            frame = tello.get_frame_read().frame
            out.write(frame)
            cv2.imshow('Tello Video', frame)

            # Check if 5 seconds have elapsed
            if time.time() - start_time >= 5:
                break

            # Exit the program if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except KeyboardInterrupt:
            break

# Start video reception in a separate thread
video_thread = threading.Thread(target=receive_video)
video_thread.start()

# Hover until 5 seconds have elapsed
tello.send_rc_control(0, 0, 0, 0)
time.sleep(5)

# Stop video recording and release resources
video_thread.join()
out.release()
cv2.destroyAllWindows()

# Land the Tello
tello.land()

# Disconnect from the Tello
tello.streamoff()
tello.disconnect()
