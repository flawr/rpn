#!/usr/bin/env python

# //******************************************************************************
# //
# //  rpnNumberTheory.py
# //
# //  RPN command-line calculator number theory operators
# //  copyright (c) 2014 (1988), Rick Gutleber (rickg@his.com)
# //
# //  License: GNU GPL 3.0 (see <http://www.gnu.org/licenses/gpl.html> for more
# //  information).
# //
# //******************************************************************************

import bz2
import contextlib
import itertools
import os
import pickle
import random

from fractions import Fraction
from functools import reduce
from mpmath import *

from rpnDeclarations import *


# //******************************************************************************
# //
# //  getNthAlternatingFactorial
# //
# //******************************************************************************

def getNthAlternatingFactorial( n ):
    result = 0

    negative = False

    for i in arange( n, 0, -1 ):
        if negative:
            result = fadd( result, fneg( fac( i ) ) )
            negative = False
        else:
            result = fadd( result, fac( i ) )
            negative = True

    return result


# //******************************************************************************
# //
# //  getNthPascalLine
# //
# //******************************************************************************

def getNthPascalLine( n ):
    result = [ ]

    for i in arange( 0, n ):
        result.append( binomial( n - 1, i ) )

    return result


# //******************************************************************************
# //
# //  getDivisorCount
# //
# //******************************************************************************

def getDivisorCount( n ):
    if n == 1:
        return 1

    return fprod( [ i[ 1 ] + 1 for i in factor( n ) ] )


# //******************************************************************************
# //
# //  createDivisorList
# //
# //******************************************************************************

def createDivisorList( seed, factors ):
    result = [ ]

    factor, count = factors[ 0 ]

    for i in range( count + 1 ):
        divisor = [ ]
        divisor.extend( seed )
        divisor.extend( [ factor ] * i )

        if len( factors ) > 1:
            result.extend( createDivisorList( divisor, factors[ 1 : ] ) )
        else:
            result.extend( [ fprod( divisor ) ] )

    return result


# //******************************************************************************
# //
# //  getDivisors
# //
# //******************************************************************************

def getDivisors( n ):
    if n == 0:
        return [ 0 ]
    elif n == 1:
        return [ 1 ]

    return sorted( createDivisorList( [ ], factor( n ) ) )


# //******************************************************************************
# //
# //  loadFactorCache
# //
# //******************************************************************************

def loadFactorCache( ):
    try:
        with contextlib.closing( bz2.BZ2File( g.dataPath + os.sep + 'factors.pckl.bz2', 'rb' ) ) as pickleFile:
            factorCache = pickle.load( pickleFile )
    except FileNotFoundError:
        factorCache = { }

    return factorCache


# //******************************************************************************
# //
# //  saveFactorCache
# //
# //******************************************************************************

def saveFactorCache( factorCache ):
    with contextlib.closing( bz2.BZ2File( g.dataPath + os.sep + 'factors.pckl.bz2', 'wb' ) ) as pickleFile:
        pickle.dump( factorCache, pickleFile )


# //******************************************************************************
# //
# //  factor
# //
# //  This is not my code, and I need to find the source so I can attribute it.
# //  I think I got it from stackoverflow.com.
# //
# //  It factors by pure brute force and is pretty fast considering, but
# //  compared to the advanced algorithms, it's unusably slow.
# //
# //  I don't know how useful the caching is, but here's a use case:  Running
# //  'aliquot' over and over with successively larger iteration values
# //  (argument k).
# //
# //******************************************************************************

