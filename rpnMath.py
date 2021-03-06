#!/usr/bin/env python

# //******************************************************************************
# //
# //  rpnMath.py
# //
# //  RPN command-line calculator, mathematical operators
# //  copyright (c) 2016, Rick Gutleber (rickg@his.com)
# //
# //  License: GNU GPL 3.0 (see <http://www.gnu.org/licenses/gpl.html> for more
# //  information).
# //
# //******************************************************************************

from mpmath import arange, ceil, fadd, fdiv, floor, fmod, fmul, fneg, fsub, \
                   mpf, nint, power, root, sign, sqrt

from rpnDateTime import RPNDateTime
from rpnGenerator import RPNGenerator
from rpnMeasurement import RPNMeasurement, RPNUnits
from rpnName import getOrdinalName
from rpnUtils import real


# //******************************************************************************
# //
# //  add
# //
# //  We used to be able to call fadd directly, but now we want to be able to add
# //  units.  Adding units includes an implicit conversion if the units are not
# //  the same, assuming they are compatible.
# //
# //******************************************************************************

def add( n, k ):
    if isinstance( n, RPNDateTime ) and isinstance( k, RPNMeasurement ):
        return n.add( k )
    elif isinstance( n, RPNMeasurement ) and isinstance( k, RPNDateTime ):
        return k.add( n )
    elif isinstance( n, RPNMeasurement ):
        return n.add( k )
    elif isinstance( k, RPNMeasurement ):
        return RPNMeasurement( n ).add( k )
    else:
        return fadd( n, k )


# //******************************************************************************
# //
# //  subtract
# //
# //  We used to be able to call fsub directly, but now we want to be able to
# //  subtract units and do the appropriate conversions.
# //
# //******************************************************************************

def subtract( n, k ):
    if isinstance( n, RPNDateTime ):
        return n.subtract( k )
    elif isinstance( n, RPNMeasurement ):
        if isinstance( k, RPNDateTime ):
            return k.subtract( n )
        else:
            return n.subtract( k )
    elif isinstance( k, RPNMeasurement ):
        return RPNMeasurement( n ).subtract( k )
    else:
        return fsub( n, k )


# //******************************************************************************
# //
# //  getNegative
# //
# //******************************************************************************

def getNegative( n ):
    if isinstance( n, RPNMeasurement ):
        return RPNMeasurement( fneg( n.getValue( ) ), n.getUnits( ) )
    else:
        return fneg( n )


# //******************************************************************************
# //
# //  getSign
# //
# //******************************************************************************

def getSign( n ):
    if isinstance( n, RPNMeasurement ):
        return sign( n.getValue( ) )
    else:
        return sign( n )


# //******************************************************************************
# //
# //  getValue
# //
# //******************************************************************************

def getValue( n ):
    if isinstance( n, RPNMeasurement ):
        return n.getValue( )
    else:
        return n


# //******************************************************************************
# //
# //  divide
# //
# //  We used to be able to call fdiv directly, but now we want to also divide
# //  the units.  Doing so lets us do all kinds of great stuff because now we
# //  can support compound units without having to explicitly declare them in
# //  makeUnits.py.
# //
# //******************************************************************************

def divide( n, k ):
    if isinstance( n, RPNMeasurement ):
        return n.divide( k )
    elif isinstance( k, RPNMeasurement ):
        return RPNMeasurement( n ).divide( k )
    else:
        return fdiv( n, k )


# //******************************************************************************
# //
# //  multiply
# //
# //  We used to be able to call fmul directly, but now we want to also multiply
# //  the units.  This allows compound units and the conversion routines try to
# //  be smart enough to deal with this.
# //
# //******************************************************************************

def multiply( n, k ):
    if isinstance( n, RPNMeasurement ):
        return n.multiply( k )
    elif isinstance( k, RPNMeasurement ):
        return RPNMeasurement( n ).multiply( k )
    else:
        return fmul( n, k )


# //******************************************************************************
# //
# //  getPower
# //
# //******************************************************************************

def getPower( n, k ):
    if isinstance( n, RPNMeasurement ):
        result = RPNMeasurement( n )
        return result.exponentiate( k )
    else:
        return power( n, k )


# //******************************************************************************
# //
# //  getRoot
# //
# //******************************************************************************

def getRoot( n, k ):
    if isinstance( n, RPNMeasurement ):
        if not isInteger( k ):
            raise ValueError( 'cannot take a fractional root of a measurement' )

        newUnits = RPNUnits( n.getUnits( ) )

        for unit, exponent in newUnits.items( ):
            if fmod( exponent, k ) != 0:
                if k == 2:
                    name = 'square'
                elif k == 3:
                    name = 'cube'
                else:
                    name = getOrdinalName( k )

                raise ValueError( 'cannot take the ' + name + ' root of this measurement: ', n.getUnits( ) ) #print measurement RPNMeasurement.getValue( ) )

            newUnits[ unit ] /= k

        value = root( n.getValue( ), k )

        return RPNMeasurement( value, newUnits )

    return root( n, k )


# //******************************************************************************
# //
# //  takeReciprocal
# //
# //  We used to be able to call fdiv directly, but now we want to handle
# //  RPNMeasurements.
# //
# //******************************************************************************

def takeReciprocal( n ):
    if isinstance( n, RPNMeasurement ):
        return n.invert( )
    else:
        return fdiv( 1, n )


# //******************************************************************************
# //
# //  tetrate
# //
# //  This is the smaller (left-associative) version of the hyper4 operator.
# //
# //  This function forces the second argument to an integer and runs in O( n )
# //  time based on the second argument.
# //
# //******************************************************************************

