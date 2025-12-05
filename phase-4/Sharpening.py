import cv2
import numpy as np

image = cv2.imread("myimage.png")

sharp_kernel = np.array([
    [0, -1, 0],
    [-1, 5,-1],
    [0, -1, 0]
])

blurred = cv2.filter2D(image,-1,sharp_kernel)

cv2.imshow("Original Image" , image)
cv2.imshow("Blurred image" , blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()