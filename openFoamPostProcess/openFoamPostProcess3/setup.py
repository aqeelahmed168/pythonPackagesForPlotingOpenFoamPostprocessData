from setuptools import setup
from distutils.core import setup

setup(name='openFoamPostProcess',
      version='1.0',
      description='manuplating postprocess data from openFoam',
      url='http://github.com/aqeel/openFoamPostProcess',
      author='Aqeel Ahmed',
      author_email='aqeel_168@hotmail.com',
      license='MIT',
      use_2to3 = True,
      use_2to3_exclude_fixers=['lib2to3.fixes.fix_import'],
      packages=['openFoamPostProcess'],
      zip_safe=False)
