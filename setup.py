from setuptools import setup, find_packages, Extension

"""
    Calling
    $python setup.py build_ext --inplace
    will build the extension library in the current file.

    Calling
    $python setup.py build
    will build a file that looks like ./build/lib*, where
    lib* is a file that begins with lib. The library will
    be in this file and end with a C library extension,
    such as .so

    Calling
    $python setup.py install
    will install the module in your site-packages file.

    See the distutils section of
    'Extending and Embedding the Python Interpreter'
    at docs.python.org for more information.
"""

# setup() parameters - https://packaging.python.org/guides/distributing-packages-using-setuptools/
setup(
    name='mykmeanssp',
    version='0.1.0',
    author="Shahar Ziv And Eyal Ben-Hemo",
    author_email="",
    description="A kmeans Algorithem C-API",
    install_requires=['invoke'],
    packages=find_packages(),  # find_packages(where='.', exclude=())
    ext_modules=[
        Extension(
            # the qualified name of the extension module to build
            'mykmeanssp',
            # the files to compile into our module relative to ``setup.py``
            sources = ['kmeans.c'],
        ),
    ]
)