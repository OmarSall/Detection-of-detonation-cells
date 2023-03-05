import cv2
from abc import ABC

cap = cv2.VideoCapture(0)

if (cap.isOpened() == False):
    print("Camera could not open")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))


#video coded ... encoders and decoders

video_cod = cv2.VideoWriter_fourcc(*'XVIO')
video_output = cv2.VideoWriter('Captured_video.MP4', video_cod, 30, (frame_width, frame_height))


while(True):
    ret, frame = cap.read()     #capture the video frame by frame

    if ret == True:
        video_output.write(frame)
        cv2.imshow('frame', frame)

    # cv2.imshow("frame" , frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()

cv2.destroyAllWindows()

print("The video was saved sucessfully")