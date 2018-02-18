import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# skin_img = np.zeros((640, 480, 3), np.uint8)
skin_lower = (0, 58, 88)
skin_upper = (25, 173, 229)

while(True):
    ret, input_img = cap.read()
    # skin_img = Scalar(0,0,0)

    frame = cv2.medianBlur(input_img, 7)  #ノイズ除去
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # HSVに変換

    # 肌色でない画素を黒に
    # for y in range(frame.shape[0]):
    #     for x in range(frame.shape[1]):
    #         if frame.item(y,x,0) > 15 and frame.item(y,x,1) < 50:
    #             frame.itemset((y,x,0), 0)
    #             frame.itemset((y,x,1), 0)
    #             frame.itemset((y,x,2), 0)
    #         else:
    #             frame.itemset((y,x,0), input_img.item(y,x,0))
    #             frame.itemset((y,x,1), input_img.item(y,x,1))
    #             frame.itemset((y,x,2), input_img.item(y,x,2))
    skin_img = cv2.inRange(frame, skin_lower, skin_upper)

    # output
    cv2.imshow('cap', skin_img)
    # cv2.imshow('result', skin_img)

    # 何かキーを押したら終了
    if cv2.waitKey(5) >= 0:
        break
cv2.destroyAllWindows()
