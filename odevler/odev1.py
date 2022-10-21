import cv2
from dizinSettings import getParentFolder
from dicFonctions import dicCreate , matrisContentsCalc


parentFolder = getParentFolder()
resim = parentFolder + "resimler\\kurtResmi.jpg"

resim = cv2.imread(resim,0)

cv2.imshow("kurtcuk :)", resim)

dic = matrisContentsCalc(resim,dicCreate())

for i in dic:
    print(f" {i} --> {dic[i]} {(dic[i]//8) * '|'}")

cv2.waitKey(0)
cv2.destroyAllWindows()