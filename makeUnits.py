#!/usr/bin/env python

#//******************************************************************************
#//
#//  makeUnits
#//
#//  RPN command-line calculator unit conversion data generator
#//  copyright (c) 2013 (1988), Rick Gutleber (rickg@his.com)
#//
#//  License: GNU GPL (see <http://www.gnu.org/licenses/gpl.html> for more
#//  information).
#//
#//******************************************************************************

import bz2
import contextlib
import itertools
import os
import pickle
import string

from mpmath import *


#//******************************************************************************
#//
#//  constants
#//
#//******************************************************************************

PROGRAM_NAME = 'makeUnits'
PROGRAM_VERSION = '5.7.7'
PROGRAM_DESCRIPTION = 'RPN command-line calculator unit conversion data generator'
COPYRIGHT_MESSAGE = 'copyright (c) 2014, Rick Gutleber (rickg@his.com)'


#//******************************************************************************
#//
#//  basicUnitTypes
#//
#//  unit type : conversion from the basic unit types (length, mass, time)
#//
#//******************************************************************************

basicUnitTypes = {
    'acceleration'  : 'length/time^2',
    'angle'         : 'angle',
    'area'          : 'length^2',
    'energy'        : 'mass*length^2/time^2',
    'force'         : 'mass*length/time',
    'length'        : 'length',
    'mass'          : 'mass',
    'power'         : 'mass*length^2/time',
    'pressure'      : 'mass/length*time^2',
    'time'          : 'time',
    'velocity'      : 'length/time',
    'volume'        : 'length^3',
}


#//******************************************************************************
#//
#//  class UnitInfo
#//
#//******************************************************************************

class UnitInfo( ):
    def __init__( self, unitType, representation, plural, abbrev, aliases ):
        self.unitType = unitType
        self.representation = representation
        self.plural = plural
        self.abbrev = abbrev
        self.aliases = aliases


#//******************************************************************************
#//
#//  unitOperators
#//
#//  unit name : unitType, representation, plural, abbrev, aliases
#//
#//******************************************************************************

