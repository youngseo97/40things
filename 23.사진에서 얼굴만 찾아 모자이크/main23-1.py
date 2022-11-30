import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')

ff = np.fromfile(r'test1.jpg', np.uint8)
img = cv2.imdecode(ff,cv2.IMREAD_UNCHANGED)#이미지파일을 alpha channel까지 포함하여 읽는는다.
img = cv2.resize(img, dsize=(0,0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)#출력이미지 픽셀단위로 설정

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.2,5)#여러개의 얼굴을 찾는함수
for (x,y,w,h) in faces :
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

    roi_gray = img[y:y+h, x:x+w]
    roi_gary = cv2.blur(roi_gray,(10,10))
    img_w_mosaic = img
    img_w_mosaic[y:y+h, x:x+w]=roi_gary
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh),(0,255,0),2)

cv2.imshow('face find', img)
cv2.waitKey(0)
cv2.destroyAllWindows()