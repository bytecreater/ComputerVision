import cv2 

image = cv2.imread("lotr.png")

blurred = cv2.GaussianBlur(image, (3,3) , 3)

cv2.imshow("Original Image" , image)
cv2.imshow("Blurred image" , blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()