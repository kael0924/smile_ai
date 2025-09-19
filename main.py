import cv2 
import modules.smile_detector

# Load the cascade


# Start web Cam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open Web Cam")
    exit()

while True:
    result, video_frame = camera.read()

    if result is False:
        print("Error: Failed to grab frame.")
        break

    modules.smile_detector.detect_bounding_box(video_frame)

    cv2.imshow("Webcam Feed", video_frame)

    #Exit on q key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()