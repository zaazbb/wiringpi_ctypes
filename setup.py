from distutils.core import setup
import libzbar
setup(
    name='libwiringpi',
    description='Python ctypes libwiringpi wrapper',
    provides=['wiringpi'],
    requires=[],
    long_description=
    """
    This package is a python ctypes wrapper for the libwiringpi api 
    """,
    version=libzbar.version,
    packages=['libwiringpi'],
    package_dir={'libwiringpi': './libwiringpi'},
    url='https://github.com/zaazbb/wiringpi_ctypes',
    author='zaazbb',
    author_email='zaazbb@163.com',
    platforms='Linux',
    license='GNU Library or Lesser General Public License (LGPL)'
)
