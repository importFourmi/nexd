import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='nexd',  
     version='1.1.1',
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
                        'mtcnn',
                        'mediapipe'              
                      ],
     classifiers=[
         "Programming Language :: Python :: 3",
     ],
)

