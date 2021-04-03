from setuptools import setup, find_packages, Extension

"""
    Calling
    $python setup.py build_ext --inplace
    will build the extension library in the current file.

"""

setup(
    name='mykmeanssp',
    version='1.1.0',
    author="Shahar Ziv And Eyal Ben-Hemo",
    description="A kmeans Algorithm C-API",
    install_requires=['invoke', 'numpy'],
    packages=find_packages(),  # find_packages(where='.', exclude=())
    ext_modules=[
        Extension(
            # the qualified name of the extension module to build
            'mykmeanssp',
            # the files to compile into our module relative to ``setup.py``
            sources=['kmeans.c'],
        ),
    ]
)
