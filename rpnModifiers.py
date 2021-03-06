#!/usr/bin/env python

# //******************************************************************************
# //
# //  rpnModifiers.py
# //
# //  RPN command-line calculator term modifier operators
# //  copyright (c) 2016, Rick Gutleber (rickg@his.com)
# //
# //  License: GNU GPL 3.0 (see <http://www.gnu.org/licenses/gpl.html> for more
# //  information).
# //
# //******************************************************************************

from mpmath import floor, nint

import rpnGlobals as g


# //******************************************************************************
# //
# //  incrementNestedListLevel
# //
# //******************************************************************************

def incrementNestedListLevel( valueList ):
    g.nestedListLevel += 1

    valueList.append( list( ) )


# //******************************************************************************
# //
# //  decrementNestedListLevel
# //
# //******************************************************************************

def decrementNestedListLevel( valueList ):
    g.nestedListLevel -= 1

    if g.nestedListLevel < 0:
        raise ValueError( 'negative list level (too many \']\'s)' )


# //******************************************************************************
# //
# //  startOperatorList
# //
# //******************************************************************************

def startOperatorList( valueList ):
    if g.operatorList:
        raise ValueError( 'nested operator lists are not supported' )

    g.operatorList = True
    g.lastOperand = len( valueList ) - 1
    g.operandsToRemove = 0
    g.operatorsInList = 0

    valueList.append( list( ) )


# //******************************************************************************
# //
# //  endOperatorList
# //
# //******************************************************************************

def endOperatorList( valueList ):
    if not g.operatorList:
        raise ValueError( 'mismatched operator list ending' )

    g.operatorList = False

    del valueList[ g.lastOperand - ( g.operandsToRemove - 1 ) : g.lastOperand + 2 ]

    result = [ ]

    for i in range( 0, g.operatorsInList ):
        result.insert( 0, valueList.pop( ) )

    valueList.append( result )


# //******************************************************************************
# //
# //  duplicateTerm
# //
# //******************************************************************************

def duplicateTerm( valueList ):
    count = valueList.pop( )
    value = valueList.pop( )

    for i in range( 0, int( count ) ):
        if isinstance( value, list ):
            for j in value:
                valueList.append( j )
        else:
            valueList.append( value )


# //******************************************************************************
# //
# //  duplicateOperation
# //
# //******************************************************************************

def duplicateOperation( valueList ):
    if g.duplicateOperations > 0:
        raise ValueError( "'dupop' must be followed by another operation" )

    if isinstance( valueList[ -1 ], list ):
        raise ValueError( "'dupop' cannot accept a list argument" )

    g.duplicateOperations = nint( floor( valueList.pop( ) ) )


# //******************************************************************************
# //
# //  unlist
# //
# //******************************************************************************

def unlist( valueList ):
    arg = valueList.pop( )

    if isinstance( arg, list ):
        for i in arg:
            valueList.append( i )
    else:
        valueList.append( arg )


# //******************************************************************************
# //
# //  handleUseMembersOperator
# //
# //******************************************************************************

def handleUseMembersOperator( valueList ):
    g.useMembers += 1


# //******************************************************************************
# //
# //  getPrevious
# //
# //******************************************************************************

def getPrevious( valueList ):
    valueList.append( valueList[ -1 ] )


# //******************************************************************************
# //
# //  forEach
# //
# //  TODO
# //
# //******************************************************************************

def forEach( valueList ):
    pass


