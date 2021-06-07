"""Install setup.py for defect_detection."""
from setuptools import setup

REQUIREMENTS = ['numpy', 'matplotlib', 'networkx', 'pydot', 'grave']

setup(name='rg',
      version=0.1,
      description='Research Graph',
      author='Alex Hagen',
      author_email='alexhagen6@gmail.com',
      url='https://github.com/alexhagen/rg',
      long_description=open('README.md').read(),
      packages=['rg'],
      install_requires=REQUIREMENTS,
     )