def factor( target ):
    n = target

    if n < -1:
        return [ ( -1, 1 ) ] + factor( fneg( n ) )
    elif n == -1:
        return [ ( -1, 1 ) ]
    elif n == 0:
        return [ ( 0, 1 ) ]
    elif n == 1:
        return [ ( 1, 1 ) ]
    else:
        if target > 10000:
            if g.factorCache is None:
                g.factorCache = loadFactorCache( )

                #for i in g.factorCache:
                #    print( i, g.factorCache[ i ] )

            if target in g.factorCache:
                return g.factorCache[ target ]

        def getPotentialPrimes( ):
            basePrimes = ( 2, 3, 5 )

            for basePrime in basePrimes:
                yield basePrime

            basePrimes = ( 7, 11, 13, 17, 19, 23, 29, 31 )

            primeGroup = 0

            while True:
                for basePrime in basePrimes:
                    yield primeGroup + basePrime

                primeGroup += 30

        factors = [ ]
        sqrtn = sqrt( n )

        cacheHit = False

        for divisor in getPotentialPrimes( ):
            if divisor > sqrtn:
                break

            exponent = 0

            while ( fmod( n, divisor ) ) == 0:
                n = floor( fdiv( n, divisor ) )

                if g.factorCache and n in g.factorCache:
                    factors.extend( g.factorCache[ n ] )
                    cacheHit = True
                    n = 1

                exponent += 1

            if exponent > 0:
                factors.append( ( divisor, exponent ) )
                sqrtn = sqrt( n )

            if cacheHit:
                break


        if n > 1:
            factors.append( ( int( n ), 1 ) )

        if g.factorCache:
            largeFactors = [ ( i[ 0 ], i[ 1 ] ) for i in factors if i[ 0 ] > 10000 ]
            product = fprod( [ power( i[ 0 ], i[ 1 ] ) for i in largeFactors ] )

            if product not in g.factorCache:
                g.factorCache[ product ] = largeFactors
                saveFactorCache( g.factorCache )

        return factors


# //******************************************************************************
# //
# //  getExpandedFactorList
# //
# //******************************************************************************

def getExpandedFactorList( factors ):
    factors = map( lambda x: [ x[ 0 ] ] * x[ 1 ], factors )
    return sorted( reduce( lambda x, y: x + y, factors, [ ] ) )


# //******************************************************************************
# //
# //  getNthLucasNumber
# //
# //******************************************************************************

def getNthLucasNumber( n ):
    if n == 1:
        return 1
    else:
        return floor( fadd( power( phi, n ), 0.5 ) )


# //******************************************************************************
# //
# //  getNthJacobsthalNumber
# //
# //  From: http://oeis.org/A001045
# //
# //  a( n ) = ceiling( 2 ^ ( n + 1 ) / 3 ) - ceiling( 2 ^ n / 3 )
# //
# //******************************************************************************

def getNthJacobsthalNumber( n ):
    return getNthLinearRecurrence( [ 2, 1 ], [ 0, 1 ], n )


# //******************************************************************************
# //
# //  getNthBaseKRepunit
# //
# //******************************************************************************

def getNthBaseKRepunit( n, k ):
    return getNthLinearRecurrence( [ fneg( k ), fadd( k, 1 ) ], [ 1, fadd( k, 1 ) ], n )


# //******************************************************************************
# //
# //  getPrimePi
# //
# //******************************************************************************

def getPrimePi( n ):
    result = primepi2( n )

    return [ mpf( result.a ), mpf( result.b ) ]


# //******************************************************************************
# //
# //  getNthTribonacci
# //
# //******************************************************************************

def getNthTribonacci( n ):
    roots = polyroots( [ 1, -1, -1, -1  ] )
    roots2 = polyroots( [ 44, 0, -2, -1 ] )

    result = 0

    for i in range( 0, 3 ):
        result += fmul( roots2[ i ], power( roots[ i ], n ) )

    return floor( fadd( re( result ), fdiv( 1, 2 ) ) )


# //******************************************************************************
# //
# //  getNthTetranacci
# //
# //  http://mathworld.wolfram.com/TetranacciNumber.html
# //
# //******************************************************************************

def getNthTetranacci( n ):
    roots = polyroots( [ 1, -1, -1, -1, -1 ] )
    roots2 = polyroots( [ 563, 0, -20, -5, -1 ] )

    result = 0

    for i in range( 0, 4 ):
        result += fmul( roots2[ i ], power( roots[ i ], n ) )

    return floor( fadd( re( result ), fdiv( 1, 2 ) ) )


