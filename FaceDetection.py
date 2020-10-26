import cv2

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
img = cv2.imread(r'C:\Users\Jeevan\PycharmProjects\CartoonMaking\Resources\Sample.jpeg')
img = cv2.resize(img, (800, 600))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converting image into grayscale image

faces = faceCascade.detectMultiScale(imgGray, 1.1, 2)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)
