import cv2

image = cv2.imread("myimage.png")

blurred = cv2.medianBlur(image,3)

cv2.imshow("Original Image" , image)
cv2.imshow("Blurred image" , blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()