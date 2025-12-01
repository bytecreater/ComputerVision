import cv2

image = cv2.imread("lotr.png")

if image is None:
    print("OOPS! image couldn't load")
else:
    print("Image loaded successfully")
    center = (200,200)
    radius = 50
    color = (0,255,0)
    thickness = 4

    cv2.circle(image , center , radius , color , -1)
    cv2.imshow("Rectangle" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
