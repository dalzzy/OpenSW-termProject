import cv2
import os
import numpy as np

PROTOTXT = "models/deploy.prototxt" # 모델 구조 정의 파일
MODEL = "models/res10_300x300_ssd_iter_140000.caffemodel" # 훈련된 가중치 파일
CONFIDENCE_THRESHOLD = 0.3 # 검출 임계값

def load_face_detector():

    if not os.path.exists(PROTOTXT) or not os.path.exists(MODEL):
        print("[Error] DNN 모델 파일(prototxt 또는 caffemodel)을 찾을 수 없습니다.")
        return None
        
    #모델 로드    
    net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
    return net

def detect_faces(image, net):
    """DNN 모델을 사용하여 이미지에서 얼굴 영역 좌표(x, y, w, h)를 검출"""

    (h, w) = image.shape[:2]

    blob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)), 
        1.0, 
        (300, 300), 
        (104.0, 177.0, 123.0)
    )

    net.setInput(blob)
    detections = net.forward() # 검출 결과 (N x 7 배열)

    faces = []
    
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2] 
        
        if confidence > CONFIDENCE_THRESHOLD:

            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            
            x, y, w_box, h_box = startX, startY, endX - startX, endY - startY
            faces.append((x, y, w_box, h_box))

    print(f"face: {len(faces)}")
    return faces