unitOperators = {
    # acceleration
    'galileo' :
        UnitInfo( 'acceleration', 'galileo', 'galileos', '', [ ] ),

    'meter/second^2' :
        UnitInfo( 'acceleration', 'meter/second^2', 'meters/second^2', 'm/s^2', [ ] ),

    'standard_gravity' :
        UnitInfo( 'acceleration', 'standard_gravity', 'standard_gravities', 'G', [ ] ),

    # angle

    'degree' :
        UnitInfo( 'angle', 'degree', 'degrees', 'deg', [ ] ),

    'grad' :
        UnitInfo( 'angle', 'grad', 'grads', '', [ 'gon', 'gons' ] ),

    'radian' :
        UnitInfo( 'angle', 'radian', 'radians', 'rad', [ ] ),

    # area

    'acre' :
        UnitInfo( 'area', 'acre', 'acres', 'ac', [ ] ),

    'are' :
        UnitInfo( 'area', 'are', 'ares', 'a', [ ] ),

    'barn' :
        UnitInfo( 'area', 'barn', 'barns', '', [ ] ),

    'rood' :
        UnitInfo( 'area', 'rood', 'roods', '', [ ] ),

    'shed' :
        UnitInfo( 'area', 'shed', 'sheds', '', [ ] ),

    'square_meter' :
        UnitInfo( 'area', 'meter^2', 'square_meters', 'm^2', [ 'meter^2', 'meters^2' ] ),

    'square_yard' :
        UnitInfo( 'area', 'yard^2', 'square_yards', 'sqyd', [ 'sqyd', 'yd^2', 'yard^2', 'yards^2' ] ),

    # energy

    'BTU' :
        UnitInfo( 'energy', 'BTU', 'BTUs', 'BTU', [ 'btu' ] ),

    'calorie' :
        UnitInfo( 'energy', 'calorie', 'calories', 'cal', [ ] ),

    'electron-volt' :
        UnitInfo( 'energy', 'electron-volt', 'electron-volts', 'eV', [ ] ),

    'erg' :
        UnitInfo( 'energy', 'erg', 'ergs', '', [ ] ),

    'horsepower-second' :
        UnitInfo( 'energy', 'horsepower*second', 'horsepower-seconds', 'hps', [ ] ),

    'joule' :
        UnitInfo( 'energy', 'joule', 'joules', 'J', [ ] ),

    'kilogram*meter^2/second^2' :
        UnitInfo( 'energy', 'kilogram*meter^2/second^2', 'kilogram*meter^2/second^2', 'kg*m^2/s^2', [ ] ),

    'planck_energy' :
        UnitInfo( 'energy', 'planck_energy', 'planck_energy', 'EP', [ ] ),

    'ton_of_TNT' :
        UnitInfo( 'energy', 'ton_of_TNT', 'tons_of_TNT', 'tTNT', [ ] ),

    'watt-second' :
        UnitInfo( 'energy', 'watt*second', 'watt-seconds', 'Ws', [ ] ),

    # force

    'dyne' :
        UnitInfo( 'force', 'dyne', 'dyne', 'dyn', [ ] ),

    'gram-force' :
        UnitInfo( 'force', 'gram-force', 'grams-force', 'g-m', [ ] ),

    'joule/meter' :
        UnitInfo( 'force', 'joule/meter', 'joule/meter', 'J/m', [ ] ),

    'newton' :
        UnitInfo( 'force', 'newton', 'newton', 'N', [ ] ),

    'pond' :
        UnitInfo( 'force', 'pond', 'ponds', 'p', [ ] ),

    'pound*foot/second^2' :
        UnitInfo( 'force', 'pound*foot/second^2', 'pound*foot/second^2', 'lb*ft/sec^2', [ ] ),

    'poundal' :
        UnitInfo( 'force', 'poundal', 'poundals', 'pdl', [ ] ),

    'sthene' :
        UnitInfo( 'force', 'sthene', 'sthenes', 'sn', [ ] ),

    # length

    'aln' :
        UnitInfo( 'length', 'aln', 'aln', '', [ ] ),

    'arpent' :
        UnitInfo( 'length', 'arpent', 'arpent', '', [ ] ),

    'angstrom' :
        UnitInfo( 'length', 'angstrom', 'angstroms', 'A', [ ] ),

    'astronomical_unit' :
        UnitInfo( 'length', 'astronomical_unit', 'astronomical_units', 'au', [ ] ),

    'barleycorn' :
        UnitInfo( 'length', 'barleycorn', 'barleycorns', '', [ ] ),

    'caliber' :
        UnitInfo( 'length', 'caliber', 'caliber', '', [ 'calibre' ] ),

    'chain' :
        UnitInfo( 'length', 'chain', 'chains', '', [ ] ),

    'cubit' :
        UnitInfo( 'length', 'cubit', 'cubits', '', [ ] ),

    'ell' :
        UnitInfo( 'length', 'ell', 'ell', '', [ ] ),

    'famn' :
        UnitInfo( 'length', 'famn', 'famn', '', [ ] ),

    'farshimmelt_potrzebie' :
        UnitInfo( 'length', 'farshimmelt_potrzebie', 'farshimmelt potrzebies', 'fpz', [ 'far-potrzebie' ] ),

    'fathom' :
        UnitInfo( 'length', 'fathom', 'fathom', 'fath', [ ] ),

    'finger' :
        UnitInfo( 'length', 'finger', 'finger', '', [ ] ),

    'fingerbreadth' :
        UnitInfo( 'length', 'fingerbreadth', 'fingerbreadths', '', [ 'fingersbreadth' ] ),

    'foot' :
        UnitInfo( 'length', 'foot', 'feet', 'ft', [ ] ),

    'furlong' :
        UnitInfo( 'length', 'furlong', 'furlongs', '', [ ] ),

    'furshlugginer_potrzebie' :
        UnitInfo( 'length', 'furshlugginer_potrzebie', 'furshlugginer potrzebies', 'Fpz', [ 'Fur-potrzebie' ] ),

    'greek_cubit' :
        UnitInfo( 'length', 'greek_cubit', 'greek_cubits', '', [ ] ),

    'hand' :
        UnitInfo( 'length', 'hand', 'hands', '', [ ] ),

    'handbreadth' :
        UnitInfo( 'length', 'handbreadth', 'handbreadths', '', [ 'handsbreadth' ] ),

    'inch' :
        UnitInfo( 'length', 'inch', 'inches', 'in', [ ] ),

    'long_reed' :
        UnitInfo( 'length', 'long_reed', 'long_reeds', '', [ ] ),

    'long_cubit' :
        UnitInfo( 'length', 'long_cubit', 'long_cubits', '', [ ] ),

    'ken' :
        UnitInfo( 'length', 'ken', 'ken', '', [ ] ),

    'league' :
        UnitInfo( 'length', 'league', 'leagues', '', [ ] ),

    'light-second' :
        UnitInfo( 'length', 'light*second', 'light-seconds', '', [ 'light-second' ] ),

    'link' :
        UnitInfo( 'length', 'link', 'link', '', [ ] ),

    'meter' :
        UnitInfo( 'length', 'meter', 'meters', 'm', [ ] ),

    'micron' :
        UnitInfo( 'length', 'micron', 'microns', '', [ ] ),

    'mil' :
        UnitInfo( 'length', 'mil', 'mils', '', [ ] ),

    'mile' :
        UnitInfo( 'length', 'mile', 'miles', 'mi', [ ] ),

    'nail' :
        UnitInfo( 'length', 'nail', 'nail', '', [ ] ),

    'nautical_mile' :
        UnitInfo( 'length', 'nautical_mile', 'nautical_miles', '', [ ] ),

    'perch' :
        UnitInfo( 'length', 'perch', 'perches', '', [ 'pole', 'poles' ] ),

    'pica' :
        UnitInfo( 'length', 'pica', 'pica', '', [ ] ),

    'planck_length' :
        UnitInfo( 'length', 'planck_length', 'planck_length', 'lP', [ ] ),

    'point' :
        UnitInfo( 'length', 'point', 'points', '', [ ] ),

    'reed' :
        UnitInfo( 'length', 'reed', 'reeds', '', [ ] ),

    'rod' :
        UnitInfo( 'length', 'rod', 'rods', 'rd', [ ] ),

    'rope' :
        UnitInfo( 'length', 'rope', 'ropes', '', [ ] ),

    'parsec' :
        UnitInfo( 'length', 'parsec', 'parsecs', 'pc', [ ] ),

    'potrzebie' :
        UnitInfo( 'length', 'potrzebie', 'potrzebies', 'pz', [ ] ),

    'span' :
        UnitInfo( 'length', 'span', 'spans', '', [ ] ),

    'twip' :
        UnitInfo( 'length', 'twip', 'twips', '', [ ] ),

    'yard' :
        UnitInfo( 'length', 'yard', 'yards', 'yd', [ ] ),

    # mass

    'blintz' :
        UnitInfo( 'mass', 'blintz', 'blintzes', 'b', [ ] ),

    'carat' :
        UnitInfo( 'mass', 'carat', 'carats', 'kt', [ ] ),

    'farshimmelt_blintz' :
        UnitInfo( 'mass', 'farshimmelt_blintz', 'farshimmelt blintzes', 'fb', [ 'far-blintz' ] ),

    'furshlugginer_blintz' :
        UnitInfo( 'mass', 'furshlugginer_blintz', 'furshlugginer blintzes', 'Fb', [ 'Fur-blintz' ] ),

    'grain' :
        UnitInfo( 'mass', 'grain', 'grains', 'gr', [ ] ),

    'gram' :
        UnitInfo( 'mass', 'gram', 'grams', 'g', [ ] ),

    'ounce' :
        UnitInfo( 'mass', 'ounce', 'ounces', 'oz', [ ] ),

    'pennyweight' :
        UnitInfo( 'mass', 'pennyweight', 'pennyweights', 'dwt', [ ] ),

    'planck_mass' :
        UnitInfo( 'mass', 'planck_mass', 'planck_masses', 'mP', [ ] ),

    'pound' :
        UnitInfo( 'mass', 'pound', 'pounds', 'lb', [ ] ),

    'slug' :
        UnitInfo( 'mass', 'slug', 'slug', '', [ ] ),

    'stone' :
        UnitInfo( 'mass', 'stone', 'stone', '', [ ] ),

    'ton' :
        UnitInfo( 'mass', 'ton', 'tons', '', [ ] ),

    'tonne' :
        UnitInfo( 'mass', 'tonne', 'tonnes', '', [ ] ),

    'troy_ounce' :
        UnitInfo( 'mass', 'troy_ounce', 'troy_ounces', '', [ ] ),

    'troy_pound' :
        UnitInfo( 'mass', 'troy_pound', 'troy_pounds', '', [ ] ),

    # power

    'horsepower' :
        UnitInfo( 'power', 'horsepower', 'horsepower', 'hp', [ ] ),

    'joule/second' :
        UnitInfo( 'power', 'joule/second', 'joules/second', 'J/s', [ ] ),

    'watt' :
        UnitInfo( 'power', 'watt', 'watts', 'W', [ ] ),

    # pressure

    'atmosphere' :
        UnitInfo( 'pressure', 'atmosphere', 'atmospheres', 'atm', [ ] ),

    'bar' :
        UnitInfo( 'pressure', 'bar', 'bar', '', [ ] ),

    'mmHg' :
        UnitInfo( 'pressure', 'mmHg', 'mmHg', '', [ ] ),

    'newton/meter^2' :
        UnitInfo( 'pressure', 'newton/meter^2', 'newtons/meter^2', 'N/m^2', [ ] ),

    'pascal' :
        UnitInfo( 'pressure', 'pascal', 'pascal', 'Pa', [ ] ),

    'psi' :
        UnitInfo( 'pressure', 'pound/inch^2', 'pounds/inch^2', 'psi', [ 'lb/in^2' ] ),

    'torr' :
        UnitInfo( 'pressure', 'torr', 'torr', '', [ ] ),

    # time

    'clarke' :
        UnitInfo( 'time', 'clarke', 'clarkes', '', [ ] ),

    'cowznofski' :
        UnitInfo( 'time', 'cowznofski', 'cowznofskis', '', [ ] ),

    'day' :
        UnitInfo( 'time', 'day', 'days', '', [ ] ),

    'fortnight' :
        UnitInfo( 'time', 'fortnight', 'fortnights', '', [ ] ),

    'hour' :
        UnitInfo( 'time', 'hour', 'hours', 'hr', [ ] ),

    'kovac' :
        UnitInfo( 'time', 'kovac', 'kovacs', '', [ ] ),

    'martin' :
        UnitInfo( 'time', 'martin', 'martins', '', [ ] ),

    'mingo' :
        UnitInfo( 'time', 'mingo', 'mingoes', '', [ ] ),

    'minute' :
        UnitInfo( 'time', 'minute', 'minutes', '', [ ] ),   # 'min' is already an operator

    'planck_time' :
        UnitInfo( 'time', 'planck_time', 'x planck_time', 'tP', [ ] ),

    'second' :
        UnitInfo( 'time', 'second', 'seconds', '', [ ] ),   # 'sec' is already an operator

    'week' :
        UnitInfo( 'time', 'week', 'weeks', 'wk', [ ] ),

    'wolverton' :
        UnitInfo( 'time', 'wolverton', 'wolvertons', '', [ ] ),

    'wood' :
        UnitInfo( 'time', 'wood', 'woods', '', [ ] ),

    'year' :
        UnitInfo( 'time', 'year', 'year', 'y', [ ] ),

    # velocity

    'meter/second' :
        UnitInfo( 'velocity', 'meter/second', 'meters per second', 'm/s', [ 'light' ] ),

    'knot' :
        UnitInfo( 'velocity', 'knot', 'knots', 'kt', [ ] ),

    'light' :
        UnitInfo( 'velocity', 'light', 'x_speed_of_light', 'c', [ 'speed_of_light' ] ),

    'mach' :
        UnitInfo( 'velocity', 'mach', 'mach', '', [ ] ),

    # volume

    'acre-foot' :
        UnitInfo( 'volume', 'acre*foot', 'acre_feet', 'ac*ft', [ ] ),

    'barrel' :
        UnitInfo( 'volume', 'barrel', 'barrels', '', [ ] ),

    'cord' :
        UnitInfo( 'volume', 'cord', 'cord', '', [ ] ),

    'cubic_foot' :
        UnitInfo( 'volume', 'foot^3', 'cubic_feet', 'cuft', [ 'ft^3', 'foot^3', 'feet^3' ] ),

    'cubic_meter' :
        UnitInfo( 'volume', 'meter^3', 'cubic_meters', 'm^3', [ 'meter^3', 'meters^3' ] ),

    'cup' :
        UnitInfo( 'volume', 'cup', 'cups', '', [ ] ),

    'dessertspoon' :
        UnitInfo( 'volume', 'dessertspoon', 'dessertspoons', '', [ ] ),

    'dram' :
        UnitInfo( 'volume', 'dram', 'drams', '', [ ] ),

    'fifth' :
        UnitInfo( 'volume', 'fifth', 'fifths', '', [ ] ),

    'firkin' :
        UnitInfo( 'volume', 'firkin', 'firkins', '', [ ] ),

    'fluid_ounce' :
        UnitInfo( 'volume', 'fluid_ounce', 'fluid_ounces', 'floz', [ ] ),

    'farshimmelt_ngogn' :
        UnitInfo( 'volume', 'farshimmelt_ngogn', 'farshimmelt ngogns', 'fn', [ 'far-ngogn' ] ),

    'furshlugginer_ngogn' :
        UnitInfo( 'volume', 'furshlugginer_ngogn', 'furshlugginer ngogns', 'Fn', [ 'Fur-ngogn' ] ),

    'gallon' :
        UnitInfo( 'volume', 'gallon', 'gallons', 'gal', [ ] ),

    'gill' :
        UnitInfo( 'volume', 'gill', 'gills', '', [ ] ),

    'hogshead' :
        UnitInfo( 'volume', 'hogshead', 'hogsheads', '', [ ] ),

    'liter' :
        UnitInfo( 'volume', 'liter', 'liters', 'l', [ ] ),

    'minim':
        UnitInfo( 'volume', 'minim', 'minims', '', [ ] ),

    'ngogn' :
        UnitInfo( 'volume', 'ngogn', 'ngogns', 'n', [ ] ),

    'oil_barrel' :
        UnitInfo( 'volume', 'oil_barrel', 'oil_barrels', 'bbl', [ ] ),

    'pinch' :
        UnitInfo( 'volume', 'pinch', 'pinches', '', [ ] ),

    'pint' :
        UnitInfo( 'volume', 'pint', 'pints', 'pt', [ ] ),

    'quart' :
        UnitInfo( 'volume', 'quart', 'quarts', 'qt', [ ] ),

    'stere' :
        UnitInfo( 'volume', 'stere', 'steres', 'st', [ ] ),

    'tablespoon' :
        UnitInfo( 'volume', 'tablespoon', 'tablespoons', 'tbsp', [ ] ),

    'teaspoon' :
        UnitInfo( 'volume', 'teaspoon', 'teaspoons', 'tsp', [ ] ),

    'tun' :
        UnitInfo( 'volume', 'tun', 'tuns', '', [ ] ),
}


