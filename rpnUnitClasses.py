#!/usr/bin/env python

# //******************************************************************************
# //
# //  rpnClasses.py
# //
# //  RPN command-line calculator, class declarations
# //  copyright (c) 2016, Rick Gutleber (rickg@his.com)
# //
# //  License: GNU GPL 3.0 (see <http://www.gnu.org/licenses/gpl.html> for more
# //  information).
# //
# //******************************************************************************

import collections

from mpmath import floor

import rpnGlobals as g


# //******************************************************************************
# //
# //  class RPNUnitTypeInfo
# //
# //******************************************************************************

class RPNUnitTypeInfo( object ):
    """This class defines the information needed to define a measurement unit type."""
    def __init__( self, dimensions, baseUnit, estimateTable ):
        self.dimensions = RPNUnits( dimensions )
        self.baseUnitType = RPNUnits( baseUnit )
        self.baseUnit = baseUnit
        self.estimateTable = estimateTable


# //******************************************************************************
# //
# //  class RPNUnitInfo
# //
# //******************************************************************************

class RPNUnitInfo( object ):
    """This class defines the information needed to define a unit of measurement."""
    def __init__( self, unitType, representation, plural, abbrev, aliases, categories,
                  description = '', autoGenerated = False ):
        self.unitType = unitType
        self.representation = representation
        self.plural = plural
        self.abbrev = abbrev
        self.aliases = aliases
        self.categories = categories
        self.description = description
        self.autoGenerated = autoGenerated


# //******************************************************************************
# //
# //  class RPNUnits
# //
# //******************************************************************************

class RPNUnits( collections.Counter ):
    """This class represents a unit of measurement."""
    def __init__( self, *arg, **kw ):
        if ( len( arg ) == 1 ):
            if isinstance( arg[ 0 ], str ):
                self.update( self.parseUnitString( arg[ 0 ] ) )
            elif isinstance( arg[ 0 ], ( list, tuple ) ):
                for item in arg[ 0 ]:
                    self.update( item )  # for Counter, update( ) adds, not replaces
            elif isinstance( arg[ 0 ], ( RPNUnits, dict ) ):
                self.update( arg[ 0 ] )
        else:
            super( RPNUnits, self ).__init__( *arg, **kw )

    def invert( self ):
        for unit in self:
            self[ unit ] = -( self[ unit ] )

        return self

    def getUnitTypes( self ):
        types = RPNUnits( )

        for unit in self:
            if unit in g.basicUnitTypes:
                unitType = unit
            else:
                if unit not in g.unitOperators:
                    raise ValueError( 'undefined unit type \'{}\''.format( unit ) )

                unitType = g.unitOperators[ unit ].unitType

            types[ unitType ] += self[ unit ]

        return types

    def getDimensions( self ):
        result = RPNUnits( )

        for unit in self:
            # if unit not in g.unitOperators:
            #     raise ValueError( 'undefined unit type \'{}\''.format( unit ) )

            dimensions = RPNUnits( g.basicUnitTypes[ g.unitOperators[ unit ].unitType ].dimensions )

            exponent = self.get( unit )

            if exponent != 1:   # handle exponent
                for unit2 in dimensions:
                    dimensions[ unit2 ] *= exponent

            result.update( dimensions )

        return result

    def getBasicTypes( self ):
        result = RPNUnits( )

        for unit in self:
            if unit in g.basicUnitTypes:
                unitType = unit
            else:
                if unit not in g.unitOperators:
                    raise ValueError( 'undefined unit type \'{}\''.format( unit ) )

                unitType = g.unitOperators[ unit ].unitType

            basicUnits = RPNUnits( g.basicUnitTypes[ unitType ].baseUnitType )

            exponent = self[ unit ]

            if exponent != 1:   # handle exponent
                for unitType2 in basicUnits:
                    basicUnits[ unitType2 ] *= exponent

            result.update( basicUnits )

        zeroKeys = [ ]

        for unitType in result:
            if result[ unitType ] == 0:
                zeroKeys.append( unitType )

        for zeroKey in zeroKeys:
            del result[ zeroKey ]

        return result

    def getUnitString( self ):
        resultString = ''

        for unit in sorted( self ):
            exponent = self.get( unit )

            if exponent > 0:
                if resultString != '':
                    resultString += '*'

                resultString += unit

                if exponent > 1:
                    resultString += '^' + str( int( exponent ) )

        denominator = ''

        for unit in sorted( self ):
            exponent = self.get( unit )

            if exponent < 0:
                if denominator != '':
                    denominator += '*'

                denominator += unit

                if exponent < -1:
                    denominator += '^' + str( int( -exponent ) )

        if denominator != '':
            resultString += '/' + denominator

        return resultString

    def parseUnitString( self, expression ):
        pieces = expression.split( '/' )

        if len( pieces ) > 2:
            raise ValueError( 'only one \'/\' is permitted' )
        elif len( pieces ) == 2:
            result = self.parseUnitString( pieces[ 0 ] )
            result.subtract( self.parseUnitString( pieces[ 1 ] ) )

            return result
        else:
            result = RPNUnits( )

            units = expression.split( '*' )

            for unit in units:
                if unit == '':
                    raise ValueError( 'wasn\'t expecting another \'*\' in \'' + expression + '\'' )

                operands = unit.split( '^' )

                plainUnit = operands[ 0 ]

                if plainUnit not in g.unitOperators and plainUnit in g.operatorAliases:
                    plainUnit = g.operatorAliases[ plainUnit ]

                operandCount = len( operands )

                exponent = 1

                if operandCount > 1:
                    for i in range( 1, operandCount ):
                        exponent *= int( floor( operands[ i ] ) )

                result[ plainUnit ] += exponent

            return result