# //******************************************************************************
# //
# //  getNthPentanacci
# //
# //******************************************************************************

def getNthPentanacci( n ):
    roots = polyroots( [ 1, -1, -1, -1, -1, -1 ] )

    result = 0

    for i in range( 0, 5 ):
        result += fdiv( power( roots[ i ], n ), polyval( [ -1, 0, 1, 8, -1 ], roots[ i ] ) )

    return floor( fadd( re( result ), fdiv( 1, 2 ) ) )


# //******************************************************************************
# //
# //  getNthHexanacci
# //
# //******************************************************************************

def getNthHexanacci( n ):
    roots = polyroots( [ 1, -1, -1, -1, -1, -1, -1 ] )

    result = 0

    for i in range( 0, 6 ):
        result += fdiv( power( roots[ i ], n ), polyval( [ -1, 0, 1, 2, 10, -1 ], roots[ i ] ) )

    return floor( fadd( re( result ), fdiv( 1, 2 ) ) )


# //******************************************************************************
# //
# //  getNthHeptanacci
# //
# //******************************************************************************

def getNthHeptanacci( n ):
    roots = polyroots( [ 1, -1, -1, -1, -1, -1, -1, -1 ] )

    result = 0

    for i in range( 0, 7 ):
        result += fdiv( power( roots[ i ], n ), polyval( [ -1, 0, 1, 2, 3, 12, -1 ], roots[ i ] ) )

    return floor( fadd( re( result ), fdiv( 1, 2 ) ) )


# //******************************************************************************
# //
# //  getNthPadovanNumber
# //
# //  Padovan sequence: a(n) = a(n-2) + a(n-3) with a(0)=1, a(1)=a(2)=0.
# //
# //  http://oeis.org/A000931
# //
# //  a(n) = (r^n)/(2r+3) + (s^n)/(2s+3) + (t^n)/(2t+3) where r, s, t are the
# //  three roots of x^3-x-1
# //
# //  http://www.wolframalpha.com/input/?i=solve+x^3-x-1
# //
# //  Unfortunately, the roots are scary-complicated, but it's a non-iterative
# //  formula, so I'll use it.
# //
# //  Wikipedia leaves off the first 4 terms, but Sloane's includes them.
# //  Wikipedia cites Ian Stewart and Mathworld, and I'll use their definition.
# //
# //******************************************************************************

def getNthPadovanNumber( arg ):
    n = fadd( arg, 4 )

    a = root( fsub( fdiv( 27, 2 ), fdiv( fmul( 3, sqrt( 69 ) ), 2 ) ), 3 )
    b = root( fdiv( fadd( 9, sqrt( 69 ) ), 2 ), 3 )
    c = fadd( 1, fmul( mpc( 0, 1 ), sqrt( 3 ) ) )
    d = fsub( 1, fmul( mpc( 0, 1 ), sqrt( 3 ) ) )
    e = power( 3, fdiv( 2, 3 ) )

    r = fadd( fdiv( a, 3 ), fdiv( b, e ) )
    s = fsub( fmul( fdiv( d, -6 ), a ), fdiv( fmul( c, b ), fmul( 2, e ) ) )
    t = fsub( fmul( fdiv( c, -6 ), a ), fdiv( fmul( d, b ), fmul( 2, e ) ) )

    return round( re( fsum( [ fdiv( power( r, n ), fadd( fmul( 2, r ), 3 ) ),
                              fdiv( power( s, n ), fadd( fmul( 2, s ), 3 ) ),
                              fdiv( power( t, n ), fadd( fmul( 2, t ), 3 ) ) ] ) ) )


# //******************************************************************************
# //
# //  convertFromContinuedFraction
# //
# //******************************************************************************