#//******************************************************************************
#//
#//  metricUnits
#//
#//  ... or any units that should get the SI prefixes
#//
#//  ( name, plural name, abbreviation, aliases, plural aliases )
#//
#//******************************************************************************

metricUnits = [
    ( 'are',            'ares',             'a',    [ ], [ ] ),
    ( 'blintz',         'blintzes',         'b',    [ ], [ ] ),
    ( 'calorie',        'calories',         'cal',  [ ], [ ] ),
    ( 'electron-volt',  'electron-volts',   'eV',   [ ], [ ] ),
    ( 'gram',           'grams',            'g',    [ 'gramme' ], [ 'grammes' ] ),
    ( 'gram-force',     'grams-force',      'gf',   [ 'gramme-force' ], [ 'grammes-force' ] ),
    ( 'joule',          'joules',           'J',    [ ], [ ] ),
    ( 'liter',          'liters',           'l',    [ 'litre' ], [ 'litres' ] ),
    ( 'meter',          'meters',           'm',    [ 'metre' ], [ 'metres' ] ),
    ( 'newton',         'newtons',          'N',    [ ], [ ] ),
    ( 'ngogn',          'ngogns',           'n',    [ ], [ ] ),
    ( 'pascal',         'pascals',          'Pa',   [ ], [ ] ),
    ( 'pond',           'ponds',            'p',    [ ], [ ] ),
    ( 'potrzebie',      'potrzebies',       'pz',   [ ], [ ] ),
    ( 'second',         'seconds',          's',    [ ], [ ] ),
    ( 'stere',          'steres',           'st',   [ ], [ ] ),
    ( 'ton_of_TNT',     'tons_of_TNT',      'tTNT', [ ], [ ] ),
    ( 'watt',           'watts',            'W',    [ ], [ ] ),
    ( 'watt-second',    'watt-seconds',     'Ws',   [ ], [ ] ),
]


