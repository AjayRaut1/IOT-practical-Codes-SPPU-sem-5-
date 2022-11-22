#3.Write an application to capture and store the image.

import picamera, time
camera = picamera.PiCamera()
camera.start_preview()
time.sleep(5) # hang for preview for 5 seconds
camera.capture('snapshot.jpg')
camera.stop_preview()