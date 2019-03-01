import cv2

image = cv2.imread("../images/fruits.jpg")
blue, green, red = cv2.split(image)

cv2.imshow("R Chanel", red)
cv2.imshow("G Chanel", green)
cv2.imshow("B Chanel", blue)

cv2.imwrite("fruits-chanel-red.jpg", red)
cv2.imwrite("fruits-chanel-green.jpg", green)
cv2.imwrite("fruits-chanel-blue.jpg", blue)

cv2.waitKey(0)
cv2.destroyAllWindows()