#//******************************************************************************
#//
#//  timeUnits
#//
#//******************************************************************************

timeUnits = [
    ( 'minute',     'minutes',      'm',        '60' ),
    ( 'hour',       'hours',        'h',        '3600' ),
    ( 'day',        'days',         'd',        '86400' ),
    ( 'year',       'years',        'y',        '31557600' ),   # 365.25 days
]


#//******************************************************************************
#//
#//  metricPrefixes
#//
#//  ( name, abbreviation, power of 10 )
#//
#//******************************************************************************

metricPrefixes = [
    ( 'yotta',      'Y',      '24' ),
    ( 'zetta',      'Z',      '21' ),
    ( 'exa',        'E',      '18' ),
    ( 'peta',       'P',      '15' ),
    ( 'tera',       'T',      '12' ),
    ( 'giga',       'G',      '9' ),
    ( 'mega',       'M',      '6' ),
    ( 'kilo',       'k',      '3' ),
    ( 'hecto',      'h',      '2' ),
    ( 'deca',       'da',     '1' ),
    ( 'deci',       'd',      '-1' ),
    ( 'centi',      'c',      '-2' ),
    ( 'milli',      'm',      '-3' ),
    ( 'micro',      'mc',     '-6' ),
    ( 'nano',       'n',      '-9' ),
    ( 'pico',       'p',      '-12' ),
    ( 'femto',      'f',      '-15' ),
    ( 'atto',       'a',      '-18' ),
    ( 'zepto',      'z',      '-21' ),
    ( 'yocto',      'y',      '-24' ),
]


#//******************************************************************************
#//
#//  metricPrefixes
#//
#//  ( first unit, second unit, conversion factor )
#//
#//******************************************************************************

