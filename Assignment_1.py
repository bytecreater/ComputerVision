# # Load the image
# # Grayscale
# # show (take display name as input from user)
# # save image (take saving name from user)

import cv2

image = cv2.imread("LOTR.jpg")

if image is not None:
    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    name = input("Enter the diaplay title : ")
    cv2.imshow(name , gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    saving_name = input("Enter the saving name : ")
    cv2.imwrite(saving_name , image)
else:
    print("Error in loading the image")
