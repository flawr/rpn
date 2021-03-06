#!/usr/bin/env python

# //******************************************************************************
# //
# //  rpn.py
# //
# //  RPN command-line calculator, setup script
# //  copyright (c) 2016, Rick Gutleber (rickg@his.com)
# //
# //  License: GNU GPL 3.0 (see <http://www.gnu.org/licenses/gpl.html> for more
# //  information).
# //
# //******************************************************************************

requirements = 'requirements.txt'
rpndata = 'rpndata'

import os

from setuptools import setup, find_packages
from rpnVersion import PROGRAM_VERSION_NAME

import rpnGlobals as g

def read( *paths ):
    """Build a file path from *paths* and return the contents."""
    with open( os.path.join( *paths ), 'r') as f:
        return f.read( )

setup(
    name = 'rpn',
    version = PROGRAM_VERSION_NAME,
    description = 'command-line RPN calculator with arbitrary precision',
    long_description =
'''
rpn is a command-line Reverse-Polish Notation calculator that was first
written in C in 1988 as a four-function calculator.  It was rewritten in
Python 3 in 2012 and now uses the mpmath library.  It was a Python learning
exercise for me, and a fun little toy, but when I found mpmath, it became
really cool and powerful, so props to Fredrik Johansson, who did all the
heavy lifting (http://mpmath.org).
''',

    url = 'http://github.com/ConceptJunkie/rpn/',
    license = 'GPL3',
    author = 'Rick Gutleber',
    author_email = 'rickg@his.com',
    py_modules = [ 'rpn',
                   'rpnAliases',
                   'rpnAstronomy',
                   'rpnBase',
                   'rpnCalendar',
                   'rpnCombinatorics',
                   'rpnComputer',
                   'rpnConstants',
                   'rpnConstantUtils',
                   'rpnDateTime',
                   'rpnDeclarations',
                   'rpnEstimates',
                   'rpnFactor',
                   'rpnGenerator',
                   'rpnGeometry',
                   'rpnGlobals',
                   'rpnInput',
                   'rpnLexicographic',
                   'rpnList',
                   'rpnLocation',
                   'rpnMath',
                   'rpnMeasurement',
                   'rpnModifiers',
                   'rpnName',
                   'rpnNumberTheory',
                   'rpnOperators',
                   'rpnOutput',
                   'rpnPersistence',
                   'rpnPhysics',
                   'rpnPolynomials',
                   'rpnPolytope',
                   'rpnPrimes',
                   'rpnPrimeUtils',
                   'rpnSettings',
                   'rpnTestUtils',
                   'rpnUnitClasses',
                   'rpnUnits',
                   'rpnUtils',
                   'rpnVersion',
                   'pyecm',
                   'makeHelp',
                   'makeUnits',
                   'preparePrimeData',
                   'testRPN',
                   'testConvert',
                   'testHelp' ],
    install_requires = open( requirements ).read( ).splitlines( ),

    include_package_data = True,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Environment :: Console',
    ],

    data_files = [ ( rpndata, [ g.dataDir + os.sep + 'balanced_primes.txt',
                                g.dataDir + os.sep + 'cousin_primes.txt',
                                g.dataDir + os.sep + 'double_balanced_primes.txt',
                                g.dataDir + os.sep + 'huge_primes.txt',
                                g.dataDir + os.sep + 'isolated_primes.txt',
                                g.dataDir + os.sep + 'large_primes.txt',
                                g.dataDir + os.sep + 'quad_primes.txt',
                                g.dataDir + os.sep + 'quint_primes.txt',
                                g.dataDir + os.sep + 'sext_primes.txt',
                                g.dataDir + os.sep + 'sexy_primes.txt',
                                g.dataDir + os.sep + 'sexy_quadruplets.txt',
                                g.dataDir + os.sep + 'sexy_triplets.txt',
                                g.dataDir + os.sep + 'small_primes.txt',
                                g.dataDir + os.sep + 'sophie_primes.txt',
                                g.dataDir + os.sep + 'super_primes.txt',
                                g.dataDir + os.sep + 'triple_balanced_primes.txt',
                                g.dataDir + os.sep + 'triplet_primes.txt',
                                g.dataDir + os.sep + 'twin_primes.txt' ] ) ],
    packages = find_packages( exclude = [ 'setup_*' ] ),
    package_dir = { 'rpn' : '' }
)