unitConversionMatrix = {
    ( 'acre',                  'square_yard' )                     : '4840',
    ( 'acre-foot',             'cubic_foot' )                      : '43560',
    ( 'are',                   'square_meter' )                    : '100',
    ( 'astronomical_unit',     'meter' )                           : '149597870700',
    ( 'atmosphere',            'pascal' )                          : '101325',
    ( 'bar',                   'pascal' )                          : '100000',
    ( 'barrel',                'gallon' )                          : '31.5',
    ( 'blintz',                'farshimmelt_blintz' )              : '100000',
    ( 'blintz',                'gram' )                            : '36.42538631',
    ( 'BTU',                   'joule' )                           : '1054.5',
    ( 'calorie',               'joule' )                           : '4.184',
    ( 'carat',                 'grain' )                           : '3.1666666666666666666666',
    ( 'chain',                 'yard' )                            : '22',
    ( 'clarke',                'day' )                             : '1',
    ( 'clarke',                'wolverton' )                       : '100000',
    ( 'cord',                  'cubic_foot' )                      : '128',
    ( 'cowznofski',            'mingo' )                           : '10',
    ( 'cubic_meter',           'liter' )                           : '1000',
    ( 'cup',                   'dram' )                            : '64',
    ( 'cup',                   'fluid_ounce' )                     : '8',
    ( 'cup',                   'gill' )                            : '2',
    ( 'day',                   'hour' )                            : '24',
    ( 'dessertspoon',          'teaspoon' )                        : '2',
    ( 'firkin',                'gallon' )                          : '9',
    ( 'fluid_ounce',           'minim' )                           : '480',
    ( 'fluid_ounce',           'tablespoon' )                      : '2',
    ( 'foot',                  'inch' )                            : '12',
    ( 'fortnight',             'day' )                             : '14',
    ( 'furlong',               'yard' )                            : '220',
    ( 'furshlugginer_blintz',  'blintz' )                          : '1000000',
    ( 'furshlugginer_ngogn',   'ngogn' )                           : '1000000',
    ( 'furshlugginer_potrzebie', 'potrzebie' )                     : '1000000',
    ( 'gallon',                'fifth' )                           : '5',
    ( 'gallon',                'quart' )                           : '4',
    ( 'grad',                  'degree' )                          : '0.9',
    ( 'gram',                  'planck_mass' )                     : '45940.892447777',
    ( 'hogshead',              'gallon' )                          : '63',
    ( 'horsepower',            'watt' )                            : '745.69987158227022',
    ( 'horsepower-second',     'joule' )                           : '745.69987158227022',
    ( 'hour',                  'minute' )                          : '60',
    ( 'inch',                  'meter' )                           : '0.0254',
    ( 'joule',                 'electron-volt' )                   : '6.24150974e18',
    ( 'joule',                 'erg' )                             : '10000000',
    ( 'joule',                 'kilogram*meter^2/second^2' )       : '1',
    ( 'joule/second',          'watt' )                            : '1',
    ( 'meter/second',          'knot' )                            : '1.943844492',
    ( 'kovac',                 'wolverton' )                       : '1000',
    ( 'league',                'mile' )                            : '3',
    ( 'light',                 'meter/second' )                    : '299792458',
    ( 'light-second',          'meter' )                           : '299792458',
    ( 'liter',                 'ngogn' )                           : '86.2477899004',
    ( 'mach',                  'meter/second' )                    : '295.0464',
    ( 'martin',                'kovac' )                           : '100',
    ( 'meter',                 'angstrom' )                        : '10000000000',
    ( 'meter',                 'micron' )                          : '1000000',
    ( 'mile',                  'foot' )                            : '5280',
    ( 'mingo',                 'clarke' )                          : '10',
    ( 'minute',                'second' )                          : '60',
    ( 'mmHg',                  'pascal' )                          : '133.3224',        # approx.
    ( 'nautical_mile',         'meter' )                           : '1852',
    ( 'newton',                'dyne' )                            : '100000',
    ( 'newton',                'joule/meter' )                     : '1',
    ( 'newton',                'pond' )                            : '101.97161298',
    ( 'newton',                'poundal' )                         : '7.233013851',
    ( 'newton/meter^2',        'pascal' )                          : '1',
    ( 'ngogn',                 'farshimmelt_ngogn' )               : '100000',
    ( 'oil_barrel',            'gallon' )                          : '42',
    ( 'ounce',                 'gram' )                            : '28.349523125',
#    ( 'parsec',                'light-year' )                      : '3.261563776971',
    ( 'potrzebie',             'farshimmelt_potrzebie' )           : '100000',
    ( 'potrzebie',             'meter' )                           : '0.002263348517438173216473',  # see Mad #33
    ( 'pound',                 'grain' )                           : '7000',
    ( 'pound',                 'ounce' )                           : '16',
    ( 'psi',                   'pascal' )                          : '6894.757',        # approx.
    ( 'quart',                 'cup' )                             : '4',
    ( 'quart',                 'liter' )                           : '0.946352946',
    ( 'quart',                 'pint' )                            : '2',
    ( 'radian',                'degree' )                          : '57.2957795130823208768',
    ( 'rod',                   'foot' )                            : '16.5',
    ( 'rood',                  'square_yard' )                     : '1210',
    ( 'square_meter',          'barn' )                            : '1.0e28',
    ( 'square_meter',          'shed' )                            : '1.0e52',
    ( 'standard_gravity',      'galileo' )                         : '980.6650',
    ( 'standard_gravity',      'meter/second^2' )                  : '9.806650',
    ( 'sthene',                'newton' )                          : '1000',
    ( 'stone',                 'pound' )                           : '14',
    ( 'tablespoon',            'teaspoon' )                        : '3',
    ( 'teaspoon',              'pinch' )                           : '8',
    ( 'ton',                   'pound' )                           : '2000',
    ( 'tonne',                 'gram' )                            : '1000000',
    ( 'ton_of_TNT',            'joule' )                           : '4184000000',
    ( 'torr',                  'mmHg' )                            : '1',
    ( 'troy_ounce',            'gram' )                            : '31.1034768',
    ( 'troy_pound',            'pound' )                           : '12',
    ( 'tun',                   'gallon' )                          : '252',
    ( 'watt-second',           'joule' )                           : '1',
    ( 'week',                  'day' )                             : '7',
    ( 'wood',                  'martin' )                          : '100',
    ( 'yard',                  'foot' )                            : '3',
    ( 'year',                  'day' )                             : '365.25',
    ( 'rope',                  'foot' )                            : '20',
    ( 'perch',                 'foot' )                            : '16.5',
    ( 'fathom',                'foot' )                            : '6',
    ( 'ell',                   'inch' )                            : '45',
    ( 'link',                  'inch' )                            : '7.92',
    ( 'span',                  'inch' )                            : '9',
    ( 'finger',                'inch' )                            : '4.5',
    ( 'nail',                  'inch' )                            : '2.25',
    ( 'inch',                  'barleycorn' )                      : '3',
    ( 'inch',                  'mil' )                             : '1000',
    ( 'arpent',                'foot' )                            : '192',
    ( 'inch',                  'pica' )                            : '6',
    ( 'inch',                  'point' )                           : '72',
    ( 'inch',                  'twip' )                            : '1440',
    ( 'famn',                  'aln' )                             : '3',
    ( 'aln',                   'inch' )                            : '23.377077865',
    ( 'inch',                  'caliber' )                         : '100',
    ( 'ken',                   'inch' )                            : '83.4',
    ( 'reed',                  'foot' )                            : '9',
    ( 'long_reed',             'foot' )                            : '10.5',
    ( 'cubit',                 'inch' )                            : '18',
    ( 'greek_cubit',           'inch' )                            : '18.22',
    ( 'long_cubit',            'inch' )                            : '21',
    ( 'handbreadth',           'inch' )                            : '3',
    ( 'fingerbreadth',         'inch' )                            : '0.75',
    ( 'slug',                  'pound' )                           : '32.174048556',
    ( 'planck_time',           'second' )                          : '5.39106e-44',
    ( 'planck_energy',         'joule' )                           : '1.956e9',
    ( 'planck_length',         'meter' )                           : '1.616199e-35',
#    ( 'planck_charge',         'coulomb' )                         : '1.875545956e-18',
}


