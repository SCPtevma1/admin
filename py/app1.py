import cv2
import numpy as np
import matplotlib.pyplot as plt

# ชื่อไฟล์ภาพอาคาร
img_filename = 'wal_172619-building-7394332_1920.jpg'

# อ่านภาพต้นฉบับ (Grayscale)
img = cv2.imread(img_filename, cv2.IMREAD_GRAYSCALE)

# ป้องกันกรณีหาไฟล์ภาพไม่พบ
if img is None:
    raise FileNotFoundError(f"ไม่พบไฟล์ '{img_filename}' กรุณาตรวจสอบชื่อไฟล์และโฟลเดอร์")

# TODO 1: Sobel Gx, Gy
gx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# TODO 2: Magnitude
magnitude = np.sqrt(gx**2 + gy**2)

# TODO 3: Canny (ลองปรับค่า threshold)
edges1 = cv2.Canny(img, 50, 150)
edges2 = cv2.Canny(img, 100, 200)

# TODO 4: Harris Corner
# แก้ไขจุดนี้: เปลี่ยนชื่อไฟล์ให้ตรงกัน
img_color = cv2.imread(img_filename)
img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)

gray = np.float32(img)
harris = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

thresh = 0.01 * harris.max()
corners = np.where(harris > thresh)

for y, x in zip(corners[0], corners[1]):
    cv2.circle(img_color, (x, y), 3, (255, 0, 0), -1)

# TODO 5: plt.subplot แสดงผลทั้งหมด
plt.figure(figsize=(14, 8))

plt.subplot(2, 4, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Gray')
plt.axis('off')

plt.subplot(2, 4, 2)
plt.imshow(np.abs(gx), cmap='gray')
plt.title('Sobel Gx')
plt.axis('off')

plt.subplot(2, 4, 3)
plt.imshow(np.abs(gy), cmap='gray')
plt.title('Sobel Gy')
plt.axis('off')

plt.subplot(2, 4, 4)
plt.imshow(magnitude, cmap='gray')
plt.title('Sobel Magnitude')
plt.axis('off')

plt.subplot(2, 4, 5)
plt.imshow(edges1, cmap='gray')
plt.title('Canny (50, 150)')
plt.axis('off')

plt.subplot(2, 4, 6)
plt.imshow(edges2, cmap='gray')
plt.title('Canny (100, 200)')
plt.axis('off')

plt.subplot(2, 4, 7)
plt.imshow(img_color)
plt.title('Harris Corner')
plt.axis('off')

plt.tight_layout()
plt.show()