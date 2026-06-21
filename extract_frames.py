import cv2
import os

# 1. 設定影片路徑與輸出資料夾
video_path = "IMG_2640.mov"  # 請確保影片跟程式碼放在同一個資料夾
output_dir = "dataset_images"
os.makedirs(output_dir, exist_ok=True)

cap = cv2.connect = cv2.VideoCapture(video_path)
frame_count = 0
saved_count = 0

print("開始擷取圖片...")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # 每 10 影格擷取一張（避免圖片太重複）
    if frame_count % 10 == 0:
        img_name = f"extinguisher_{saved_count:03d}.jpg"
        img_path = os.path.join(output_dir, img_name)
        cv2.imwrite(img_path, frame)
        saved_count += 1
        
    frame_count += 1

cap.release()
print(f"擷取完成！共儲存了 {saved_count} 張圖片在 '{output_dir}' 資料夾中。")
print("下一步：你可以把這些圖片上傳到 Roboflow 網頁進行滅火器框選標註！")