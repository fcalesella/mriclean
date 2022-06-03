# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 15:16:32 2022

@author:Federico Calesella
        PhD Student in Cognitive Neuroscience

        Psychiatry and Clinical Psychobiology Unit 
        Division of Neuroscience
        IRCCS San Raffaele Scientific Institute
        Via Stamira d'Ancona 20, 20127, Milano, Italy
        E-mail: f.calesella@studenti.unisr.it
"""

from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()
    
setup(name='mriclean',
version='0.0.2',
description='Confounder removal for neuroimaging data',
long_description=readme(),
long_description_content_type='text/markdown',
url='https://github.com/fcalesella/mriclean',
author='Federico Calesella',
author_email='f.calesella@studenti.unisr.it',
license='GNU General Public License v3.0',
packages=['mriclean'],
install_requires=['numpy', 'nibabel', 'scipy', 'tqdm'])