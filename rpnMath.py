#!/usr/bin/env python

# //******************************************************************************
# //
# //  rpnMath.py
# //
# //  RPN command-line calculator, mathematical operators
# //  copyright (c) 2015 (1988), Rick Gutleber (rickg@his.com)
# //
# //  License: GNU GPL 3.0 (see <http://www.gnu.org/licenses/gpl.html> for more
# //  information).
# //
# //******************************************************************************

from mpmath import *

from rpnDateTime import RPNDateTime
from rpnMeasurement import RPNMeasurement


# //******************************************************************************
# //
# //  add
# //
# //  We used to be able to call fadd directly, but now we want to be able to add
# //  units.  Adding units includes an implicit conversion if the units are not
# //  the same.
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
# //  exponentiate
# //
# //******************************************************************************

def exponentiate( n, k ):
    if isinstance( n, RPNMeasurement ):
        return n.exponentiate( k )
    elif isinstance( k, RPNMeasurement ):
        raise ValueError( 'a measurement cannot be exponentiated (yet)' )
    else:
        return power( n, k )


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
# //  This function forces the second argument to an integer and runs at O( n )
# //  based on the second argument.
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
# //  This function forces the second argument to an integer and runs at O( n )
# //  based on the second argument.
# //
# //******************************************************************************

def tetrateLarge( i, j ):
    result = i

    for x in arange( 1, j ):
        result = power( i, result )

    return result


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
    return 1 if n == k else 0


# //******************************************************************************
# //
# //  isNotEqual
# //
# //******************************************************************************

def isNotEqual( n, k ):
    return 1 if n != k else 0


# //******************************************************************************
# //
# //  isGreater
# //
# //******************************************************************************

def isGreater( n, k ):
    return 1 if n > k else 0


# //******************************************************************************
# //
# //  isLess
# //
# //******************************************************************************

def isLess( n, k ):
    return 1 if n < k else 0


# //******************************************************************************
# //
# //  isNotGreater
# //
# //******************************************************************************

def isNotGreater( n, k ):
    return 1 if n <= k else 0


# //******************************************************************************
# //
# //  isNotLess
# //
# //******************************************************************************

def isNotLess( n, k ):
    return 1 if n >= k else 0


# //******************************************************************************
# //
# //  isInteger
# //
# //******************************************************************************

def isInteger( n ):
    return 1 if n == floor( n ) else 0


# //******************************************************************************
# //
# //  divides
# //
# //******************************************************************************

def divides( n, k ):
    return isInteger( n / k );


# //******************************************************************************
# //
# //  round
# //
# //******************************************************************************

def round( n, decimals ):
    factor = power( 10, decimals )
    return fdiv( nint( fmul( n, factor ) ), factor )

