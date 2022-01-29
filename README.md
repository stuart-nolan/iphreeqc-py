# iphreeqc-py
A python 3+ ctypes wrapper for selected function prototypes defined by
IPhreeqc version 3 in IPhreeqc.h and Var.h.

Version 0.3.1.

See "Change Log" below for recent changes.

This package is tailored to the author's preference but is made available in
the event others find it useful.  

The author is not affiliated with the USGS or the PHREEQC project.  

## Install
#### Option 1

    pip install iphreeqc-py

#### Option 2

    pip install git+https://github.com/stuart-nolan/iphreeqc-py.git@v0.3.1
    
#### Option 3

    git clone -b 'v0.3.1' --single-branch https://github.com/stuart-nolan/iphreeqc-py.git
    cd iphreeqc-py; python setup.py install

This python package intentionally does not install or come with an IPhreeqc
instance.  An IPhreeqc shared library must be built and installed by the user.
An example IPhreeqc install is below.

## Additional Documentation
See IPhreeqc.h and Var.h.

## Example iphreeqc-3.7.3-15968.tar.gz install
Using Ubuntu 20.04.3 LTS with gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0:

    screen # optional, start screen session
    tmpDir=$(mktemp -d)
    cd $tmpDir
    wget https://water.usgs.gov/water-resources/software/PHREEQC/iphreeqc-3.7.3-15968.tar.gz
    tar xvf ./iphreeqc-3.7.3-15968.tar.gz
    cd iphreeqc*/
    # configure options used by the author
    ./configure --libdir=${HOME}/local/lib/iphreeqc-3.7.3-15968 --includedir=${HOME}/local/include/iphreeqc-3.7.3-15968 --docdir=${HOME}/local/share/doc/iphreeqc-3.7.3-15968 CFLAGS="-g -O2 -march=native" CXXFLAGS="-g -O2 -march=native"
    ncp1=$(expr $(cat /proc/cpuinfo | grep processor | wc -l) + 1)
    make -j $ncp1 V=s 2>&1 | tee ipcBuild-$(date +"%Y%m%d-%H%M").log | grep -i '[^_\"a-z-]error[^_.a-z-]'
    make install

#### Example iphreeqc-py tests
Assuming iphreeqc-py is installed and an IPhreeqc shared library has been
configured, built, and installed as described above, try:

    python -c "import iphreeqc; print(iphreeqc.ex1_mod(lib=\"${HOME}/local/lib/iphreeqc-3.7.3-15968/libiphreeqc.so\", database=\"${HOME}/local/share/doc/iphreeqc-3.7.3-15968/database/phreeqc.dat\"))"
    python -c "from test_iphreeqc.test_ex2 import ex2; print(ex2(lib=\"${HOME}/local/lib/iphreeqc-3.7.3-15968/libiphreeqc.so\", database=\"${HOME}/local/share/doc/iphreeqc-3.7.3-15968/database/phreeqc.dat\"))"

#### Clean up

    cd /tmp
    rm -fr $tmpDir
    exit # screen session

#### Notes
For the above examples, IPhreeqc.h and Var.h are in

    ${HOME}/local/include/iphreeqc-3.7.3-15968/

Last tested with iphreeqc-3.7.3-15968 and python 3.10.2 in a virtual environment 
on Ubuntu 20.04.3 LTS, January 2022.

## References & Attribution
    <https://www.usgs.gov/software/phreeqc-version-3>
        Note the files in the examples directory and content used from 
        these files elsewhere in iphreeqc-py are copied from:
    
        <http://water.usgs.gov/water-resources/software/PHREEQC/phreeqc-3.7.3-15968.tar.gz>
    
        and are distributed under the terms of the PHREEQC Public Domain
        declaration (see the "phreeqc-version-3" link above).

    <https://www.phreeqpy.com/>
    PhreeqPy, Python Tools for PHREEQC
    Copyright 2011 Mike Mueller and contributors

    <http://raviapatel.bitbucket.io/IPhreeqcPy>
    IPhreeqcPy, a python wrapper for IPhreeqc
    Copyright 2016 Ravi Patel

This work is derived from IPhreeqcPy.

## License Notice
    iphreeqc-py Copyright (C) 2020 Stuart Nolan

    This program is free software: you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public License
    as published by the Free Software Foundation, version 3.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

#### License Usage Reference
    <https://www.gnu.org/licenses/gpl-howto.html>

## Change Log
Notable changes from 0.2.2:
  - update for iphreeqc-3.7.3-15968 release December 5, 2021
  - revert license notices from LGPL-3.0-or-later to LGPL-3.0-only
  - fix setup.py pypi license classifier
  
See [here](https://github.com/stuart-nolan/iphreeqc-py/commits/master) for
specifics.
