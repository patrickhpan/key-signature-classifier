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

# target = open("out/log.txt", "w")

# target.write("Errors:\n")

for file in range(0, 100):
    my_img = imread('./files/%04d.jpg' % file)
    my_img = crop.remove_top_segment(my_img)

    my_img = np.transpose(my_img)
    # LANDSCAPE #

    my_img = crop.crop_to_widest(my_img, threshold = 400)

    if my_img.shape[0] > 1850:
        print "Likely error: page-%04d.jpg" % file
        # target.write("%d\n" % file)
        continue
         

    clef = my_img[0:70]

    my_img = np.transpose(my_img)
    clef = np.transpose(clef)
    # PORTRAIT #

    i = 0
    clef_ranges = crop.filled_ranges(clef, threshold = 1)
    clef_ranges = map(lambda range: crop.expand_range(range, 176), clef_ranges)

    height = clef.shape[0]
    print "%d height %d last row" % (height, clef_ranges[-1][1])
    if height - 170 > clef_ranges[-1][1]:
        clef_ranges.append([height - 176, height])

    rows = crop.split_rows(my_img, clef_ranges)
    rows = map(lambda row: np.transpose(crop.trim_top(np.transpose(row), 20)), rows) 

    for row in rows:
        end = np.transpose(np.transpose(row)[-300:])
        if crop.percent_filled(end) < 0.05:
            continue
        else:
            # ks = np.transpose(crop.grey_top(np.transpose(row)[0:350], 64))
            ks = np.transpose(np.transpose(row)[0:64])
            misc.imsave("out/%04d-%02d.jpg" % (file, i), ks)
        i += 1

    # misc.imsave("out/page-%04d.jpg" % file, my_img)