#//******************************************************************************
#//
#//  makeMetricUnit
#//
#//******************************************************************************

def makeMetricUnit( prefix, unit ):
    if unit[ 0 ] == 'a' and ( ( prefix[ -1 ] in 'a' ) or ( prefix[ -3 : ] == 'cto' ) ):
        return prefix[ : -1 ] + unit
    else:
        return prefix + unit


#//******************************************************************************
#//
#//  makeUnitTypeTable
#//
#//  maps each unit type to a list of units with that type
#//
#//******************************************************************************

def makeUnitTypeTable( unitOperators ):
    unitTypeTable = { }

    for unitType in basicUnitTypes:
        unitTypeTable[ unitType ] = [ ]

    for unit in unitOperators:
        unitTypeTable[ unitOperators[ unit ].unitType ].append( unit )

    return unitTypeTable


#//******************************************************************************
#//
#//  makeAliases
#//
#//******************************************************************************

def makeAliases( ):
    newAliases = { }

    for metricUnit in metricUnits:
        newAliases[ metricUnit[ 2 ] ] = metricUnit[ 0 ]

        for prefix in metricPrefixes:
            unit = makeMetricUnit( prefix[ 0 ], metricUnit[ 0 ] )
            pluralUnit = makeMetricUnit( prefix[ 0 ], metricUnit[ 1 ] )
            newAliases[ pluralUnit ] = unit                     # add plural alias

            newAliases[ prefix[ 1 ] + metricUnit[ 2 ] ] = unit   # add SI abbreviation alias

            for alternateUnit in metricUnit[ 3 ]:                # add alternate spelling alias
                newAliases[ makeMetricUnit( prefix[ 0 ], alternateUnit ) ] = unit

            for alternateUnit in metricUnit[ 4 ]:                # add alternate spelling plural alias
                newAliases[ makeMetricUnit( prefix[ 0 ], alternateUnit ) ] = unit

    for unit in unitOperators:
        unitInfo = unitOperators[ unit ]
        newAliases[ unitInfo.plural ] = unit

        if unitInfo.abbrev != '':
            newAliases[ unitInfo.abbrev ] = unit

    #for i in newAliases:
    #    print( i, newAliases[ i ] )
    return newAliases


#//******************************************************************************
#//
#//  expandMetricUnits
#//
#//  Every metric unit needs to be permuted for all SI power types.  We need to
#//  create conversions for each new type, as well as aliases.
#//
#//******************************************************************************

def expandMetricUnits( newAliases ):
    # expand metric measurements for all prefixes
    newConversions = { }

    for metricUnit in metricUnits:
        for prefix in metricPrefixes:
            newName = makeMetricUnit( prefix[ 0 ], metricUnit[ 0 ] )
            newPlural = makeMetricUnit( prefix[ 0 ], metricUnit[ 1 ] )

            # constuct unit operator info
            unitOperators[ newName ] = \
                UnitInfo( unitOperators[ metricUnit[ 0 ] ].unitType, newName, newPlural,
                                         prefix[ 1 ] + metricUnit[ 2 ], [ ] )

            newConversion = power( 10, mpmathify( prefix[ 2 ] ) )
            unitConversionMatrix[ ( newName, metricUnit[ 0 ] ) ] = str( newConversion )
            newConversion = fdiv( 1, newConversion )
            unitConversionMatrix[ ( metricUnit[ 0 ], newName ) ] = str( newConversion )

            for op1, op2 in unitConversionMatrix:
                if ( op1 == metricUnit[ 0 ] ) or ( op2 == metricUnit[ 0 ] ):
                    oldConversion = mpmathify( unitConversionMatrix[ ( op1, op2 ) ] )

                    if op1 == metricUnit[ 0 ] and newName != op2:
                        newConversions[ ( newName, op2 ) ] = str( fdiv( oldConversion, newConversion ) )
                    elif op2 == metricUnit[ 0 ] and newName != op1:
                        newConversions[ ( op1, newName ) ] = str( fmul( oldConversion, newConversion ) )

            if unitOperators[ metricUnit[ 0 ] ].unitType == 'length':
                newUnitInfo, newUnitAliases = makeAreaOperator( newName, newPlural )

                newUnit = 'square_' + newName
                unitOperators[ newUnit ] = newUnitInfo
                newAliases.update( newUnitAliases )

                oldUnit = 'square_' + metricUnit[ 0 ]

                # add new conversions
                areaConversion = power( newConversion, 2 )

                newConversions[ ( oldUnit, newUnit ) ] = str( areaConversion )
                newConversions[ ( newUnit, oldUnit ) ] = str( fdiv( 1, areaConversion ) )

                for op1, op2 in unitConversionMatrix:
                    if ( op1 == oldUnit ) or ( op2 == oldUnit ):
                        oldConversion = mpmathify( unitConversionMatrix[ ( op1, op2 ) ] )

                        if op1 == oldUnit and newUnit != op2:
                            newConversions[ ( newUnit, op2 ) ] = str( fdiv( oldConversion, areaConversion ) )
                        elif op2 == oldUnit and newUnit != op1:
                            newConversions[ ( op1, newUnit ) ] = str( fmul( oldConversion, areaConversion ) )

                newUnitInfo, newUnitAliases = makeVolumeOperator( newName, newPlural )

                newUnit = 'cubic_' + newName
                unitOperators[ newUnit ] = newUnitInfo
                newAliases.update( newUnitAliases )

                oldUnit = 'cubic_' + metricUnit[ 0 ]

                # add new conversions
                volumeConversion = power( newConversion, 3 )

                newConversions[ ( oldUnit, newUnit ) ] = str( volumeConversion )
                newConversions[ ( newUnit, oldUnit ) ] = str( fdiv( 1, volumeConversion ) )

                for op1, op2 in unitConversionMatrix:
                    if ( op1 == oldUnit ) or ( op2 == oldUnit ):
                        oldConversion = mpmathify( unitConversionMatrix[ ( op1, op2 ) ] )

                        if op1 == oldUnit and newUnit != op2:
                            newConversions[ ( newUnit, op2 ) ] = str( fdiv( oldConversion, volumeConversion ) )
                            #print( newUnit, op2, volumeConversion )
                        elif op2 == oldUnit and newUnit!= op1:
                            newConversions[ ( op1, newUnit) ] = str( fmul( oldConversion, volumeConversion ) )
                            #print( op1, newUnit, volumeConversion )

    return newConversions


