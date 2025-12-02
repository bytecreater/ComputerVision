import cv2 

cap = cv2.VideoCapture(0)

print("Webcam is loading....")

while True:
    ret , frame = cap.read() # ret = True/False frame=image

    if not ret:
        print("Couldnt read frame")
        break

    cv2.imshow("WebCam feed" , frame)

    if cv2.waitKey(1) & 0xff == ord('q'): 
        print("Quitting....")
        break

cap.release()
cv2.destroyAllWindows()