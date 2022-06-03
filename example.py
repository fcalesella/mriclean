#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 15:45:52 2022

@author:Federico Calesella
        PhD Student in Cognitive Neuroscience

        Psychiatry and Clinical Psychobiology Unit 
        Division of Neuroscience
        IRCCS San Raffaele Scientific Institute
        Via Stamira d'Ancona 20, 20127, Milano, Italy
        E-mail: f.calesella@studenti.unisr.it
"""

import numpy as np
from mriclean import MRIClean

# define the path to the folder with the images
img_path = 'path/to/images'
# define the path to the file with the confounder. Note that the file must be 
# CSV format with header. Please also make sure that the order of the files and 
# the order of the confounder are the same
confounder_path = 'path/to/file/with/confounder/.csv'
# define the path to the mask
mask_path = 'path/to/mask/.nii/.nii.gz'
# define the path to the output folder
output_path = 'path/to/output/directory'

confounder = np.genfromtxt(confounder_path, delimiter=',', skip_header=1)

mc = MRIClean(img_path, mask=mask_path)
mc.load()
mc.remove_confound(confounder)
mc.save(output_path)