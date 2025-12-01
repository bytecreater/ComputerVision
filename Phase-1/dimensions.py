import cv2

image = cv2.imread("LOTR.jpg")

if image is not None:
    h , w, c = image.shape
    print(f"Image Loaded\n Height:{h}\n Width:{w}\n Channels:{c}")
else:
    print("Could not load image")

