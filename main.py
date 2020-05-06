import math
import random
import time
import numpy as np
import cv2


def linhaAleatoria(img, x, y, passo):
    if random.random() > 0.5:
        cv2.line(img, (x, y), (x+passo, y+passo), (0, 0, 0), 10)
    else:
        cv2.line(img, (x+passo, y), (x, y+passo), (0, 0, 0), 10)


img = np.zeros((2340*2, 1080*2, 3), np.uint8)
img[:, :] = (255, 255, 0)

passo = 90*2

for x in range(0, img.shape[1], passo):
    for y in range(0, img.shape[0], passo):
        linhaAleatoria(img, x, y, passo)
        cv2.imshow("teste", cv2.resize(
            img, (img.shape[1]//4, img.shape[0]//4)))
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.005)

cv2.destroyAllWindows()
cv2.imwrite("teste1.png", img)
