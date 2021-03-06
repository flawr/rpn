#!/usr/bin/env python

# //******************************************************************************
# //
# //  preparePrimeData.py
# //
# //  RPN command-line calculator prime number data file compiler
# //  copyright (c) 2016, Rick Gutleber (rickg@his.com)
# //
# //  License: GNU GPL 3.0 (see <http://www.gnu.org/licenses/gpl.html> for more
# //  information).
# //
# //******************************************************************************

import six

import bz2
import contextlib
import os
import pickle

import rpnGlobals as g

if not six.PY3:
    g.dataDir = "rpndata2"


# //******************************************************************************
# //
# //  preparePrimeData
# //
# //******************************************************************************

def preparePrimeData( baseName ):
    print( 'processing ' + baseName + '...' )

    inputFileName = g.dataDir + os.sep + baseName + '.txt'

    data = { }

    with open( inputFileName, "rU" ) as input:
        for line in input:
            try:
                key, value = line.split( )
                data[ int( key ) ] = int( value )
            except:
                print( 'parsing error in file ' + inputFileName + ': \'' + line + '\'' )


    pickleFileName = g.dataDir + os.sep + baseName + '.pckl.bz2'

    with contextlib.closing( bz2.BZ2File( pickleFileName, 'wb' ) ) as pickleFile:
        pickle.dump( data, pickleFile )


# //******************************************************************************
# //
# //  __main__
# //
# //******************************************************************************

if __name__ == '__main__':
    preparePrimeData( "balanced_primes" )
    preparePrimeData( "cousin_primes" )
    preparePrimeData( "double_balanced_primes" )
    preparePrimeData( "huge_primes" )
    preparePrimeData( "isolated_primes" )
    preparePrimeData( "large_primes" )
    preparePrimeData( "quad_primes" )
    preparePrimeData( "quint_primes" )
    preparePrimeData( "sext_primes" )
    preparePrimeData( "sexy_primes" )
    preparePrimeData( "sexy_quadruplets" )
    preparePrimeData( "sexy_triplets" )
    preparePrimeData( "small_primes" )
    preparePrimeData( "sophie_primes" )
    preparePrimeData( "super_primes" )
    preparePrimeData( "triplet_primes" )
    preparePrimeData( "triple_balanced_primes" )
    preparePrimeData( "twin_primes" )

