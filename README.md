[![Build Status](https://travis-ci.com/dcs4cop/xcube.svg?branch=master)](https://travis-ci.com/dcs4cop/xcube)


# xcube-gen-rbins

This is a plugin for xcube which can be used for processing inputdata provided by RBINS. 
With xcube-gen-rbins all features of xcube can be used. 
In order to use the xcube-gen-rbins you need to install xcube first: 

# Installation

First install xcube
    
    $ git clone https://github.com/dcs4cop/xcube.git
    $ cd xcube
    $ conda env create
    
Then
    
    $ activate xcube
    $ python setup.py develop

Secondly, clone the xcube-gen-rbins repository:

    $ git clone https://github.com/dcs4cop/xcube-gen-rbins.git
    $ cd xcube-gen-rbins
    $ python setup.py develop
    
Once in a while make an update of xcube and xcube-gen-rbins:
    
    $ activate xcube
    $ git pull --force
    $ cd xcube
    $ python setup.py develop
    
Then change into the xcube-gen-rbins directory:

    $ cd xcube-gen-rbins
    $ python setup.py develop
    
    
Run tests

    $ pytest
    
with coverage

    $ pytest --cov=xcube

with [coverage report](https://pytest-cov.readthedocs.io/en/latest/reporting.html) in HTML

    $ pytest --cov-report html --cov=xcube

# Developer Guide 

...is [here](https://github.com/dcs4cop/xcube/blob/master/docs/DEV-GUIDE.md).


# User Guide

Please use the [README](https://github.com/dcs4cop/xcube/blob/master/README.md) 
of xcube for further information. 
