from skimage import io
from skimage import data, feature, filters , img_as_float
from skimage.morphology import (erosion, dilation, opening, closing, white_tophat)
from scipy import ndimage
from pylab import *
from skimage.morphology import disk

b = np.array([[2,4,5,4,2],[4,9,12,9,4],[5,12,15,12,5],[4,9,12,9,4],[2,4,5,4,2]], np.float32)
b = b / 240
images = ["samolot07.jpg", "samolot10.jpg", "samolot01.jpg", "samolot14.jpg", "samolot08.jpg", "samolot17.jpg"]
img = []
img2 = []
for i in images:
    img.append(img_as_float(io.imread(i, as_gray=True)))

for i in range(len(img)):
    img2.append(ndimage.filters.convolve(img[i],b))

footprint = disk(1)
for i in range(len(img2)):
    img2[i]= feature.canny(img2[i] , sigma=3)


fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(10, 10))

for i in range(2):
    for j in range(3):
        ax[i][j].imshow(img2[(i*3)+j], cmap='gray')

for a in ax[0]:
    a.axis('off')
for a in ax[1]:
    a.axis('off')

fig.tight_layout()
plt.show()