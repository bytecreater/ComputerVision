import cv2

image = cv2.imread("LOTR.jpg")

if image is not None:
    cv2.imshow("Image Showing" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could not load image")