def tetrate( i, j ):
    result = i

    for x in arange( 1, j ):
        result = power( result, i )

    return result


# //******************************************************************************
# //
# //  tetrateLarge
# //
# //  This is the larger (right-associative) version of the hyper4 operator.
# //
# //  This function forces the second argument to an integer and runs in O( n )
# //  time based on the second argument.
# //
# //******************************************************************************

def tetrateLarge( i, j ):
    result = i

    for x in arange( 1, j ):
        result = power( i, result )

    return result


# //******************************************************************************
# //
# //  isDivisible
# //
# //******************************************************************************

def isDivisible( n, k ):
    return 1 if fmod( real( n ), real( k ) ) == 0 else 0


# //******************************************************************************
# //
# //  isSquare
# //
# //******************************************************************************

def isSquare( n ):
    sqrtN = sqrt( n )

    return 1 if sqrtN == floor( sqrtN ) else 0


# //******************************************************************************
# //
# //  performTrigOperation
# //
# //******************************************************************************

def performTrigOperation( i, operation ):
    if isinstance( i, RPNMeasurement ):
        value = mpf( i.convertValue( RPNMeasurement( 1, { 'radian' : 1 } ) ) )
    else:
        value = i

    return operation( value )


# //******************************************************************************
# //
# //  isEqual
# //
# //******************************************************************************

def isEqual( n, k ):
    if isinstance( n, RPNMeasurement ):
        return 1 if n.isEqual( k ) else 0
    else:
        return 1 if n == k else 0


# //******************************************************************************
# //
# //  isNotEqual
# //
# //******************************************************************************

def isNotEqual( n, k ):
    if isinstance( n, RPNMeasurement ):
        return 1 if n.isNotEqual( k ) else 0
    else:
        return 1 if n != k else 0


# //******************************************************************************
# //
# //  isGreater
# //
# //******************************************************************************

def isGreater( n, k ):
    if isinstance( n, RPNMeasurement ):
        return 1 if n.isLarger( k ) else 0
    else:
        return 1 if real( n ) > real( k ) else 0


# //******************************************************************************
# //
# //  isLess
# //
# //******************************************************************************

def isLess( n, k ):
    if isinstance( n, RPNMeasurement ):
        return 1 if n.isSmaller( k ) else 0
    else:
        return 1 if real( n ) < real( k ) else 0


# //******************************************************************************
# //
# //  isNotGreater
# //
# //******************************************************************************

def isNotGreater( n, k ):
    if isinstance( n, RPNMeasurement ):
        return 1 if n.isNotLarger( k ) else 0
    else:
        return 1 if real( n ) <= real( k ) else 0


# //******************************************************************************
# //
# //  isNotLess
# //
# //******************************************************************************

def isNotLess( n, k ):
    if isinstance( n, RPNMeasurement ):
        return 1 if n.isNotSmaller( k ) else 0
    else:
        return 1 if real( n ) >= real( k ) else 0


# //******************************************************************************
# //
# //  isInteger
# //
# //******************************************************************************

def isInteger( n ):
    return 1 if n == floor( n ) else 0


# //******************************************************************************
# //
# //  roundOff
# //
# //******************************************************************************

def roundOff( n ):
    if isinstance( n, RPNMeasurement ):
        return RPNMeasurement( roundOff( n.getValue( ) ), n.getUnits( ) )
    else:
        return floor( fadd( real( n ), 0.5 ) )


# //******************************************************************************
# //
# //  roundByValue
# //
# //******************************************************************************

def roundByValue( n, value ):
    if isinstance( n, RPNMeasurement ):
        return RPNMeasurement( roundByValue( n.getValue( ), value ), n.getUnits( ) )
    else:
        return fmul( floor( fdiv( fadd( real( n ), fdiv( value, 2 ) ), value ) ), value )


# //******************************************************************************
# //
# //  roundByDigits
# //
# //******************************************************************************

def roundByDigits( n, digits ):
    if isinstance( n, RPNMeasurement ):
        return RPNMeasurement( roundByDigits( n.getValue( ), digits ), n.getUnits( ) )
    else:
        return roundByValue( real( n ), power( 10, digits ) )


# //******************************************************************************
# //
# //  getLarger
# //
# //******************************************************************************

def getLarger( n, k ):
    return n if real( n ) > real( k ) else k


# //******************************************************************************
# //
# //  getSmaller
# //
# //******************************************************************************

def getSmaller( n, k ):
    return n if real( n ) < real( k ) else k


# //******************************************************************************
# //
# //  getFloor
# //
# //******************************************************************************

def getFloor( n ):
    if isinstance( n, RPNMeasurement ):
        return RPNMeasurement( getFloor( n.getValue( ) ), n.getUnits( ) )
    else:
        return floor( n )


# //******************************************************************************
# //
# //  getCeiling
# //
# //******************************************************************************

def getCeiling( n ):
    if isinstance( n, RPNMeasurement ):
        return RPNMeasurement( getCeiling( n.getValue( ) ), n.getUnits( ) )
    else:
        return ceil( n )


# //******************************************************************************
# //
# //  getMaximum
# //
# //******************************************************************************

def getMaximum( n ):
    if isinstance( n[ 0 ], ( list, RPNGenerator ) ):
        return [ max( arg ) for arg in n ]
    else:
        return max( n )


# //******************************************************************************
# //
# //  getMinimum
# //
# //******************************************************************************

def getMinimum( n ):
    if isinstance( n[ 0 ], ( list, RPNGenerator ) ):
        return [ min( arg ) for arg in n ]
    else:
        return min( n )