def convertFromContinuedFraction( n ):
    if not isinstance( n, list ):
        n = [ n ]

    if ( len( n ) == 1 ) and ( n[ 0 ] == 0 ):
        raise ValueError( "invalid input for evaluating a continued fraction" )

    fraction = ContinuedFraction( n ).getFraction( )
    return fdiv( fraction.numerator, fraction.denominator )


# //******************************************************************************
# //
# //  interpretAsFraction
# //
# //******************************************************************************

def interpretAsFraction( i, j ):
    fraction = ContinuedFraction( i, maxterms=j ).getFraction( )
    return [ fraction.numerator, fraction.denominator ]


# //******************************************************************************
# //
# //  interpretAsBase
# //
# //  This is a list operator so if the integer argument (base) is also a list,
# //  we need to handle that explicitly here.
# //
# //******************************************************************************

def interpretAsBase( args, base ):
    if isinstance( args, list ):
        if isinstance( args[ 0 ], list ):
            return [ interpretAsBase( i, base ) for i in args ]
        else:
            args.reverse( )
    else:
        args = [ args ]

    if isinstance( base, list ):
        return [ interpretAsBase( args, i ) for i in base ]

    value = mpmathify( 0 )
    multiplier = mpmathify( 1 )

    for i in args:
        value = fadd( value, fmul( i, multiplier ) )
        multiplier = fmul( multiplier, base )

    return value


# //******************************************************************************
# //
# //  getGreedyEgyptianFraction
# //
# //******************************************************************************

