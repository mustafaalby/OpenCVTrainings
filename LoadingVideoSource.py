import numpy as np
import cv2
import sys

print("1 for video capture")
print("2 for video from file")
final = sys.argv[1]
print(final)


def main():

    cap = cv2.VideoCapture(0)  # getting video from webcam
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # the codec we wanna use
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(frame)
        cv2.imshow('frame', frame)
        cv2.imshow('gray', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


main()
