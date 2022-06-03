# -*- coding: utf-8 -*-
"""
Created on Tue May 31 11:43:53 2022

@author:Federico Calesella
        PhD Student in Cognitive Neuroscience

        Psychiatry and Clinical Psychobiology Unit 
        Division of Neuroscience
        IRCCS San Raffaele Scientific Institute
        Via Stamira d'Ancona 20, 20127, Milano, Italy
        E-mail: f.calesella@studenti.unisr.it
"""

import os
import numpy as np
import nibabel as nib
from scipy import stats
from tqdm import tqdm

class MRIClean():
    
    def __init__(self, path, mask=None):
        
        """
        Initialize the class.
        Inputs:
            path: the full path to the folder where the files are stored
            mask [optional]: the full path to the mask
        """
        
        self.path = path
        self.files = [filename for filename in os.listdir(self.path)]
        self.files.sort()
        self.mask_path = mask
         
##############################################################################
         
    def load(self):
         
        """
        Load all the images in the folder and arrange them in a bidimensional
        array (subjects x voxels). Eventually, if a mask was provided, it will
        be applyed to the data.
        """
        
        self.imgs = list()
        self.img_affine = list()
        self.img_shape = list()
        
        for file in self.files:
            img = nib.load(os.path.join(self.path, file))
            self.img_affine.append(img.affine)
            self.img_shape.append(img.shape)
            img_data = img.get_fdata()
            self.imgs.append(np.reshape(img_data, np.prod(img_data.shape)))
            
        self.imgs = np.array(self.imgs)
        if self.mask_path:
            mask = nib.load(self.mask_path).get_fdata()
            self.mask = np.reshape(mask, np.prod(mask.shape))
            self.imgs = self.imgs[:, self.mask!=0]
             
##############################################################################
            
    def remove_confound(self, confounder):
         
        """
        Perform confounder removal. The correction is performed by 
        X_j_corrected = X_j - C*β_j following Snoek, L., Miletić, S., & 
        Scholte, H. S. (2019). How to control for confounds in decoding 
        analyses of neuroimaging data. Neuroimage, 184, 741-760.)
        Inputs:
            confounder: a 1-dimensional array with as many values as the 
            number of subjects. This is the variable for which to correct the
            data
        """
        
        nvox = self.imgs.shape[1]
        self.vox_corr = np.zeros_like(self.imgs)
        wbar = tqdm(total=nvox, leave=False, 
                    desc="Confounder removal progress", position=0)
        
        for voxel in range(nvox):
            sub_vox = self.imgs[:, voxel]
            beta_vox, _, _, _, _ = stats.linregress(confounder, sub_vox)
            self.vox_corr[:, voxel] = sub_vox - (confounder * beta_vox)
            wbar.update()
            
        wbar.close()
    
##############################################################################
                 
    def save(self, outdir, fill_nan=False):
         
        """
        Save the corrected data in nifti format.
        Inputs:
            outdir: full path to the output directory
            fill_nan [optional]: if True then the background will be filled 
            with NaNs, otherwise the background values will be 0
        """
        
        if fill_nan:
            recover = np.empty((len(self.files), self.mask.shape[0]))
            recover[:] = np.nan
        else:
            recover = np.zeros((len(self.files), self.mask.shape[0]))
            
        recover[:, self.mask!=0] = self.vox_corr
        
        for nsub, sub in enumerate(recover):
            sub_img = np.reshape(sub, self.img_shape[nsub])
            sub_nifti = nib.Nifti1Image(sub_img, self.img_affine[nsub])
            outfile = os.path.join(outdir, self.files[nsub])
            nib.save(sub_nifti, outfile)
             
##############################################################################