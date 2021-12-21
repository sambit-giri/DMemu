'''
Created on 21 December 2021
@author: Sambit Giri
Setup script
'''

#from setuptools import setup, find_packages
from distutils.core import setup

DMemu_link = 'https://github.com/sambit-giri/DMemu.git'

setup(name='DMemu',
      version='0.0.1',
      description='Emulators for fast modelling of power spectra in various dark matter scenarios.',
      url=DMemu_link,
      author='Sambit Giri',
      author_email='sambit.giri@gmail.com',
      package_dir = {'DMemu' : 'src'},
      packages=['DMemu'],
      package_data={'DMemu': ['input_data/*.pkl']},
      install_requires=['numpy', 'scipy', 'matplotlib', 'astropy',
                        'scikit-learn', 'cython'],
      zip_safe=False
      )