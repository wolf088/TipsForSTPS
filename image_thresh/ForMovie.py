import cv2
import numpy as np
import csv

def calc_black_whiteArea(bw_image):
    image_size = bw_image.size
    whitePixels = cv2.countNonZero(bw_image)
    whiteRatio = (whitePixels / image_size) * 100
    return whiteRatio


mv = cv2.VideoCapture('input/spray#2.mp4')                                  #動画の読み込み
frame_count = int(mv.get(cv2.CAP_PROP_FRAME_COUNT))                      #動画のフレームをすべて取得
print("総フレーム数:",frame_count)

th_value = 24
f = open('out_'+str(th_value)+'.csv', 'w')
df = []
writer = csv.writer(f)

for i in range(frame_count):
    ch,frame = mv.read()                                                  #１フレームずつ取り出す
    if ch == True:                                                        #取り出せたら、変数chにTrueが入ります
        #frame = cv2.resize(frame,(600,400))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                    #グレイ画像にする
        threshold = cv2.threshold(gray, th_value, 255, cv2.THRESH_BINARY)[1]   #2値化で白黒にする
        cv2.imshow('movie', threshold)                                    #表示
        df.append(calc_black_whiteArea(threshold))

    k = cv2.waitKey(10)       #1ミリ秒間フレームを表示
    if k == 27:               #ESCキーを押したとき終了
        break

writer.writerow(df)
f.close()

mv.release()                #動画を閉じる
cv2.destroyAllWindows()     #ウインドウを閉じる