"""Utility functions for car_license_plate project."""

import logging
import math
from matplotlib import gridspec
import matplotlib.pyplot as plt
import numpy as np
import os
import scipy.misc
import time


def pim(images, titles=None, cmap='gray', interpolation='none'):
        """Plot Image.

        Display one or more images in one row without blocking.

        Input :
            images : list of images as numpy arrays
            titles : list of title strings for each image. Default : None
            cmap : color map for showing image. Default : gray

        Output :
            Plot all images in one row with plt.show(block=False)
        """

        if type(images) != list and type(images) != np.ndarray:
            logging.warning('Input must be list or numpy array')
            return None

        N = len(images)

        cols = len(images)
        rows = int(math.ceil(N / cols))

        if titles is None:
            titles = ['Image'] * N

        gs = gridspec.GridSpec(rows, cols)
        fig = plt.figure(figsize=(14, 8))
        for n in range(N):
            ax = fig.add_subplot(gs[n])
            ax.imshow(images[n], cmap=cmap)
            ax.set_title(titles[n])

        gs.tight_layout(fig)
        plt.show(block=False)


def saveIm(file_name, im):
    """Save image file to local system.

    If file exist rename.
    """
    if os.path.exists(file_name):
        file_name = file_name.split('.')
        extension = file_name[-1]
        file_name = '.'.join(file_name[0:-1])
        file_name = file_name + '_' + str(int(round(time.time() * 1000))) + '.' + extension

    scipy.misc.imsave(file_name, im)
