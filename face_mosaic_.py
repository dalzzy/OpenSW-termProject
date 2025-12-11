# utf-8 인코딩 문제로 face_mosiac.py -> face_mosaic_.py 로 파일명 변경

import cv2
import os
from face_detect import load_face_detector, detect_faces
from media_utils_ import load_image, save_image


def apply_mosaic(image, faces, mosaic_size: int = 15):
    output = image.copy()

    for (x, y, w, h) in faces:
        x = max(0, x)
        y = max(0, y)
        w = max(1, w)
        h = max(1, h)

        x2 = min(output.shape[1], x + w)
        y2 = min(output.shape[0], y + h)

        roi = output[y:y2, x:x2]

        if roi.size == 0:
            continue

        small_w = max(1, w // mosaic_size)
        small_h = max(1, h // mosaic_size)

        small = cv2.resize(roi, (small_w, small_h), interpolation=cv2.INTER_LINEAR)
        mosaic = cv2.resize(small, (x2 - x, y2 - y), interpolation=cv2.INTER_NEAREST)

        output[y:y2, x:x2] = mosaic

    return output


def apply_blur(image, faces, ksize: int = 31):
    output = image.copy()

    if ksize % 2 == 0:
        ksize += 1

    for (x, y, w, h) in faces:
        x = max(0, x)
        y = max(0, y)
        w = max(1, w)
        h = max(1, h)

        x2 = min(output.shape[1], x + w)
        y2 = min(output.shape[0], y + h)

        roi = output[y:y2, x:x2]

        if roi.size == 0:
            continue

        blurred = cv2.GaussianBlur(roi, (ksize, ksize), 0)
        output[y:y2, x:x2] = blurred

    return output
