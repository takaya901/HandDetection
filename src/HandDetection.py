# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
import ctypes

ESC = 0x1B  # ESCキーの仮想キーコード
def getkey(key):
    return(bool(ctypes.windll.user32.GetAsyncKeyState(key) & 0x8000))

cap = cv2.VideoCapture(0)
# 肌色のHSV閾値
skin_lower = (0, 58, 88)
skin_upper = (25, 173, 229)

while(True):
    ret, input_img = cap.read()

    noise_deleted = cv2.medianBlur(input_img, 7)    #ノイズ除去
    input_hsv = cv2.cvtColor(noise_deleted, cv2.COLOR_BGR2HSV)  # HSVに変換

    # 肌色だけ残して輪郭描画
    skin_mask = cv2.inRange(input_hsv, skin_lower, skin_upper)
    counter_img, contours, hierarchy = cv2.findContours(skin_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    input_masked = cv2.bitwise_and(input_img, input_img, mask=skin_mask)
    result = cv2.drawContours(input_masked, contours, -1, (0,255,0), 3)

    plt.ion()   # 対話モードオン
    result_arr = np.asarray(result) # 画像をarrayに変換
    plt.imshow(result_arr)
    plt.pause(.00001)
    plt.title('result')

    # ESCキーが押されたら終了
    if getkey(ESC):
        break
    # キーが押されたら終了
    if cv2.waitKey(5) >= 0:
        break
cv2.destroyAllWindows()
plt.close()
