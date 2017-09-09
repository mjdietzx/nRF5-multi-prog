"""
Setup script for nrf5_multi_prog.

USAGE:
    python setup.py install
"""

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def read_requirements(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).readlines()

setup(
    name ='nrf5_multi_prog',
    version = '0.0.1',
    description = 'Program multiple nRF5 devices concurrently with this nrfjprog inspired python module/exe',
    long_description=read('README.md'),
    url = 'http://www.nordicsemi.com/',
    author = 'Nordic Semiconductor ASA',
    license = 'BSD',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Embedded Systems',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    keywords = 'nRF5 nRF51 nRF52 nrfjprog pynrfjprog Nordic Semiconductor SEGGER JLink',
    install_requires = read_requirements('requirements.txt'),
    packages = ['nrf5_multi_prog']
)
