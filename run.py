import sys

import cv2

from config import CASCADES

ESC_CODE = 27


def is_user_wants_quit():
    return cv2.waitKey(3) & 0xFF == ESC_CODE


def show_frame(frame):
    cv2.imshow('Video', frame)


def draw_rect(frame, x, y, w, h, color):
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)


def make_cascades(cascades=None):
    """Collect cv2 cascade objects from config with nested cascads."""
    if cascades is None:
        return None
    return [
        {
            'cascade': cv2.CascadeClassifier(cascade['path']),
            'color': cascade['color'],
            'sub_cascades': make_cascades(cascade.get('sub_cascades', None))
        }
        for _, cascade in cascades.items()
        if cascade['draw']
    ]


def detect(cascades=None, gray_frame=None, cam_frame=None):
    """Detect objects in frame."""

    for cascade in cascades:
        color = cascade['color']
        captures = cascade['cascade'].detectMultiScale(
            gray_frame,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(30, 30)
        )
        sub_cascades = cascade['sub_cascades']
        for (x, y, w, h) in captures:
            draw_rect(cam_frame, x, y, w, h, color)

            if sub_cascades is not None:
                detect(
                    sub_cascades,
                    gray_frame[y:y + h, x:x + w],
                    cam_frame[y:y + h, x:x + w]
                )


def main():
    cascades = make_cascades(CASCADES)
    video_capture = cv2.VideoCapture(0)

    while True:
        if not video_capture.isOpened():
            print("Couldn't find your webcam... Sorry :c")
            sys.exit(0)

        _, cam_frame = video_capture.read()
        gray_frame = cv2.cvtColor(cam_frame, cv2.COLOR_BGR2GRAY)
        detect(
            cascades=cascades,
            gray_frame=gray_frame,
            cam_frame=cam_frame
        )
        show_frame(cam_frame)

        if is_user_wants_quit():
            break

    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