#//******************************************************************************
#//
#//  makeAreaOperator
#//
#//******************************************************************************

def makeAreaOperator( unit, unitPlural ):
    unitInfo = unitOperators[ unit ]

    newAliases = { }

    newUnit = 'square_' + unit

    if unitInfo.abbrev == '':
        abbrev = 'sq' + unit
    else:
        abbrev = 'sq' + unitInfo.abbrev
        newAliases[ 'sq' + unitInfo.abbrev ] = newUnit

    newUnitInfo = UnitInfo( 'area', unit + '^2', 'square_' + unitPlural, abbrev, [ ] )

    newAliases[ 'square_' + unitInfo.plural ] = newUnit
    newAliases[ 'square_' + unitInfo.abbrev ] = newUnit
    newAliases[ 'sq' + unitInfo.plural ] = newUnit
    newAliases[ unit +  '^2' ] = newUnit
    newAliases[ unitInfo.plural + '^2' ] = newUnit

    return newUnitInfo, newAliases


#//******************************************************************************
#//
#//  makeVolumeOperator
#//
#//******************************************************************************

def makeVolumeOperator( unit, unitPlural ):
    unitInfo = unitOperators[ unit ]

    newAliases = { }

    newUnit = 'cubic_' + unit

    if unitInfo.abbrev == '':
        abbrev = 'cu' + unit
    else:
        abbrev = 'cu' + unitInfo.abbrev
        newAliases[ 'cu' + unitInfo.abbrev ] = newUnit

    newUnitInfo = UnitInfo( 'volume', unit + '^3', 'cubic_' + unitPlural, abbrev, [ ] )

    newAliases[ 'cubic_' + unitInfo.plural ] = newUnit
    newAliases[ 'cubic_' + unitInfo.abbrev ] = newUnit
    newAliases[ 'cu' + unitInfo.plural ] = newUnit
    newAliases[ unit +  '^3' ] = newUnit
    newAliases[ unitInfo.plural + '^3' ] = newUnit

    return newUnitInfo, newAliases


#//******************************************************************************
#//
#//  initializeConversionMatrix
#//
#//******************************************************************************

