from curses.ascii import FF

import cv2

framewidth = 640
frameHeight = 480
noplateCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")
color = (255, 0, 255)
cap = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameHeight)
cap.set(10, 150)
while True:
    sucess, img = cap.read()
    img = cv2.resize(img, (800, 600))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = noplateCascade.detectMultiScale(imgGray, 1.1, 2)
    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > 500:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # yo put rectangle around our biggest
            # contour here our number plate
            cv2.putText(img, "Number plate", (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
            imgRoi = img[y:y + h, x:x + w]  # image with our region of interest
            cv2.imshow("ROI", imgRoi)

    cv2.imshow("result", img)
    if cv2.waitKey(1) & 0 * FF == ord('q'):
        break
