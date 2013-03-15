PYGRIB - Python Module for Reading GRIB files version 1.9.6
===========================================================

General Info
------------

Pygris is a Python module for reading and writing GRIB (editions 1 and 2) files.
GRIB is the World Meterological Organization (WMO) standard for distributing gridded data. 
The module is a python interface to the GRIB API C library from the European Centre
for Medium-Range Weather Forecasts (ECMWF).

Installation
-----------

Make sure first that the appropriate configuration scripts
pertaining to your system are defined. You will need the
following scripts to be defined

::

  ${PROTEUS}/externalPackages/versionsConfig/versions.${PROTEUS_ARCH}
  ${PROTEUS}/externalPackages/jasperConfig/configure.${PROTEUS_ARCH}
  ${PROTEUS}/externalPackages/grib_apiConfig/configure.${PROTEUS_ARCH}


For manual installation of PYGRIB you will to install the 
following dependecies first (if you're doing it away from 
a full build of all externalPackages within Proteus)

::

  JASPER
  GRIB_API
  PYPROJ

You do so in externalPackages directory 

::

  cd ${PROTEUS}/externalPackages

and installing each via

::

  make install_jasper
  make install_grib_api
  make install_pyproj

Then finally you can install and test PYGRIB by

::
  make install_pygrib
  make test_pygrib


That should do it!

If you have question, you can contact either:
Matt Malej   ==> matt.malej@erdc.dren.mil
                 or
Tyler Hesser ==> tyler.hesser@erdc.dren.mil