# MRICleaner
 Confounder removal for neuroimaging data

## Table of Contents
1. [Project Overview](#Project_Overview)
2. [Installation and Data Requirements](#Installation)
3. [Usage](#Usage)
   1. [Initialize the ```MRIClean``` class](#Initialize)
   2. [Load the data](#Load)
   3. [Remove the effect of the confounder](#Clean)
   4. [Save the Results](#Save)
5. [Example](#Example)
7. [References](#References)
8. [Contributors](#Contributors)

## 1. Project Overview <a name="Project_Overview"></a>
The code aims at providing a framework in order to remove the effects of nuisance covariates from voxelwise magnetic resonance imaging (MRI) data. \
The method applyed here is the confound regression (Snoek et al., 2019; Rao et al., 2017), which is based on removing the variance explained by the confounder from the MRI image. More specifically, each voxel is regressed on the confounder, and the coefficient is then used to correct each voxel in turn, by:

<p align="center">
    $X_j corr = X_j - C\beta$,
</p>

where $X_j corr$ is the voxel j corrected, $X_j$ is the uncorrected voxel j, $C$ is the confounder, and $\beta$ is the regression coefficient of $X_j$ on $C$. \
This can be particularly useful if a data correction is needed before the group-analyses .

## 2. Installation and Data Requirements <a name="Installation"></a>
The installation with pip is supported:
```
pip install mricleaner
```

To be run, the code requires some MRI images (in NIfTI format - .nii or .nii.gz - ) and a confounder.

## 3. Usage <a name="Usage"></a>

### i. Initialize the ```MRIClean``` class <a name="Initialize"></a>
The ```MRIClean``` class requires 1 mandatory and 1 optional parameters to be set as input:
```python 
MRIClean(path, mask=None)
``` 
*Parameters*:
- **path**: is a string indicating the full path to the folder where the NIfTI images are stored
- **mask** [optional]: is a string indicating the full path to mask, if any

### ii. Load the data <a name="Load"></a>
The ```load``` method allows to load all the images and arraneg them in a data matrix (subjects x voxels). If the path to a mask was passed to ```MRIClean```, then the matrix will contain only the voxels in the mask.
```python 
load()
``` 

### iii. Remove the effect of the confounder <a name="Clean"></a>
Two methods can be used to estimate the voxelwise habituation parameters: ```reg``` and ```fml```.\
The ```remove_confound``` method remove the effect of the confounder from each voxel.
```python 
remove_confound(confounder)
``` 
*Parameters*:
- **confounder**: a 1-dimensional array with as many values as the number of subjects. This is the variable for which to correct the data. Make sure that the order of the files and the order of the confounder are the same

### iv. Save the Results <a name="Save"></a>
The corrected images can be saved in a specified directory using the ```save``` method.
```python 
save(outdir, fill_nan=False)
``` 
*Parameters*:
- **outdir**: full path of the directory where to save the files
- **fill_nan** [optional]: is boolean parameter. If True then the background will be filled with NaNs, otherwise the background values will be 0

## 4. Example <a name="Example"></a>
An example on how to run the code is provided in the ```example.py``` file (it can also be used as a run-file).

## References <a name="References"></a>
- Snoek, L., Miletić, S., & Scholte, H. S. (2019). How to control for confounds in decoding analyses of neuroimaging data. Neuroimage, 184, 741-760.
- Rao, A., Monteiro, J. M., Mourao-Miranda, J., & Alzheimer's Disease Initiative. (2017). Predictive modelling using neuroimaging data in the presence of confounds. NeuroImage, 150, 23-49.

## Contributors <a name="Contributors"></a>
Federico Calesella \
Camilla Monopoli \
Lidia Fortaner-Uyà
