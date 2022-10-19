import cv2
import numpy as np
from dizinSettings import getParentFolder

parentFolder = getParentFolder()

resim = parentFolder + "resimler\\joker.jpg"

jokerResmi = cv2.imread(resim)

jokerResmi[50,30] = [0,0,0]
# for j in range(len(jokerResmi)):
#     for i in range(0,len(jokerResmi[j])):
#         jokerResmi[j,i] = [i%255,j%255,i%255] 


cv2.imshow("Joker", jokerResmi)

cv2.waitKey(0)
cv2.destroyAllWindows()
