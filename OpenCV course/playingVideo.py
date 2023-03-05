import cv2

cap = cv2.VideoCapture("captured_video.MP4")

while(True):
    ret, frame = cap.read()     #capture the video frame by frame

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
