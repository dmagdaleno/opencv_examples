import cv2

image = cv2.imread("../images/fruits.jpg")
blue, green, red = cv2.split(image)

merged_image = cv2.merge((blue, green, red))
cv2.imshow("Merged Image", merged_image)

cv2.waitKey(0)
cv2.destroyAllWindows()