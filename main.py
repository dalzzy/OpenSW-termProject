import argparse
import os
import cv2
from media_utils_ import load_image, save_image
from face_detect import load_face_detector, detect_faces
from face_mosaic_ import apply_mosaic, apply_blur

def run(image_path, effect, mosaic_size=15, blur_ksize=31):
    # 1) 이미지 불러오기
    img = load_image(image_path)
    if img is None:
        return

    # 2) 모델 로드
    net = load_face_detector()
    if net is None:
        print("[Error] 얼굴 검출 모델을 불러오지 못했습니다.")
        return

    # 3) 얼굴 검출
    faces = detect_faces(img, net)
    print(f"[System] 검출된 얼굴 수: {len(faces)}")

    if len(faces) == 0:
        print("[System] 얼굴이 없어 효과 적용 생략.")
        return

    # 4) 효과 적용
    if effect == "mosaic":
        result = apply_mosaic(img, faces, mosaic_size=mosaic_size)
        output_name = "mosaic_result.jpg"

    elif effect == "blur":
        result = apply_blur(img, faces, ksize=blur_ksize)
        output_name = "blur_result.jpg"

    else:
        print("[Error] 지원하지 않는 효과입니다.")
        return

    # 5) 결과 저장
    os.makedirs("result", exist_ok=True)
    output_path = os.path.join("result", output_name)
    save_image(result, output_path)

    # 6) 결과 화면 출력
    cv2.imshow("Original", img)
    cv2.imshow("Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def parse_arguments():
    parser = argparse.ArgumentParser(description="Face Mosaic / Blur Processor")

    parser.add_argument(
        "--image",
        type=str,
        required=True,
        help="입력 이미지 경로 (예: image/test.jpg)"
    )

    parser.add_argument(
        "--effect",
        type=str,
        choices=["mosaic", "blur"],
        required=True,
        help="적용할 효과 선택: mosaic 또는 blur"
    )

    parser.add_argument(
        "--mosaic-size",
        type=int,
        default=15,
        help="모자이크 픽셀 크기 (기본값: 15)"
    )

    parser.add_argument(
        "--blur-ksize",
        type=int,
        default=31,
        help="블러 커널 크기 (기본값: 31 / 홀수만 가능)"
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    run(
        image_path=args.image,
        effect=args.effect,
        mosaic_size=args.mosaic_size,
        blur_ksize=args.blur_ksize
    )
