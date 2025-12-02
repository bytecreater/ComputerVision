import cv2

image = cv2.imread("lotr.png")

if image is None:
    print("OOPS! image couldn't load")
else:
    print("Image loaded successfully")
    pt1 = (10,20)
    pt2 = (100,200)
    color = (255,0,0)
    thickness = 4

    cv2.putText(image , "Hi from Nihal" , (50,100) , cv2.FONT_HERSHEY_SIMPLEX,1.2,color ,thickness)
    cv2.imshow("TEXT" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
