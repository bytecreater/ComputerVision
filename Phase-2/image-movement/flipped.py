import cv2 

image = cv2.imread("resized_image.png")

if image is not None:
    flipped_vertical = cv2.flip(image , 0)
    flipped_horizontal = cv2.flip(image , 1)
    flipped_both = cv2.flip(image , -1)
    cv2.imshow("Original image" , image)
    cv2.imshow("Rotated image vertical" , flipped_vertical)
    cv2.imshow("Rotated image horizontal" , flipped_horizontal)
    cv2.imshow("Rotated image both" , flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()