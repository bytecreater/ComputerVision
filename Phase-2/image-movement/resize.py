import cv2 

image = cv2.imread("LOTR.jpg")

if image is None:
    print("Error: Could not load image")
else:
    print("Image is loaded successfully")

    resize = cv2.resize(image , (600, 300)) # (width , height)
    cv2.imshow("Resize Image" , resize)
    cv2.imwrite("resized_image.png" , resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
