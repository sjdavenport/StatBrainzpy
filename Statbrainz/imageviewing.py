"""
A Collection of files for Image Viewing 
"""

import ants


def imgload(imname):
    # Eg. im = imgload('MNImask')
    sbmaindir = '/Users/sdavenport/Documents/Code/Python/MyPackages/StatBrainzpy/'
    sbmaindir_images = sbmaindir + 'BrainImages/Volume/'
    if imname.endswith('.gz') or imname.endswith('.nii'):
        try:
            antsimg = ants.image_read(sbmaindir_images + imname)
        except ValueError:
            try:
                antsimg = ants.image_read(imname)
            except ValueError:
                raise ValueError('This file is not available')
    else:
        try:
            antsimg = ants.image_read(sbmaindir_images + imname + '.nii')
        except ValueError:
            try:
                antsimg = ants.image_read(
                    sbmaindir_images + imname + '.nii.gz')
            except ValueError:
                raise ValueError('This file is not available')
    img = antsimg.numpy()
    return img
