# OpenCV Face Mosaic Processor (Privacy Protector Project)

This project uses **OpenCV’s DNN face detection model (SSD ResNet10)** and  
**image processing techniques (mosaic / blur)**  
to automatically detect and anonymize faces in images.

---

## 📌 Key Features

### 1. Image Loading & Saving

- Load image files from local storage
- Save processed images to a specified output path

---

### 2. Automatic Face Detection (OpenCV DNN)

- Utilizes `deploy.prototxt` and `res10_300x300_ssd_iter_140000.caffemodel`
- SSD-based face detection
- Supports detecting multiple faces

---

### 3. Face Mosaic / Blur Processing

- Adjustable mosaic intensity (`--mosaic-size`)
- Adjustable Gaussian blur strength (`--blur-ksize`)

---

### 4. CLI-Based Execution (`main.py`)

Run the program with simple terminal commands and configurable options.

---

## 📦 Used Packages & Versions
The following packages are required to run this project:
- **Python 3.9+** : Recommended Python version for running this project.
- **OpenCV (opencv-python) 4.9.0+** : Used for DNN-based face detection and image processing.
- **NumPy 1.26.0+** : Required for numerical computations and matrix operations.
## 📁 Folder Structure

```
📂image
┃ ┗ 📜horse.jpg
┣ 📂models
┃ ┣ 📜deploy.prototxt
┃ ┗ 📜res10*300x300*ssd_iter_140000.caffemodel
┣ 📂result
┃ ┗ 📜mosaic_result.jpg
┣ 📜README.md
┣ 📜face_detect.py
┣ 📜face_mosaic.py
┣ 📜face_mosaic_.py
┣ 📜main.py
┣ 📜media_utils.py
┗ 📜media_utils_.py
```

- `face_mosaic.py`
- `face_mosaic_.py`
- `media_utils.py`
- `media_utils_.py`

These duplicate files were created because of **encoding issues on macOS**.  
Both versions contain the **same code**, and only one of them is actually used in the project.

## 🚀 How to Run

### 1. Install Required Libraries

`pip install opencv-python numpy`

### 2. Run the Program

`python3 main.py --image image/horse.jpg --effect mosaic --mosaic-size 15`

## 📸 Result

| Before | After |
|--------|-------|
| ![horse](https://github.com/user-attachments/assets/f01fde06-7489-4450-89d4-881ead8bf7cf) | ![mosaic_result](https://github.com/user-attachments/assets/34808989-cb29-448d-9a62-89b772ec3a79) |

