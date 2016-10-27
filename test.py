import numpy as np
from scipy import misc
import crop 

imread = misc.imread
imsave = misc.imsave

for file in range(0, 507):
    my_img = imread('./files/%04d.jpg' % file)
    my_img = crop.remove_top_segment(my_img)

    my_img = np.transpose(my_img)
    my_img = crop.crop_to_widest(my_img, threshold = 300)
    my_img = np.transpose(my_img)

    if my_img.shape[1] > 1850:
        print "Likely error: %04d.jpg" % file

    misc.imsave("out/%04d.jpg" % file, my_img)
