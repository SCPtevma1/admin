import cv2
import numpy as np

print("🔄 กำลังสร้างภาพจำลองในหน่วยความจำเพื่อทดสอบระบบ...")

# 1. สร้างภาพจำลองขึ้นมาแทนการเปิดไฟล์จากเครื่อง (ตัดปัญหาเรื่องหาไฟล์ไม่เจอ)
img = np.random.randint(0, 256, (400, 400, 3), dtype=np.uint8)
cv2.circle(img, (200, 200), 100, (100, 150, 200), -1)

# สร้าง Ground Truth Mask จำลองขึ้นมา (วงกลมสีขาวตรงกลาง)
gt_mask = np.zeros((400, 400), dtype=np.uint8)
cv2.circle(gt_mask, (200, 200), 90, 255, -1)


# 2. ฟังก์ชันตรวจจับผิวหนังด้วยกฎพื้นที่สี RGB (อ้างอิง Kovac et al.)
def skin_mask_rgb(img):
    b, g, r = cv2.split(img.astype(np.int32))
    mask = (
        (r > 95)
        & (g > 40)
        & (b > 20)
        & ((np.max(img, axis=2) - np.min(img, axis=2)) > 15)
        & (np.abs(r - g) > 15)
        & (r > g)
        & (r > b)
    )
    return (mask * 255).astype(np.uint8)


# 3. ฟังก์ชันตรวจจับผิวหนังด้วยช่วงสี HSV (เติมค่าอาร์เรย์ให้เต็มเรียบร้อย)
def skin_mask_hsv(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 30, 60])
    upper = np.array([20, 150, 255])
    return cv2.inRange(hsv, lower, upper)


# 4. ฟังก์ชันตรวจจับผิวหนังด้วยช่วงสี LAB (เน้นช่อง a, b)
def skin_mask_lab(img):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    mask = (a > 130) & (a < 170) & (b > 130) & (b < 175)
    return (mask * 255).astype(np.uint8)


# 5. ฟังก์ชันประเมินผลเชิงปริมาณ (Precision, Recall, F1-score)
def evaluate(pred_mask, gt_mask):
    pred = (pred_mask > 0).astype(np.uint8).flatten()
    gt = (gt_mask > 0).astype(np.uint8).flatten()

    tp = np.sum((pred == 1) & (gt == 1))
    fp = np.sum((pred == 1) & (gt == 0))
    fn = np.sum((pred == 0) & (gt == 1))

    precision = tp / (tp + fp + 1e-6)
    recall = tp / (tp + fn + 1e-6)
    f1 = 2 * precision * recall / (precision + recall + 1e-6)

    return precision, recall, f1


# 6. รันคำนวณและสรุปผลทั้ง 3 วิธี
results = {}
print("\n" + "="*50)
print(f"{'Color Space':<12} | {'Precision':<10} | {'Recall':<10} | {'F1-score':<10}")
print("-" * 50)

methods = [
    ("RGB", skin_mask_rgb),
    ("HSV", skin_mask_hsv),
    ("LAB", skin_mask_lab),
]

for name, func in methods:
    mask = func(img)
    p, r, f1 = evaluate(mask, gt_mask)
    results[name] = (p, r, f1)
    print(f"{name:<12} | {p:<10.3f} | {r:<10.3f} | {f1:<10.3f}")
print("="*50)
