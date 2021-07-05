import cv2

cam = cv2.VideoCapture(1, cv2.CAP_DSHOW) #creates a video capture object that captures video from webcam
cam.set(3, 640) #set video frame width
cam.set(4, 480) #set video frame height


detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

face_id = input("Enter a numeric user id here: ")

print("Taking Samples look at the camera ........... ")
count = 0

while True:

    ret, img = cam.read()
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(converted_image, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (225,0,0), 2)
        count += 1

        cv2.imwrite("samples/face." + str(face_id) + '.' + str(count) + ".jpg", converted_image[y:y+h, x:x+w])

        cv2.imshow('write', img)

    k = cv2.waitKey(100) & 0xff
    if k == 27: #press esc to stop
        break
    elif count >=10: #can add samples more samples = more accuracy
        break

print("Samples taken now closing the program....")
cam.release()
cv2.destroyAllWindows()