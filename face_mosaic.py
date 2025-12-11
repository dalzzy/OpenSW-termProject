import cv2
import os
from face_detect import load_face_detector, detect_faces
from media_utils import load_image, save_image


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


def main():
    # 1) 이미지 불러오기
    image_path = "image/sample.jpg"  
    img = load_image(image_path)
    if img is None:
        return

    # 2) 얼굴 검출 모델 불러오기
    net = load_face_detector()
    if net is None:
        return

    faces = detect_faces(img, net)
    print("[System] 검출된 얼굴 개수:", len(faces))

    if len(faces) == 0:
        print("[System] 얼굴이 검출되지 않아 효과를 적용하지 않습니다.")
        return

    # 3) 모자이크 또는 블러 선택 적용
    # mosaic_result = apply_mosaic(img, faces, mosaic_size=15)
    blur_result = apply_blur(img, faces, ksize=31)

    # 4) 결과 저장
    os.makedirs("result", exist_ok=True)
    output_path = "result/face_blur_result.jpg"
    save_image(blur_result, output_path)

    # 5) 화면 출력
    cv2.imshow("Original", img)
    cv2.imshow("Blur Result", blur_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()