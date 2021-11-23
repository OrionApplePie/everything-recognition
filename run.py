import sys

import cv2

from config import CASCADES


def is_user_wants_quit():
    return cv2.waitKey(1) & 0xFF == ord('q')


def show_frame(frame):
    cv2.imshow('Video', frame)


def draw_rect(frame, x, y, w, h, color):
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)


def get_cascades():
    return [
        (cv2.CascadeClassifier(cascade['path']), cascade['color'])
        for _, cascade in CASCADES.items()
        if cascade['draw']
    ]


def main():
    cascades = get_cascades()
    video_capture = cv2.VideoCapture(0)

    while True:
        if not video_capture.isOpened():
            print("Couldn't find your webcam... Sorry :c")
            sys.exit(0)
        _, webcam_frame = video_capture.read()
        gray_frame = cv2.cvtColor(webcam_frame, cv2.COLOR_BGR2GRAY)

        for cascade, color in cascades:
            captures = cascade.detectMultiScale(
                    gray_frame,
                    scaleFactor=1.1,
                    minNeighbors=10,
                    minSize=(30, 30)
                )
            for (x, y, w, h) in captures:
                draw_rect(webcam_frame, x, y, w, h, color)
        show_frame(webcam_frame)

        if is_user_wants_quit():
            break
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
