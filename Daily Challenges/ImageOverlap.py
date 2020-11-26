'''
Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?
'''
from scipy.ndimage import convolve
import numpy as np

def largestOverlap(A, B):
    B = np.pad(B, len(A), mode='constant', constant_values=(0, 0))
    return np.amax(convolve(B, np.flip(np.flip(A,1),0), mode='constant'))

'''
Runtime: 204ms - 94.35%
Memory: 37.6MB - 5.31%
'''