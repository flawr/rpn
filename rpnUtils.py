#!/usr/bin/env python

#//******************************************************************************
#//
#//  rpnUtils
#//
#//  RPN command-line calculator utility functions
#//  copyright (c) 2014 (1988), Rick Gutleber (rickg@his.com)
#//
#//  License: GNU GPL 3.0 (see <http://www.gnu.org/licenses/gpl.html> for more
#//  information).
#//
#//******************************************************************************

import arrow
import builtins
import bz2
import contextlib
import math
import os
import pickle
import string
import textwrap

from mpmath import *

from rpnDeclarations import *
from rpnVersion import *

import rpnGlobals as g


#//******************************************************************************
#//
#//  loadUnitConversionMatrix
#//
#//******************************************************************************

def loadUnitConversionMatrix( ):
    try:
        with contextlib.closing( bz2.BZ2File( g.dataPath + os.sep + 'unit_conversions.pckl.bz2', 'rb' ) ) as pickleFile:
            g.unitConversionMatrix = pickle.load( pickleFile )
    except FileNotFoundError:
        print( 'rpn:  Unable to load unit conversion matrix data.  Unit conversion will be unavailable.' )


#//******************************************************************************
#//
#//  removeUnderscores
#//
#//******************************************************************************

def removeUnderscores( source ):
    result = ''

    for c in source:
        if c == '_':
            result += ' '
        else:
            result += c

    return result


#//******************************************************************************
#//
#//  debugPrint
#//
#//******************************************************************************

def debugPrint( *args, **kwargs ):
    if g.debugMode:
        builtins.print( *args, **kwargs )
    else:
        return


#//******************************************************************************
#//
#//  downloadOEISSequence
#//
#//******************************************************************************

def downloadOEISSequence( id ):
    keywords = downloadOEISText( id, 'K' ).split( ',' )

    if 'nonn' in keywords:
        result = downloadOEISText( id, 'S' )
        result += downloadOEISText( id, 'T' )
        result += downloadOEISText( id, 'U' )
    else:
        result = downloadOEISText( id, 'V' )
        result += downloadOEISText( id, 'W' )
        result += downloadOEISText( id, 'X' )

    if 'cons' in keywords:
        offset = int( downloadOEISText( id, 'O' ).split( ',' )[ 0 ] )
        result = ''.join( result.split( ',' ) )
        return mpmathify( result[ : offset ] + '.' + result[ offset : ] )
    else:
        return [ int( i ) for i in result.split( ',' ) ]


#//******************************************************************************
#//
#//  downloadOEISText
#//
#//******************************************************************************

def downloadOEISText( id, char, addCR=False ):
    import urllib.request
    import re as regex

    data = urllib.request.urlopen( 'http://oeis.org/search?q=id%3AA{:06}'.format( id ) + '&fmt=text' ).read( )

    pattern = regex.compile( b'%' + bytes( char, 'ascii' ) + b' A[0-9][0-9][0-9][0-9][0-9][0-9] (.*?)\n', regex.DOTALL )

    lines = pattern.findall( data )

    result = ''

    for line in lines:
        if result != '' and addCR:
            result += '\n'

        result += line.decode( 'ascii' )

    return result


#//******************************************************************************
#//
#//  convertToBase10
#//
#//******************************************************************************

def convertToBase10( integer, mantissa, inputRadix ):
    result = mpmathify( 0 )
    base = mpmathify( 1 )

    validNumerals = g.numerals[ : inputRadix ]

    for i in range( len( integer ) - 1, -1, -1 ):
        digit = validNumerals.find( integer[ i ] )

        if digit == -1:
            raise ValueError( 'invalid numeral \'%c\' for base %d' % ( integer[ i ], inputRadix ) )

        result += digit * base
        base *= inputRadix

    base = fdiv( 1, inputRadix )

    for i in range( 0, len( mantissa ) ):
        digit = validNumerals.find( mantissa[ i ] )

        if digit == -1:
            raise ValueError( 'invalid numeral \'%c\' for base %d' % ( mantissa[ i ], inputRadix ) )

        result += digit * base
        base /= inputRadix

    return result


