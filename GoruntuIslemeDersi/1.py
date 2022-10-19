import cv2
import numpy as np
from dizinSettings import getParentFolder

parentFolder = getParentFolder()
resim = parentFolder + "resimler//kurtResmi.jpg"

# wolfImage = cv2.imread(resim,0)
wolfImage = cv2.imread(resim)
cv2.imshow("WolfImage", wolfImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
