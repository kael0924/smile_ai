import cv2

def detect_bounding_box(vid) -> None:
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    smile_cascade =  cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))

    for(x, y, width, height) in faces:
        cv2.rectangle(vid, (x, y), (x + width, y + height), (0, 255, 0), 4)
        gray_temp = gray_image[y: y + height, x: x + width]

        smile = smile_cascade.detectMultiScale(gray_temp, scaleFactor=1.3, minNeighbors=25)
        for i in smile:
            if len(smile) > 1 :
                cv2.putText(vid, "Smiling", (x, y - 50), cv2.FONT_HERSHEY_PLAIN, 2, (255,0 , 0), 3, cv2.LINE_AA)

    return
    