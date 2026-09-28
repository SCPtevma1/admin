import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1. อ่านภาพ (OpenCV อ่านภาพเข้ามาเป็น BGR)
img_bgr = cv2.imread("Screenshot 2026-09-25 215636.png")  # เปลี่ยน 'sample.jpg' เป็นชื่อไฟล์ภาพของคุณ
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# 2. แปลงพื้นที่สี (Color Space Conversion)
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
img_lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)

# 3. แยกช่องสัญญาณ (Channels) ของแต่ละพื้นที่สี
r, g, b = cv2.split(img_rgb)
h, s, v = cv2.split(img_hsv)
l, a, b_ = cv2.split(img_lab)

# จัดเก็บช่องสัญญาณลงใน Dictionary เพื่อเตรียมวนลูปแสดงผล
channels = {
    "R": r,
    "G": g,
    "B": b,
    "H": h,
    "S": s,
    "V": v,
    "L": l,
    "A": a,
    "B*": b_,
}

# 4. แสดงผลด้วย Matplotlib ในรูปแบบ Grid 3x3
fig, axes = plt.subplots(3, 3, figsize=(10, 10))

for ax, (name, ch) in zip(axes.flat, channels.items()):
    ax.imshow(ch, cmap="gray")  # แสดงผลแต่ละ channel เป็นภาพขาวดำ
    ax.set_title(name)
    ax.axis("off")  # ซ่อนแกน x, y

plt.tight_layout()
plt.show()