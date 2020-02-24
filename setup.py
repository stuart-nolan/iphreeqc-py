import setuptools
import iphreeqc

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    author="Stuart Nolan",
    author_email="61199416+stuart-nolan@users.noreply.github.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
    description="python 3+ ctypes wrapper for selected function prototypes defined by IPhreeqc version 3 in IPhreeqc.h and Var.h",
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="iphreeqc-py", 
    packages=setuptools.find_packages(),
    py_modules = ['iphreeqc'],
    url="https://github.com/stuart-nolan/iphreeqc-py.git",
    version=iphreeqc.__version__,
    zip_safe = False
)
