import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

# Defining a function that will do the detections
def detect(gray, frame):
    gray1 = None
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w] 
        gray1 = roi_gray 
    return gray1

# Doing some Face Recognition with the webcam
video_capture = cv2.VideoCapture(0)

i = 0
while (i < 300):
    print('vijani ' + str(i))
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   
    face = detect(gray, frame)
    
    if face is not None:
        print('/home/vijani/Desktop/movetopi/images/img'+ str(i) + '.jpg')
        cv2.imwrite('/home/vijani/Desktop/movetopi/images/img'+ str(i) + '.jpg', face)

    i = i + 1
'''
    cv2.imshow('Video', face)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
'''
