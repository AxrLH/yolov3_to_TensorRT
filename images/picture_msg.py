import cv2

img_path = "./eagle.jpg"

img = cv2.imread(img_path)
col, long = img.shape[:2]
print(col, long)

