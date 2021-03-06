import numpy as np
from scipy import misc

# Tests if row in image has at least `threshold` pixels that are not `value`.
def test_row(img, row_number = 0, threshold = 10):
    row = (img[row_number] == 255)
    count = np.count_nonzero(row == False)
    return (count > threshold)

def trim_top(img, threshold = 10):
    for i in range(0, img.shape[0]):
        if test_row(img, i, threshold):
            return img[i:]
    return img

# Identifies continuous of size `min_size` regions of the image where `test_row` is true.
def filled_ranges(img, min_size = 15, threshold = 20):
    ranges = []
    found_row = False
    for i in range(0, img.shape[0]):
        if (found_row == False and test_row(img, i, threshold)):
            found_row = i
        elif (found_row != False and not test_row(img, i, threshold)):
            if i - found_row > min_size:
                ranges.append([found_row, i])
            found_row = False
    return ranges

def remove_top_segment(img, min_size = 15, threshold = 20):
    ranges = filled_ranges(img, min_size, threshold)
    del ranges[0]
    if len(ranges) > 0:
        return img[ranges[0][0]:ranges[-1][1]]
    else:
        return img 

def biggest_diff(ranges):
    sizes = map(lambda range: range[1] - range[0], ranges)
    return ranges[np.argmax(sizes)]

def crop_to_widest(img, min_size = 15, threshold = 20):
    widest = biggest_diff(filled_ranges(img, min_size, threshold))
    return img[widest[0]:widest[1]]

def split_rows(img, ranges):
    return map(lambda range: img[range[0]:range[1]], ranges)

def save_imgs(images, path = "out/"):
    i = 0
    for img in images:
        misc.imsave("%s%04d.jpg" % (path, i), img)
        i += 1

def percent_filled(img):
    if img.size == 0:
        return 0
    return float(np.count_nonzero(img != 255)) / float(img.size)

def expand_range(range, to):
    size = range[1] - range[0]
    dist = (to - size) / 2
    range[1] += dist
    range[0] = range[1] - to
    return range

def grey_top(img, until):
    greyed = img[:until]
    greyed = greyed / 2
    img = img[until:]
    return np.concatenate((greyed, img), axis=0)