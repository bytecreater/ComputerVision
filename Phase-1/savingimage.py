import cv2

image = cv2.imread("LOTR.jpg")

if image is not None:
    success = cv2.imwrite("output_python.png" , image)
    if success :
        print("Image saved successfully as 'output_python'")
    else:
        print("Image failed to save")
else:
    print("Error : Could not load image")

