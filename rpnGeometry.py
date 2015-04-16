#!/usr/bin/env python

# //******************************************************************************
# //
# //  rpnGeometry.py
# //
# //  RPN command-line calculator geometry operators
# //  copyright (c) 2014 (1988), Rick Gutleber (rickg@his.com)
# //
# //  License: GNU GPL 3.0 (see <http://www.gnu.org/licenses/gpl.html> for more
# //  information).
# //
# //******************************************************************************

from mpmath import *

from rpnMeasurement import *


# //******************************************************************************
# //
# //  getRegularPolygonArea
# //
# //  based on having sides of unit length
# //
# //  http://www.mathopenref.com/polygonregulararea.html
# //
# //******************************************************************************

def getRegularPolygonArea( n ):
    if n < 3:
        raise ValueError( 'the number of sides of the polygon cannot be less than 3,' )

    return fdiv( n, fmul( 4, tan( fdiv( pi, n ) ) ) )


# //******************************************************************************
# //
# //  getNSphereRadius
# //
# //  k needs to be a Measurement so getNSphereRadius can tell if it's an area
# //  or a volume and use the correct formula.
# //
# //******************************************************************************

def getNSphereRadius( n, k ):
    if n < 3:
        raise ValueError( 'the number of dimensions must be at least 3' )

    if not isinstance( k, Measurement ):
        return Measurement( k, 'inch' )

    measurementType = k.getBasicTypes( )

    if measurementType == { 'length' : 1 }:
        return k
    elif measurementType == { 'length' : 2 }:
        return fmul( fdiv( gamma( fadd( fdiv( n, 2 ), 1 ) ),
                           fmul( n, power( pi, fdiv( n, 2 ) ) ) ),
                     root( k, fsub( n, 1 ) ) )
    elif measurementType == { 'length' : 3 }:
        return root( fmul( fdiv( gamma( fadd( fdiv( n, 2 ), 1 ) ),
                                 power( pi, fdiv( n, 2 ) ) ), k ), 3 )
    else:
        raise ValueError( 'incompatible measurement type for computing the radius: ' +
                          measurementType )


# //******************************************************************************
# //
# //  getNSphereSurfaceArea
# //
# //  https://en.wikipedia.org/wiki/N-sphere#Volume_and_surface_area
# //
# //  n dimensions, k measurement
# //
# //  If k is a length, then it is taken to be the radius.  If it is a volume
# //  then it is taken to be the volume.  If it is an area, then it is returned
# //  unchanged.  Other measurement types cause an exception.
# //
# //******************************************************************************

def getNSphereSurfaceArea( n, k ):
    if not isinstance( k, Measurement ):
        return getNSphereSurfaceArea( n, Measurement( k, 'inch' ) )

    if n < 3:
        raise ValueError( 'the number of dimensions must be at least 3' )

    measurementType = k.getBasicTypes( )

    if measurementType == { 'length' : 1 }:
        newUnits = Units( k.units )

        for unit in newUnits:
            newUnits[ unit ] *= 2

        return Measurement( fmul( fdiv( fmul( n, power( pi, fdiv( n, 2 ) ) ),
                                  gamma( fadd( fdiv( n, 2 ), 1 ) ) ), power( k, fsub( n, 1 ) ) ),
                            newUnits )
    elif measurementType == { 'length' : 2 }:
        return k
    elif measurementType == { 'length' : 3 }:
        raise ValueError( 'convertion volume to area is not implemented yet' )
        return 3    # TODO: formula for converting volume to surface area
    else:
        raise ValueError( 'incompatible measurement type for computing the surface area' )


# //******************************************************************************
# //
# //  getNSphereVolume
# //
# //  https://en.wikipedia.org/wiki/N-sphere#Volume_and_surface_area
# //
# //  n dimensions, k measurement
# //
# //  If k is a length, then it is taken to be the radius.  If it is an area
# //  then it is taken to be the surface area.  If it is a volume, then it is
# //  returned unchanged.  Other measurement types cause an exception.
# //
# //******************************************************************************

def getNSphereVolume( n, k ):
    if n < 3:
        raise ValueError( 'the number of dimensions must be at least 3' )

    if not isinstance( k, Measurement ):
        return getNSphereVolume( n, Measurement( k, 'inch' ) )

    measurementType = k.getBasicTypes( )

    if measurementType == { 'length' : 1 }:
        return fmul( fdiv( power( pi, fdiv( n, 2 ) ),
                           gamma( fadd( fdiv( n, 2 ), 1 ) ) ), power( k, n ) )
    elif measurementType == { 'length' : 2 }:
        raise ValueError( 'convertion area to volume is not implemented yet' )
        return 2   # TODO: formula for converting surface area to volume
    elif measurementType == { 'length' : 3 }:
        return k
    else:
        raise ValueError( 'incompatible measurement type for computing the volume' )


# //******************************************************************************
# //
# //  getTriangleArea
# //
# //  https://en.wikipedia.org/wiki/Equilateral_triangle#Area
# //
# //******************************************************************************

def getTriangleArea( a, b, c ):
    # semiperimeter
    s = fdiv( fsum( [ a, b, c ] ), 2 )
    return sqrt( fprod( [ s, fsub( s, a ), fsub( s, b ), fsub( s, c ) ] ) )


# //******************************************************************************
# //
# //  getTorusVolume
# //
# //  http://preccalc.sourceforge.net/geometry.shtml
# //
# //  R = major radius
# //  s = minor radius
# //
# //******************************************************************************

def getTorusVolume( R, s ):
    return fprod( [ 2, power( pi, 2 ), R, pow( s, 2 ) ] )


# //******************************************************************************
# //
# //  getTorusSurfaceArea
# //
# //  http://preccalc.sourceforge.net/geometry.shtml
# //
# //  R = major radius
# //  s = minor radius
# //
# //******************************************************************************

def getTorusSurfaceArea( R, s ):
    return fprod( [ 4, power( pi, 2 ), R, s ] )


# //******************************************************************************
# //
# //  getConeVolume
# //
# //  http://preccalc.sourceforge.net/geometry.shtml
# //
# //  r = radius
# //  h = height
# //
# //******************************************************************************

def getConeVolume( r, h ):
    return fprod( [ pi, power( r, 2 ), fdiv( h, 3 ) ] )


# //******************************************************************************
# //
# //  getConeSurfaceArea
# //
# //  http://preccalc.sourceforge.net/geometry.shtml
# //
# //  r = radius
# //  h = height
# //
# //******************************************************************************

def getConeSurfaceArea( r, h ):
    return fprod( [ pi, r, fadd( r, hypot( r, h ) ) ] )

