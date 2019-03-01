import cv2

capture = cv2.VideoCapture("../videos/video.mp4")

while True:
    ret, frame = capture.read()
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()