def initializeConversionMatrix( unitConversionMatrix ):
    mp.dps = 50

    # reverse each conversion
    print( 'Reversing each conversion...' )

    newConversions = { }

    for op1, op2 in unitConversionMatrix:
        conversion = fdiv( 1, mpmathify( unitConversionMatrix[ ( op1, op2 ) ] ) )
        newConversions[ ( op2, op1 ) ] = str( conversion )

    unitConversionMatrix.update( newConversions )

    # create map for compound units based on the conversion matrix
    print( )
    print( 'Mapping compound units...' )

    compoundUnits = { }

    for unit1, unit2 in unitConversionMatrix:
        chars = set( '*/^' )

        if any( ( c in chars ) for c in unit2 ):
            compoundUnits[ unit1 ] = unit2
            print( '    compound unit: ', unit1, '(', unit2, ')' )

    # create area and volume units from all of the length units
    print( )
    print( 'Creating area and volume units for all length units...' )

    newOperators = { }
    newAliases = { }

    for unit in unitOperators:
        unitInfo = unitOperators[ unit ]

        if unitInfo.unitType == 'length':
            newUnit = 'square_' + unit

            if newUnit not in unitOperators:
                newUnitInfo, newUnitAliases = makeAreaOperator( unit, unitOperators[ unit ].plural )

                newAliases.update( newUnitAliases )
                newOperators[ newUnit ] = newUnitInfo

            newUnit = 'cubic_'+ unit

            if newUnit not in unitOperators:
                newUnitInfo, newUnitAliases = makeVolumeOperator( unit, unitOperators[ unit ].plural )

                newAliases.update( newUnitAliases )
                newOperators[ newUnit ] = newUnitInfo

    unitOperators.update( newOperators )

    # add new conversions for the new area and volume units
    print( 'Adding new conversions for the new area and volume units...' )

    newConversions = { }

    for op1, op2 in unitConversionMatrix:
        if unitOperators[ op1 ].unitType == 'length':
            conversion = mpmathify( unitConversionMatrix[ ( op1, op2 ) ] )
            newConversions[ ( 'square_' + op1, 'square_' + op2 ) ] = str( power( conversion, 2 ) )
            newConversions[ ( 'cubic_' + op1, 'cubic_' + op2 ) ] = str( power( conversion, 3 ) )

    unitConversionMatrix.update( newConversions )

    # extrapolate transitive conversions
    print( )
    print( 'Extrapolating transitive conversions for', len( unitOperators ), 'units...' )

    unitTypeTable = makeUnitTypeTable( unitOperators )

    for unitType in basicUnitTypes:
        print( '    ', unitType, '({} operators)'.format( len( unitTypeTable[ unitType ] ) ) )

        while True:
            newConversion = False

            for op1, op2 in itertools.combinations( unitTypeTable[ unitType ], 2 ):
                if ( op1, op2 ) in unitConversionMatrix:
                    #print( )
                    #print( ( op1, op2 ), ': ', unitConversionMatrix[ ( op1, op2 ) ] )

                    for op3 in unitTypeTable[ unitType ]:
                        # we can ignore duplicate operators
                        if ( op3 == op1 ) or ( op3 == op2 ):
                            continue

                        # we can shortcut if the types are not compatible
                        if unitOperators[ op3 ].unitType != unitOperators[ op1 ].unitType:
                            continue

                        conversion = mpmathify( unitConversionMatrix[ ( op1, op2 ) ] )

                        if ( op1, op3 ) not in unitConversionMatrix and ( op2, op3 ) in unitConversionMatrix:
                            #print( 'transitive: ', ( op2, op3 ), unitConversionMatrix[ ( op2, op3 ) ] )
                            newConversion = fmul( conversion, mpmathify( unitConversionMatrix[ ( op2, op3 ) ] ) )
                            #print( ( op1, op3 ), newConversion )
                            unitConversionMatrix[ ( op1, op3 ) ] = str( newConversion )
                            #print( ( op3, op1 ), fdiv( 1, newConversion ) )
                            unitConversionMatrix[ ( op3, op1 ) ] = str( fdiv( 1, newConversion ) )

                            newConversion = True
                        elif ( op2, op3 ) not in unitConversionMatrix and ( op1, op3 ) in unitConversionMatrix:
                            #print( 'transitive: ', ( op1, op3 ), unitConversionMatrix[ ( op1, op3 ) ] )
                            newConversion = fdiv( mpmathify( unitConversionMatrix[ ( op1, op3 ) ] ), conversion )
                            #print( ( op2, op3 ), newConversion )
                            unitConversionMatrix[ ( op2, op3 ) ] = str( newConversion )
                            #print( ( op3, op2 ), fdiv( 1, newConversion ) )
                            unitConversionMatrix[ ( op3, op2 ) ] = str( fdiv( 1, newConversion ) )

                            newConversion = True

                print( len( unitConversionMatrix ), end='\r' )

            if not newConversion:
                break

    # expand metric operators and add new conversions, aliases, etc.
    print( '           ' )
    print( 'Expanding metric units against the list of SI prefixes...' )

    newAliases = { }

    unitConversionMatrix.update( expandMetricUnits( newAliases ) )

    # add new operators for compound time units
    print( 'Expanding compound time units...' )

    newUnitOperators = { }

    for unit in unitOperators:
        if unit[ -7 : ] == '-second' and unit[ : 7 ] != 'square_' and unit[ : 6 ] != 'cubic_':
            unitRoot = unit[ : -7 ]

            unitInfo = unitOperators[ unit ]
            rootUnitInfo = unitOperators[ unitRoot ]

            for timeUnit in timeUnits:
                newUnit = unitRoot + '-' + timeUnit[ 0 ]
                newPlural = unitRoot + '-' + timeUnit[ 1 ]
                newAliases[ newPlural ] = newUnit
                newAliases[ unitRoot + '-' + timeUnit[ 1 ] ] = newUnit

                # We assume the abbrev ends with an s for second
                if unitInfo.abbrev != '':
                    newAbbrev = unitInfo.abbrev[ : -1 ] + timeUnit[ 2 ]
                    newAliases[ newAbbrev ] = newUnit

                for alias in rootUnitInfo.aliases:
                    newAliases[ alias + '*' + timeUnit[ 0 ] ] = newUnit
                    newAliases[ alias + '-' + timeUnit[ 0 ] ] = newUnit
                    newAliases[ alias + '*' + timeUnit[ 1 ] ] = newUnit
                    newAliases[ alias + '-' + timeUnit[ 1 ] ] = newUnit

                newUnitOperators[ newUnit ] = \
                    UnitInfo( unitInfo.unitType, unitRoot + '*' + timeUnit[ 0 ],
                              newPlural, '', [ ] )

                conversion = mpmathify( timeUnit[ 3 ] )
                unitConversionMatrix[ ( newUnit, unit ) ] = str( conversion )
                unitConversionMatrix[ ( unit, newUnit ) ] = str( fdiv( 1, conversion ) )

    unitOperators.update( newUnitOperators )

    # add new conversions for compound time units
    print( 'Adding new conversions for compound time units...' )

    newUnitConversions = { }

    for unit in unitOperators:
        unitInfo = unitOperators[ unit ]

        if unit[ -7 : ] == '-second':
            for timeUnit in timeUnits:
                newUnit = unit[ : -6 ] + timeUnit[ 0 ]

                factor = mpmathify( timeUnit[ 3 ] )

                for op1, op2 in unitConversionMatrix:
                    if op1 == unit:
                        oldConversion = mpmathify( unitConversionMatrix[ ( op1, op2 ) ] )
                        newUnitConversions[ ( newUnit, op2 ) ] = str( fmul( oldConversion, factor ) )

                        if unitInfo.abbrev != '':
                            newAliases[ unitInfo.abbrev[ : -1 ] + timeUnit[ 2 ] ] = newUnit
                    elif op2 == unit:
                        oldConversion = mpmathify( unitConversionMatrix[ ( op1, op2 ) ] )
                        newUnitConversions[ ( op1, newUnit ) ] = str( fdiv( oldConversion, factor ) )

                        if unitInfo.abbrev != '':
                            newAliases[ unitInfo.abbrev[ : -1 ] + timeUnit[ 2 ] ] = newUnit

    unitConversionMatrix.update( newUnitConversions )

    # make some more aliases
    print( 'Making some more aliases...' )

    newAliases.update( makeAliases( ) )

    #for op1, op2 in unitConversionMatrix:
    #    print( op1, op2, unitConversionMatrix[ ( op1, op2 ) ] )

    #print( )
    #print( )

    #for alias in newAliases:
    #    print( alias, newAliases[ alias ] )

    print( 'Saving everything...' )

    dataPath = os.path.abspath( os.path.realpath( __file__ ) + os.sep + '..' + os.sep + 'rpndata' )
    fileName = dataPath + os.sep + 'units.pckl.bz2'

    with contextlib.closing( bz2.BZ2File( fileName, 'wb' ) ) as pickleFile:
        pickle.dump( PROGRAM_VERSION, pickleFile )
        pickle.dump( basicUnitTypes, pickleFile )
        pickle.dump( unitOperators, pickleFile )
        pickle.dump( unitConversionMatrix, pickleFile )
        pickle.dump( newAliases, pickleFile )
        pickle.dump( compoundUnits, pickleFile )

    print( )
    print( '{:,} unit operators'.format( len( unitOperators ) ) )
    print( '{:,} unit conversions'.format( len( unitConversionMatrix ) ) )
    print( '{:,} aliases'.format( len( newAliases ) ) )
    print( '{:,} compound units'.format( len( compoundUnits ) ) )


#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    print( PROGRAM_NAME, PROGRAM_VERSION, '-', PROGRAM_DESCRIPTION )
    print( COPYRIGHT_MESSAGE )
    print( )

    initializeConversionMatrix( unitConversionMatrix )


#//******************************************************************************
#//
#//  __main__
#//
#//******************************************************************************

if __name__ == '__main__':
    main( )

