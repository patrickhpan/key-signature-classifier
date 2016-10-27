import numpy as np
from scipy import misc

imread = misc.imread
imsave = misc.imsave

def test_row(img, value = 255, row_number = 0, threshold = 10):
    row = (img[row_number] == value)
    return (np.count_nonzero(row == False) > threshold)

def split_rows(img, value = 255):
    ranges = []
    found_row = False
    for i in range(0, img.shape[0]):
        if (found_row == False and test_row(img, value, i)):
            found_row = i
        elif (found_row != False and not test_row(img, value, i)):
            ranges.append([found_row, i])
            found_row = False
    return ranges

def save_split_rows(img, ranges):
    i = 0
    for range in ranges:
        imsave("%03d.jpg" % i, img[range[0]:range[1]])