import cv2
import numpy as np


def nothing(x):
    pass


# 1. อ่านภาพและแปลงเป็น HSV
img = cv2.imread("Screenshot 2026-09-25 215636.png")  # เปลี่ยน 'object_sample.jpg' เป็นชื่อไฟล์ภาพของคุณ
img = cv2.resize(img, (500, 400))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 2. สร้างหน้าต่างสำหรับ Trackbar
cv2.namedWindow("Trackbars")

# สร้าง Trackbar ทั้ง 6 ตัวเพื่อปรับค่า HSV (Min/Max)
cv2.createTrackbar("H min", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("H max", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("S min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("S max", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("V min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("V max", "Trackbars", 255, 255, nothing)

# 3. ลูปประมวลผลแบบ Real-time
while True:
    # ดึงค่าปัจจุบันจาก Trackbar
    h_min = cv2.getTrackbarPos("H min", "Trackbars")
    h_max = cv2.getTrackbarPos("H max", "Trackbars")
    s_min = cv2.getTrackbarPos("S min", "Trackbars")
    s_max = cv2.getTrackbarPos("S max", "Trackbars")
    v_min = cv2.getTrackbarPos("V min", "Trackbars")
    v_max = cv2.getTrackbarPos("V max", "Trackbars")

    # กำหนดช่วงสี Threshold (Lower Bound และ Upper Bound)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # สร้าง Mask และตัดเฉพาะบริเวณที่มีสีตามช่วงที่เลือก
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    # แสดงผลหน้าต่างภาพ
    cv2.imshow("Original", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    # กดปุ่ม 'q' เพื่อออกจากโปรแกรมและพิมพ์ค่าที่เลือกไว้
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print(f"ค่าที่ใช้: Lower={lower}, Upper={upper}")
        break

cv2.destroyAllWindows()