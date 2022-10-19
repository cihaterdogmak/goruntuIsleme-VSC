import cv2
import numpy as np
from dizinSettings import getParentFolder

parentFolder = getParentFolder()
resim = parentFolder + "resimler\\kurtResmi.jpg"


kurtResmi = cv2.imread(resim)

cv2.imshow("kurtresmi", kurtResmi)

print(kurtResmi[(230,80)])

cv2.waitKey(0)
cv2.destroyAllWindows()