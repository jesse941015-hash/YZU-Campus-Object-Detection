import cv2
from ultralytics import YOLO

# 1. 載入你訓練好的客製化模型權重 (訓練完後 YOLO 會自動生成 best.pt)
# 提示：在還沒訓練前，可以先用 'yolov8n.pt' (官方預訓練模型) 來測試程式能否跑通
model = YOLO("yolov8n.pt")  # 改用官方預訓練的奈米版模型

# 2. 讀取原始影片
input_video = "IMG_2640.mov"
cap = cv2.VideoCapture(input_video)

# 3. 取得影片的長寬、FPS 以便輸出新影片
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# 4. 設定輸出影片路徑 (加上學號符合規範)
output_video = "s1120361_output.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, fps, (frame_width, frame_height))

print("正在處理影片並繪製物件偵測框...")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # 讓 YOLO 模型去辨識這一影格的畫面
    results = model(frame, verbose=False)[0]
    
    # 將偵測到的 Bounding Box 繪製到 frame 上
    annotated_frame = results.plot()
    
    # 寫入新影片
    out.write(annotated_frame)
    
    # 在螢幕上即時顯示 (按 'q' 可以提早退出)
    cv2.imshow("YZU Campus Object Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print(f"處理完畢！帶有偵測框的展示影片已儲存為：{output_video}")