#//******************************************************************************
#//
#//  parseInputValue
#//
#//  Parse out a time value or a numerical expression and attempt to set the
#//  precision to an appropriate value based on the expression.
#//
#//******************************************************************************

def parseInputValue( term, inputRadix ):
    if isinstance( term, mpf ):
        return term

    innerChars = term[ 1 : -1 ]

    if '/' in innerChars:
        term = term.replace( '/', '-' )
        innerChars = term[ 1 : -1 ]

    if ( '-' in innerChars ) or ( ':' in innerChars ):
        try:
            datetime = arrow.get( term )
        except:
            raise ValueError( 'error parsing datetime' )

        return datetime

    if term == '0':
        return mpmathify( 0 )

    # ignore commas
    term = ''.join( [ i for i in term if i not in ',' ] )

    if term[ 0 ] == '\\':
        term = term[ 1 : ]
        ignoreSpecial = True
    else:
        ignoreSpecial = False

    if '.' in term:
        if inputRadix == 10:
            newPrecision = len( term ) + 1

            if mp.dps < newPrecision:
                mp.dps = newPrecision

            return mpmathify( term )

        decimal = term.find( '.' )
    else:
        decimal = len( term )

    negative = term[ 0 ] == '-'

    if negative:
        start = 1
    else:
        if term[ 0 ] == '+':
            start = 1
        else:
            start = 0

    integer = term[ start : decimal ]
    mantissa = term[ decimal + 1 : ]

    # check for hex, then binary, then octal, otherwise a plain old decimal integer
    if not ignoreSpecial and mantissa == '':
        if integer[ 0 ] == '0':
            if len( integer ) == 1:
                return mpmathify( 0 )

            if integer[ 1 ] in 'Xx':
                # set the precision big enough to handle this value
                newPrecision = math.ceil( ( math.log10( 16 ) * ( len( integer ) - 2 ) ) ) + 1

                if mp.dps < newPrecision:
                    mp.dps = newPrecision

                return mpmathify( int( integer[ 2 : ], 16 ) )
            elif integer[ -1 ] in 'bB':
                # set the precision big enough to handle this value
                newPrecision = math.ceil( math.log10( 2 ) * ( len( integer ) - 1 ) ) + 1

                if mp.dps < newPrecision:
                    mp.dps = newPrecision

                integer = integer[ : -1 ]
                return mpmathify( int( integer, 2 ) * ( -1 if negative else 1 ) )
            else:
                integer = integer[ 1 : ]

                return mpmathify( int( integer, 8 ) )
        if integer[ 0 ] == '1' and integer[ -1 ] in 'bB':
            # set the precision big enough to handle this value
            newPrecision = math.ceil( math.log10( 2 ) * ( len( integer ) - 1 ) ) + 1

            if mp.dps < newPrecision:
                mp.dps = newPrecision

            integer = integer[ : -1 ]
            return mpmathify( int( integer, 2 ) * ( -1 if negative else 1 ) )
        elif inputRadix == 10:
            newPrecision = len( integer ) + 1

            if mp.dps < newPrecision:
                mp.dps = newPrecision

            return fneg( integer ) if negative else mpmathify( integer )

    # finally, we have a non-radix 10 number to parse
    result = convertToBase10( integer, mantissa, inputRadix )
    return fneg( result ) if negative else mpmathify( result )


#//******************************************************************************
#//
#//  convertToBaseN
#//
#//******************************************************************************

def convertToBaseN( value, base, baseAsDigits, numerals ):
    if baseAsDigits:
        if ( base < 2 ):
            raise ValueError( 'base must be greater than 1' )
    else:
        if not ( 2 <= base <= len( numerals ) ):
            raise ValueError( 'base must be from 2 to %d' % len( numerals ) )

    if value == 0:
        return 0

    if value < 0:
        return '-' + convertToBaseN( ( -1 ) * value, base, baseAsDigits, numerals )

    if base == 10:
        return str( value )

    result = ''
    leftDigits = value

    while leftDigits > 0:
        if baseAsDigits:
            if result != '':
                result = ' ' + result

            result = str( int( leftDigits ) % base ) + result
        else:
            result = numerals[ int( leftDigits ) % base ] + result

        leftDigits = floor( fdiv( leftDigits, base ) )

    return result


