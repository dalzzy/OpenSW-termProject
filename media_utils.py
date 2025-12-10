import cv2
import os

def load_image(filepath):
    """
    이미지 파일을 불러오는 함수
    :param filepath: 파일 경로 (예: 'data/sample.jpg')
    :return: 이미지 객체 (실패 시 None)
    """
   
    if not os.path.exists(filepath):
        print(f"[Error] 파일을 찾을 수 없습니다: {filepath}")
        return None
    
   
    image = cv2.imread(filepath)
    
    if image is None:
        print(f"[Error] 이미지 형식이 잘못되었습니다: {filepath}")
        return None
        
    print(f"[System] 이미지를 성공적으로 불러왔습니다: {filepath}")
    return image

def save_image(image, output_path):
    """
    처리된 이미지를 저장하는 함수
    """
    if image is None:
        print("[Error] 저장할 이미지가 비어있습니다.")
        return False
        

    success = cv2.imwrite(output_path, image)
    
    if success:
        print(f"[System] 저장 완료! -> {output_path}")
    else:
        print(f"[Error] 저장 실패. 경로를 확인해주세요.")
    
    return success


if __name__ == "__main__":
   
    img = load_image("test.jpg")
    if img is not None:
        save_image(img, "result_test.jpg")