import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='nexd',
     version='1.3.0',
     scripts=['nexd/main.py'] ,
     author="importFourmi",
     author_email="calvin.galagain@gmail.com",
     description="Ma librairie de fonctions utiles",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/importFourmi/nexd",
     packages=setuptools.find_packages(),
     install_requires=[ 'opencv-python',
                        'matplotlib',
                        'numpy',
                        'scikit-learn',
                      ],
     classifiers=[
         "Programming Language :: Python :: 3",
     ],
)