#//******************************************************************************
#//
#//  convertToPhiBase
#//
#//******************************************************************************

def convertToPhiBase( num ):
    epsilon = power( 10, -( mp.dps - 3 ) )

    output = ''
    integer = ''

    start = True
    previousPlace = 0
    remaining = num

    originalPlace = 0

    while remaining > epsilon:
        place = int( floor( log( remaining, phi ) ) )

        if start:
            output = '1'
            start = False
            originalPlace = place
        else:
            if place < -( originalPlace + 1 ):
                break

            for i in range( previousPlace, place + 1, -1 ):
                output += '0'

                if ( i == 1 ):
                    integer = output
                    output = ''

            output += '1'

            if place == 0:
                integer = output
                output = ''

        previousPlace = place
        remaining -= power( phi, place )

    if integer == '':
        return output, ''
    else:
        return integer, output


#//******************************************************************************
#//
#//  convertToFibBase
#//
#//  Returns a string with Fibonacci encoding for n (n >= 1).
#//
#//  adapted from https://en.wikipedia.org/wiki/Fibonacci_coding
#//
#//******************************************************************************

def convertToFibBase( value ):
    result = ''

    n = value

    if n >= 1:
        a = 1
        b = 1

        c = fadd( a, b )    # next Fibonacci number
        fibs = [ b ]        # list of Fibonacci numbers, starting with F(2), each <= n

        while n >= c:
            fibs.append( c )  # add next Fibonacci number to end of list
            a = b
            b = c
            c = fadd( a, b )

        for fibnum in reversed( fibs ):
            if n >= fibnum:
                n = fsub( n, fibnum )
                result = result + '1'
            else:
                result = result + '0'

    return result


#//******************************************************************************
#//
#//  convertFractionToBaseN
#//
#//******************************************************************************

def convertFractionToBaseN( value, base, precision, baseAsDigits, accuracy ):
    if baseAsDigits:
        if ( base < 2 ):
            raise ValueError( 'base must be greater than 1' )
    else:
        if not ( 2 <= base <= len( g.numerals ) ):
            raise ValueError( 'base must be from 2 to %d' % len( g.numerals ) )

    if value < 0 or value >= 1.0:
        raise ValueError( 'value (%s) must be >= 0 and < 1.0' % value )

    if base == 10:
        return str( value )

    result = ''

    while value > 0 and precision > 0:
        value = value * base
        digit = int( value )

        if len( result ) == accuracy:
            value -= digit
            newDigit = int( value ) % base

            if newDigit >= base // 2:
                digit += 1

        if baseAsDigits:
            if result != '':
                result += ' '

            result += str( digit % base )
        else:
            result += g.numerals[ digit % base ]

        if len( result ) == accuracy:
            break

        value -= digit
        precision -= 1

    return result


#//******************************************************************************
#//
#//  addAliases
#//
#//******************************************************************************

def addAliases( operatorList, operatorAliases ):
    for index, operator in enumerate( operatorList ):
        aliasList = [ key for key in operatorAliases if operator == operatorAliases[ key ] ]

        if operator in g.unitOperators:
            unitInfo = g.unitOperators[ operator ]

            if unitInfo.abbrev != '':
                aliasList.append( unitInfo.abbrev )

            aliasList.extend( unitInfo.aliases )

            aliasList = list( set( aliasList ) )

        if len( aliasList ) > 0:
            operatorList[ index ] += ' (' + ', '.join( sorted( aliasList ) ) + ')'



#//******************************************************************************
#//
#//  validateOptions
#//
#//******************************************************************************

