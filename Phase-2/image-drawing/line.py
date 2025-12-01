import cv2

image = cv2.imread("lotr.png")

if image is None:
    print("OOPS! image couldn't load")
else:
    print("Image loaded successfully")
    pt1 = (10,20)
    pt2 = (1000,20)
    color = (0,255,0)
    thickness = 4

    cv2.line(image , pt1 , pt2 , color ,thickness)
    cv2.imshow("Line Drawing" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
