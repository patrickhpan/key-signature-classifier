import os
import glob
import numpy as np
from scipy import misc
import crop 

imread = misc.imread
imsave = misc.imsave

files = glob.glob('out/*')
for f in files:
    os.remove(f)

errors = 0

for file in range(0, 10):
    my_img = imread('./files/%04d.jpg' % file)
    my_img = crop.remove_top_segment(my_img)

    my_img = np.transpose(my_img)
    # LANDSCAPE #

    my_img = crop.crop_to_widest(my_img, threshold = 400)

    if my_img.shape[0] > 1850:
        print "Likely error: page-%04d.jpg" % file
        errors += 1

    clef = my_img[0:70]

    my_img = np.transpose(my_img)
    clef = np.transpose(clef)
    # PORTRAIT #

    i = 0
    clef_ranges = crop.filled_ranges(clef, threshold = 1)
    rows = crop.split_rows(my_img, clef_ranges)

    for row in rows:
        end = np.transpose(np.transpose(row)[-200:])
        if crop.percent_filled(np.transpose(row)[-200:]) < 0.02:
            pass
        else:
            ks = np.transpose(np.transpose(row)[0:250])
            misc.imsave("out/%04d-%02d.jpg" % (file, i), ks)
        i += 1

    misc.imsave("out/page-%04d.jpg" % file, my_img)

    print "%d total errors" % errors
