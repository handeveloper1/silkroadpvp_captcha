import cv2

img = cv2.imread("ss.png")
print(img.shape)  #image boyutları

imgcropped = img[355:415,385:635]  #kroplama




cv2.imshow("image crop", imgcropped)



cv2.waitKey(0)