import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='nexd',  
     version='1.0.0',
     scripts=['nexd/main.py'] ,
     author="importFourmi",
     author_email="calvin.galagain@gmail.com",
     description="Python utility package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/importFourmi/nexd",
     packages=setuptools.find_packages(),
     install_requires=[ 'opencv-python',
                        'matplotlib',   
                        'numpy',                  
                      ],
     classifiers=[
         "Programming Language :: Python :: 3",
     ],
)