def validateOptions( args ):
    if args.hex:
        if args.output_radix != 10 and args.output_radix != 16:
            return False, '-r and -x can\'t be used together'

        if args.octal:
            return False, '-x and -o can\'t be used together'

    if args.octal:
        if args.output_radix != 10 and args.output_radix != 8:
            return False, '-r and -o can\'t be used together'

    if args.output_radix_numerals > 0:
        if args.hex:
            return False, '-R and -x can\'t be used together'

        if args.octal:
            return False, '-R and -o can\'t be used together'

        if args.output_radix != 10:
            return False, '-R and -r can\'t be used together'

        if args.output_radix_numerals < 2:
            return False, 'output radix must be greater than 1'

    if args.comma and args.integer_grouping > 0 :
        return False, 'rpn:  -c can\'t be used with -i'

    if args.output_radix_numerals > 0 and \
       ( args.comma or args.decimal_grouping > 0 or args.integer_grouping > 0 ):
        return False, '-c, -d and -i can\'t be used with -R'

    return True, ''


#//******************************************************************************
#//
#//  validateArguments
#//
#//******************************************************************************

def validateArguments( terms ):
    bracketCount = 0

    for term in terms:
        if term == '[':
            bracketCount += 1
        elif term == ']':
            bracketCount -= 1

    if bracketCount:
        print( 'rpn:  mismatched brackets (count: {})'.format( bracketCount ) )
        return False

    return True


#//******************************************************************************
#//
#//  evaluateOneListFunction
#//
#//******************************************************************************

def evaluateOneListFunction( func, args ):
    if isinstance( args, list ):
        for arg in args:
            if isinstance( arg, list ) and isinstance( arg[ 0 ], list ):
                return [ evaluateOneListFunction( func, arg ) for arg in args ]

        return func( args )
    else:
        return func( [ args ] )


#//******************************************************************************
#//
#//  evaluateOneArgFunction
#//
#//******************************************************************************

def evaluateOneArgFunction( func, args ):
    if isinstance( args, list ):
        return [ evaluateOneArgFunction( func, i ) for i in args ]
    else:
        return func( args )


#//******************************************************************************
#//
#//  evaluateTwoArgFunction
#//
#//******************************************************************************

def evaluateTwoArgFunction( func, arg1, arg2 ):
    #print( 'arg1: ' + str( arg1 ) )
    #print( 'arg2: ' + str( arg2 ) )

    len1 = len( arg1 )
    len2 = len( arg2 )

    list1 = len1 > 1
    list2 = len2 > 1

    #print( list1 )
    #print( list2 )

    if list1:
        if list2:
            return [ func( arg2[ index ], arg1[ index ] ) for index in range( 0, min( len1, len2 ) ) ]
        else:
            return [ func( arg2[ 0 ], i ) for i in arg1 ]

    else:
        if list2:
            return [ func( j, arg1[ 0 ] ) for j in arg2 ]
        else:
            return [ func( arg2[ 0 ], arg1[ 0 ] ) ]


#//******************************************************************************
#//
#//  callers
#//
#//******************************************************************************

callers = [
    lambda func, args: [ func( ) ],
    evaluateOneArgFunction,
    evaluateTwoArgFunction,
    lambda func, arg1, arg2, arg3:
        [ func( a, b, c ) for c in arg1 for b in arg2 for a in arg3 ],
    lambda func, arg1, arg2, arg3, arg4:
        [ func( a, b, c, d ) for d in arg1 for c in arg2 for b in arg3 for a in arg4 ],
    lambda func, arg1, arg2, arg3, arg4, arg5:
        [ func( a, b, c, d, e ) for e in arg1 for d in arg2 for c in arg3 for b in arg4 for a in arg5 ],
]


#//******************************************************************************
#//
#//  getModifiedOnesName
#//
#//******************************************************************************

def getModifiedOnesName( name, code ):
    if ( 'n' in code ) and ( ( name == 'septe' ) or ( name == 'nove' ) ):
        return name + 'n'
    elif ( 'm' in code ) and ( ( name == 'septe' ) or ( name == 'nove' ) ):
        return name + 'm'
    elif ( 's' in code ) and ( ( name == 'tre' ) or ( name == 'se' ) ):
        return name + 's'
    elif ( 'x' in code ):
        if ( name == 'tre' ):
            return name + 's'
        elif ( name == 'se' ):
            return name + 'x'
        else:
            return name
    else:
        return name


#//******************************************************************************
#//
#//  getSmallNumberName
#//
#//  Returns an english number name for anything from 0 to 999.
#//
#//******************************************************************************

