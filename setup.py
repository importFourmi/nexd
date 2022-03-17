import setuptools
from pysoft import pylib

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='nexd',  
     version='0.1',
     scripts=['nexd'] ,
     author="importFourmi",
     author_email="calvin.galagain@gmail.com",
     description="Python utility package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/importFourmi/nexd",
     packages=setuptools.find_packages(),
     py_modules=['pylib'],
     install_requires=['pysoft'],
     classifiers=[
         "Programming Language :: Python :: 3",
     ],
 )
