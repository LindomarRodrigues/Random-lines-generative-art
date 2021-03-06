import math
import random
import time
import numpy as np
import cv2


def linhaAleatoria(img, x, y, passo):
    if random.random() > 0.5:
        cv2.line(img, (x, y), (x+passo, y+passo),
                 (0, 0, 0), 8, lineType=cv2.LINE_AA)
    else:
        cv2.line(img, (x+passo, y), (x, y+passo),
                 (0, 0, 0), 8, lineType=cv2.LINE_AA)


img = np.zeros((2340, 1080, 3), np.uint8)
img[:, :] = (255, 255, 0)

passo = 90

for x in range(0, img.shape[1], passo):
    for y in range(0, img.shape[0], passo):
        linhaAleatoria(img, x, y, passo)
        cv2.imshow("FLOW", cv2.resize(
            img, (img.shape[1]//4, img.shape[0]//4)))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.005)

cv2.destroyAllWindows()
cv2.imwrite("RandomLines.png", img)