def getSmallNumberName( n ):
    unitNumberNames = [ '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
                        'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
                        'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                        'nineteen' ]

    tensNumberNames = [ '', '', 'twenty', 'thirty', 'forty',
                        'fifty', 'sixty', 'seventy', 'eighty', 'ninety' ]

    hundreds = n // 100
    tens = ( n // 10 ) % 10
    ones = n % 10

    name = ''

    if hundreds > 0:
        name = unitNumberNames[ hundreds ] + ' hundred'

    if tens > 1:
        if name != '':
            name += ' '

        name += tensNumberNames[ tens ]

    if ones > 0:
        if tens > 1:
            name += '-'
            name += unitNumberNames[ ones ]
        elif tens == 1:
            if name != '':
                name += ' '

            name += unitNumberNames[ ones + 10 ]
        else:
            if name != '':
                name += ' '

            name += unitNumberNames[ ones ]
    elif tens == 1:
        if name != '':
            name += ' '

        name += unitNumberNames[ 10 ]

    return name


#//******************************************************************************
#//
#//  getNumberGroupName
#//
#//  returns the name of the "group", i.e., the three-digit group of an integer
#//  separated by commas in the usual notation.  Group 0 has no name because it
#//  represents the "ones".  Group 1 is "thousand", group 2 is "million", etc.
#//
#//******************************************************************************

def getNumberGroupName( n ):
    groupNames = [ '', 'thousand', 'million', 'billion', 'trillion',
                  'quadrillion', 'quintillion', 'sextillion', 'septillion',
                  'octillion', 'nonillion', 'decillion' ]

    onesNames = [ '', 'un', 'duo', 'tre', 'quattuor', 'quinqua', 'se', 'septe', 'octo', 'nove' ]

    tensNames = [ ( '', '' ), ( 'deci', 'n' ), ( 'viginti', 'ms' ), ( 'triginta', 'ns' ),
                  ( 'quadraginta', 'ns' ), ( 'quinquaginta', 'ns' ), ( 'sexaginta', 'n' ),
                  ( 'septuaginta', 'n' ), ( 'octoginta', 'mx' ), ( 'nonaginta', '' ) ]

    hundredsNames = [ ( '', '' ), ( 'centi', 'nx' ), ( 'ducenti', 'n' ), ( 'trecenti', 'ns' ),
                      ( 'quadringenti', 'ns' ), ( 'quingenti', 'ns' ), ( 'sescenti', 'n' ),
                      ( 'septingenti', 'n' ), ( 'octingenti', 'mx' ), ( 'nongenti', '' ) ]

    if n < len( groupNames ):
        return groupNames[ n ]
    else:
        n -= 1

        hundreds = n // 100
        tens = ( n // 10 ) % 10
        ones = n % 10

        name = ''
        hasTens = False
        special = False

        if ones > 0:
            name += onesNames[ ones ]

        if tens > 0:
            hasTens = True

            if name != '':
                name = getModifiedOnesName( name, tensNames[ tens ][ 1 ] )

            name += tensNames[ tens ][ 0 ]

        if hundreds > 0:
            if not hasTens:
                name = getModifiedOnesName( name, hundredsNames[ hundreds ][ 1 ] )

            name += hundredsNames[ hundreds ][ 0 ]

        if name[ -1 ] in 'ai':
            name = name[ : -1 ]

        name += 'illion'

        return name


#//******************************************************************************
#//
#//  getNumberName
#//
#//******************************************************************************

def getNumberName( n ):
    if n == 0:
        return 'zero'

    current = fabs( n )

    if current >= power( 10, 3003 ):
        raise ValueError( 'value out of range for converting to an English name' )

    group = 0
    name = ''

    while current > 0:
        section = getSmallNumberName( int( fmod( current, 1000 ) ) )

        if section != '':
            groupName = getNumberGroupName( group )

            if groupName != '':
                section += ' ' + groupName

            if name == '':
                name = section
            else:
                name = section + ' ' + name

        current = floor( fdiv( current, 1000 ) )
        group += 1

    if n < 0:
        name = 'negative ' + name

    return name


