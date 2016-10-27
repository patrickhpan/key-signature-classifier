from PIL import Image
import imagehash
import glob
import numpy as np
from scipy.cluster.vq import kmeans2

files = glob.glob('out/*')
numfiles = len(files)

imgs = np.zeros((numfiles, 64), dtype=float)

i = 0
for file in files:
    hash = imagehash.average_hash(Image.open(file)).hash
    imgs[i] = np.array(hash).reshape(64)
    i += 1

centroids, labels = kmeans2(imgs, 5)

i=0
for file in files:
    print "%s: %s" % (file, labels[i])
    i += 1