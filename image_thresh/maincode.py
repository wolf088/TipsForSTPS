import cv2

# 画像の読み込み
img = cv2.imread("input/spray#1_Moment.jpg", 0)

# 閾値の設定
threshold = 25

# 二値化(閾値100を超えた画素を255にする。)
ret, img_thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

# 二値化画像の表示
cv2.imshow("img_th", img_thresh)
cv2.imwrite('t0.3_thrs.jpg', img_thresh)
cv2.waitKey()
cv2.destroyAllWindows()