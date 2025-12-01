import cv2 

image = cv2.imread("LOTR.jpg")

if image is not None:

    cropped = image[200:800 , 1200:1800] #(height_start : height_end , width_start : width_end)
    cv2.imshow("Original Image" , image)
    cv2.imshow("Cropped Image" , cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("Error: Could not load image")