def getGreedyEgyptianFraction( n, d ):
    if n > d:
        raise ValueError( "'egypt' requires the numerator to be smaller than the denominator" )

    # Create a list to store the Egyptian fraction representation.
    result = [ ]

    rational = Fraction( int( n ), int( d ) )

    # Now, iteratively subtract out the largest unit fraction that may be
    # subtracted out until we arrive at a unit fraction.
    while True:
        # If the rational number has numerator 1, we're done.
        if rational.numerator == 1:
            result.append( rational )
            return result

        # Otherwise, find the largest unit fraction less than the current rational number.
        # This is given by the ceiling of the denominator divided by the numerator.
        unitFraction = Fraction( 1, rational.denominator // rational.numerator + 1 )

        result.append( unitFraction )

        # Subtract out this unit fraction.
        rational = rational - unitFraction

    return result


# //******************************************************************************
# //
# //  getNthLinearRecurrence
# //
# //  nth element of Fibonacci sequence = rpn [ 1 1 ] 1 n linear
# //  nth element of Lucas sequence = rpn [ 1 1 ] [ 1 3 ] n linear
# //
# //******************************************************************************

def getNthLinearRecurrence( recurrence, seeds, n ):
    if not isinstance( recurrence, list ):
        return getNthLinearRecurrence( [ recurrence ], seeds, n )

    if not isinstance( seeds, list ):
        return getNthLinearRecurrence( recurrence, [ seeds ], n )

    if len( seeds ) == 0:
        raise ValueError( 'for operator \'linearrecur\', seeds list cannot be empty ' )

    # calculate missing seeds
    for i in range( len( seeds ), len( recurrence ) ):
        seeds.append( getNthLinearRecurrence( recurrence[ : i ], seeds, i ) )

    if isinstance( n, list ):
        return [ getNthLinearRecurrence( recurrence, seeds, i ) for i in n ]

    if n < len( seeds ):
        return seeds[ int( n ) - 1 ]
    else:
        if len( recurrence ) == 0:
            raise ValueError( 'internal error:  for operator \'linearrecur\', '
                              'recurrence list cannot be empty ' )

        result = [ ]
        result.extend( seeds )

        for i in arange( len( seeds ), n ):
            newValue = 0

            for j in range( -1, -( len( seeds ) + 1 ), -1 ):
                newValue = fadd( newValue, fmul( result[ j ], recurrence[ j ] ) )

            result.append( newValue )
            del result[ 0 ]

        return result[ -1 ]


# //******************************************************************************
# //
# //  makePythagoreanTriple
# //
# //  Euclid's formula
# //
# //  http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Pythag/pythag.html#mnformula
# //
# //******************************************************************************

def makePythagoreanTriple( a, b ):
    if a < 0 or b < 0:
        raise ValueError( "'makepyth3' requires positive arguments" )

    if a == b:
        raise ValueError( "'makepyth3' requires unequal arguments" )

    result = [ ]

    result.append( fprod( [ 2, a, b ] ) )
    result.append( fabs( fsub( fmul( a, a ), fmul( b, b ) ) ) )
    result.append( fadd( fmul( a, a ), fmul( b, b ) ) )

    return sorted( result )


# //******************************************************************************
# //
# //  makePythagoreanQuadruple
# //
# //  From https://en.wikipedia.org/wiki/Pythagorean_quadruple:
# //
# //  All Pythagorean quadruples (including non-primitives, and with repetition,
# //  though a, b and c do not appear in all possible orders) can be generated
# //  from two positive integers a and b as follows:
# //
# //  If a and b have different parity, let p be any factor of a^2 + b^2 such that
# //  p^2 < a^2 + b^2.  Then c = (a^2 + b^2 - p^2)/(2p) and d =
# //  (a^2 + b^2 + p^2)/(2p).  Note that p = {d - c}.
# //
# //  A similar method exists for a, b both even, with the further restriction
# //  that 2p must be an even factor of a^2 + b^2. No such method exists if both
# //  a and b are odd.
# //
# //******************************************************************************

def makePythagoreanQuadruple( a, b ):
    if a < 0 or b < 0:
        raise ValueError( "'makepyth4' requires positive arguments" )

    #if a == b:
    #    raise ValueError( "'makepyth4' requires unequal arguments" )

    odd1 = ( fmod( a, 2 ) == 1 )
    odd2 = ( fmod( b, 2 ) == 1 )

    if odd1 and odd2:
        raise ValueError( "'makepyth4' arguments cannot both be odd" )

    result = [ a, b ]

    sumsqr = fadd( fmul( a, a ), fmul( b, b ) )

    div = getDivisors( sumsqr )

    if odd1 != odd2:
        if len( div ) <= 3:
            p = 1
        else:
            p = random.choice( div[ : ( len( div ) - 1 ) // 2 ] )
    else:
        if ( fmod( sumsqr, 2 ) == 1 ):
            raise ValueError( "'makepyth4' oops, can't make one!" )
        else:
            div = [ i for i in div[ : ( len( div ) - 1 ) // 2 ] if fmod( sumsqr, fmul( i, 2 ) ) == 0 and fmod( i, 2 ) == 0 ]
            p = random.choice( div )

    psqr = fmul( p, p )
    result.append( fdiv( fsub( sumsqr, psqr ), fmul( p, 2 ) ) )
    result.append( fdiv( fadd( sumsqr, psqr ), fmul( p, 2 ) ) )

    return sorted( result )


# //******************************************************************************
# //
# //  makeEulerBrick
# //
# //  http://mathworld.wolfram.com/EulerBrick.html
# //
# //  Saunderson's solution lets (a^',b^',c^') be a Pythagorean triple, then
# //  ( a, b, c ) = ( a'( 4b'^2 - c'^2 ), ( b'( 4a'^2 ) - c'^2 ), 4a'b'c' )
# //
# //******************************************************************************

def makeEulerBrick( _a, _b, _c ):
    a, b, c = sorted( [ _a, _b, _c ] )

    if fadd( power( a, 2 ), power( b, 2 ) ) != power( c, 2 ):
        raise ValueError( "'eulerbrick' requires a pythogorean triple" )

    result = [ ]

    a2 = fmul( a, a )
    b2 = fmul( b, b )
    c2 = fmul( c, c )

    result.append( fabs( fmul( a, fsub( fmul( 4, b2 ), c2 ) ) ) )
    result.append( fabs( fmul( b, fsub( fmul( 4, a2 ), c2 ) ) ) )
    result.append( fprod( [ 4, a, b, c ] ) )

    return sorted( result )


# //******************************************************************************
# //
# //  getNthFibonorial
# //
# //******************************************************************************

def getNthFibonorial( n ):
    result = 1

    for i in arange( 2, n ):
        result = fmul( result, fib( i ) )

    return result


# //******************************************************************************
# //
# //  getGCD
# //
# //  This function is intended to be used with two numerical values or a
# //  single list of values.   The list can be recursive (to support the
# //  'gcd' list operator), but if b is non-zero, then a and b must be single
# //  values.
# //
# //******************************************************************************

def getGCD( a, b = 0 ):
    if b != 0:
        a, b = fabs( a ), fabs( b )

        while a:
            b, a = a, fmod( b, a )

        return b

    if not isinstance( a, list ):
        return a

    if isinstance( a[ 0 ], list ):
        return [ getGCD( arg ) for arg in a ]
    else:
        result = max( a )

        for pair in itertools.combinations( a, 2 ):
            gcd = getGCD( *pair )

            if gcd < result:
                result = gcd

        return result


# //******************************************************************************
# //
# //  getExtendedGCD
# //
# //  adapted from http://ccgi.gladman.plus.com/wp/?page_id=1500
# //
# //******************************************************************************

def getExtendedGCD( a, b ):
    '''
    Euclid's Extended GCD Algorithm

    >>> xgcd(314159265, 271828186)
    (-18013273, 20818432, 7)
    '''
    u, u1 = 1, 0
    v, v1 = 0, 1

    while b != 0:
        q = floor( fdiv( a, b ) )
        r = fmod( a, b )
        a, b = b, r
        u, u1 = u1, fsub( u, fmul( q, u1 ) )
        v, v1 = v1, fsub( v, fmul( q, v1 ) )

    return ( u, v, a ) if a > 0 else ( -u, -v, -a )


# //******************************************************************************
# //
# //  getLCM
# //
# //******************************************************************************

def getLCM( args ):
    if isinstance( args, list ):
        if isinstance( args[ 0 ], list ):
            return [ getLCM( arg ) for arg in args ]
        else:
            result = 1

            for arg in args:
                result = result * arg / getGCD( result, arg )

            return result
    else:
        return args


# //******************************************************************************
# //
# //  getFrobeniusNumber
# //
# //  adapted from http://ccgi.gladman.plus.com/wp/?page_id=1500
# //
# //  Since this is classified as a list operator, it has to behave like the
# //  other operators in rpnList.py.
# //
# //******************************************************************************

def getFrobeniusNumber( args ):
    '''
    http://ccgi.gladman.plus.com/wp/?page_id=1500

    For the integer sequence (a[0], a[1], ...) with a[0] < a[1] < ... < a[n],
    return the largest number, N, that cannot be expressed in the form:
    N = sum(m[i] * x[i]) where all m[i] are non-negative integers.

    >>> frobenius_number((9949, 9967, 9973))
    24812836

    >>> frobenius_number((6, 9, 20))
    43

    >>> frobenius_number((5, 8, 15))
    27

    frobenius_number((5, 8, 9, 12))
    11
    '''

    if isinstance( args, list ):
        if isinstance( args[ 0 ], list ):
            return [ getFrobeniusNumber( arg ) for arg in args ]
        else:
            a = [ ]

            if getGCD( args ) > 1:
                raise ValueError( "the 'frobenius' operator is only valid for lists of values that contain at least one pair of coprime values" )

            for i in sorted( args ):
                a.append( int( i ) )

            def __residue_table( a ):
                n = [ 0 ] + [ None ] * ( a[ 0 ] - 1 )

                for i in range( 1, len( a ) ):
                    d = int( getGCD( a[ 0 ], a[ i ] ) )
                    for r in range( d ):
                        try:
                            nn = min( n[ q ] for q in range( r, a[ 0 ], d ) if n[ q ] is not None )
                        except ValueError:
                            continue

                        if nn is not None:
                            for c in range( a[ 0 ] // d ):
                                nn += a[ i ]
                                p = nn % a[ 0 ]
                                nn = min( nn, n[ p ] ) if n[ p ] is not None else nn
                                n[ p ] = nn
                return [ i for i in n if not i is None ]

            return max( __residue_table( sorted( a ) ) ) - min( a )
    else:
        return 1 if args > 1 else -1




# //******************************************************************************
# //
# //  def _crt(a, b, m, n):
# //
# //  Helper function for calculateChineseRemainderTheorem
# //
# //******************************************************************************

def _crt( a, b, m, n ):
    d = getGCD( m, n )

    if fmod( fsub( a, b ), d ) != 0:
        return None

    x = floor( fdiv( m, d ) )
    y = floor( fdiv( n, d ) )
    z = floor( fdiv( fmul( m, n ), d ) )
    p, q, r = getExtendedGCD( x, y )

    return fmod( fadd( fprod( [ b, p, x ] ), fprod( [ a, q, y ] ) ), z )


# //******************************************************************************
# //
# //  calculateChineseRemainderTheorem
# //
# //  adapted from http://ccgi.gladman.plus.com/wp/?page_id=1500
# //
# //  Since this is classified as a list operator, it has to behave like the
# //  other operators in rpnList.py.
# //
# //******************************************************************************

def calculateChineseRemainderTheorem( values, mods ):
    '''
    The Chinese Remainder Theorem (CRT)

    Solve the equations x = a[i] mod m[i] for x

    >>> crt((2, 3, 5, 7), (97, 101, 103, 107))
    96747802
    '''

    if isinstance( values, list ) != isinstance( mods, list ):
        raise ValueError( "the 'crt' operator requires arguments that are both lists" )

    if not isinstance( values, list ):
        return calculateChineseRemainderTheorem( [ values ], [ mods ] )

    if isinstance( values[ 0 ], list ):
        if isinstance( mods[ 0 ], list ):
            return [ calculateChineseRemainderTheorem( i, j ) for i in values for j in mods ]
        else:
            return [ calculateChineseRemainderTheorem( values, j ) for j in mods ]
    else:
        if isinstance( mods[ 0 ], list ):
            return [ calculateChineseRemainderTheorem( i , mods ) for i in values ]

    if len( values ) != len( mods ):
        raise ValueError( "the 'crt' operator requires arguments that are both lists of the same length" )

    x = values[ 0 ]
    mm = mods[ 0 ]

    for i in range( 1, len( values ) ):
        x = _crt( values[ i ], x, mods[ i ], mm )

        if not x:
            break

        mm = getLCM( [ mods[ i ], mm ] )

    return x


# //******************************************************************************
# //
# //  getSigma
# //
# //  This is the naive implementation.  I believe there's a formula that's
# //  much faster.
# //
# //******************************************************************************

def getSigma( n ):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fsum( getDivisors( n ) )


# //******************************************************************************
# //
# //  getAliquotSequence
# //
# //******************************************************************************

def getAliquotSequence( n, k ):
    result = [ n ]

    a = n

    for i in arange( 0, k - 1 ):
        b = fsub( getSigma( a ), a )
        result.append( b )
        a = b

    return result


# //******************************************************************************
# //
# //  getMobius
# //
# //******************************************************************************

def getMobius( n ):
    if n == 1:
        return 1

    factors = factor( n )

    for i in factors:
        if i[ 1 ] > 1:
            return 0

    if len( factors ) % 2:
        return -1
    else:
        return 1


# //******************************************************************************
# //
# //  getMertens
# //
# //  This function could be cached like the prime numbers.
# //
# //******************************************************************************

def getMertens( n ):
    if n == 1:
        return 1

    result = 0

    for i in arange( 1, n + 1 ):
        result = fadd( result, getMobius( i ) )

    return result


