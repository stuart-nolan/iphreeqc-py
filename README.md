# iphreeqc-py
A python 3+ ctypes wrapper for selected function prototypes defined by
IPhreeqc version 3 in IPhreeqc.h and Var.h.

Version 0.1a1 is an "alpha" pre-release.  

This is a work in progress and has not been fully tested.  

This package is tailored to the author's preference but is made available in the
event others find it useful.  

The author is not affiliated with the USGS or the Phreeqc project.  

## Install
#### Option 1

    pip install iphreeqc-py

#### Option 2

    pip install git+https://github.com/stuart-nolan/iphreeqc-py.git
    
#### Option 3

    git clone https://github.com/stuart-nolan/iphreeqc-py.git
    cd iphreeqc-py; python setup.py install

This python package intentionally does not install or come with an IPhreeqc
instance.  An IPhreeqc shared library must be built and installed by the user.
An example IPhreeqc install is below.

## Additional Documentation
See IPhreeqc.h and Var.h.

## Example iphreeqc-3.6.2-15100 install
Using Ubuntu 18.04.4 LTS with gcc (Ubuntu 7.4.0-1ubuntu1~18.04.1) 7.4.0:

    screen # optional, start screen session
    tmpDir=$(mktemp -d)
    cd $tmpDir
    wget https://water.usgs.gov/water-resources/software/PHREEQC/iphreeqc-3.6.2-15100.tar.gz
    tar xvf ./iphreeqc-3.6.2-15100.tar.gz
    cd iphreeqc*/
    # configure options used by the author
    ./configure --libdir=${HOME}/local/lib/iphreeqc-3.6.2-15100 --includedir=${HOME}/local/include/iphreeqc-3.6.2-15100 --docdir=${HOME}/local/share/doc/iphreeqc-3.6.2-15100 CFLAGS="-g -O2 -march=native" CXXFLAGS="-g -O2 -march=native"
    ncp1=$(expr $(cat /proc/cpuinfo | grep processor | wc -l) + 1)
    make -j $ncp1 V=s 2>&1 | tee ipcBuild-$(date +"%Y%m%d-%H%M").log | grep -i '[^_-\"a-z]error[^_-.a-z]'
    make install

#### Example iphreeqc.py test
Assuming iphreeqc-py is installed and an IPhreeqc shared library has been
configured, built, and installed as described above, try:

    python -c "import iphreeqc as ipcl; print(ipcl.example1(lib=\"${HOME}/local/lib/iphreeqc-3.6.2-15100/libiphreeqc.so\", database=\"${HOME}/local/share/doc/iphreeqc-3.6.2-15100/database/phreeqc.dat\"))"

#### Clean up

    rm -fr $tmpDir
    exit # screen session

#### Notes
For the above examples, IPhreeqc.h and Var.h are in

    ${HOME}/local/include/iphreeqc-3.6.2-15100/

Last tested with iphreeqc-3.6.2-15100 and python 3.8.1 in a virtual environment 
on Ubuntu 18.04.4 LTS, February 2020.

## References & Attribution
    <https://www.usgs.gov/software/phreeqc-version-3>

    <https://www.phreeqpy.com/>
    PhreeqPy, Python Tools for PHREEQC
    Copyright 2011 Mike Mueller and contributors

    <http://raviapatel.bitbucket.io/IPhreeqcPy>
    IPhreeqcPy, a python wrapper for IPhreeqc
    Copyright 2016 Ravi Patel

This work is derived from IPhreeqcPy.

## License Notice
    iphreeqc-py Copyright (C) 2020 Stuart Nolan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published 
    by the Free Software Foundation, version 3.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

#### License Usage Reference
    <https://www.gnu.org/licenses/gpl-howto.html>
