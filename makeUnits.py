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
PROGRAM_VERSION = '5.10.0'
PROGRAM_DESCRIPTION = 'RPN command-line calculator unit conversion data generator'
COPYRIGHT_MESSAGE = 'copyright (c) 2014, Rick Gutleber (rickg@his.com)'


#//******************************************************************************
#//
#//  basicUnitTypes
#//
#//  conversion from the basic unit types (length, mass, time, current, angle)
#//
#//******************************************************************************

basicUnitTypes = {
    'acceleration'              : 'length/time^2',
    'angle'                     : 'angle',
    'area'                      : 'length^2',
    'capacitance'               : 'current^2*time^4/mass*length^2',
    'charge'                    : 'current*time',
    'current'                   : 'current',
    'data_rate'                 : 'information_entropy/time',
    'electrical_conductance'    : 'time*current^2/mass*length^2',
    'electrical_resistance'     : 'mass*length^2/time*current^2',
    'electric_potential'        : 'mass*length^2/current*time^3',
    'energy'                    : 'mass*length^2/time^2',
    'force'                     : 'mass*length/time',
    'illuminance'               : 'luminous_intensity*angle^2/length^2',
    'inductance'                : 'electric_potential*time/current',
    'information_entropy'       : 'information_entropy',
    'length'                    : 'length',
    'luminance'                 : 'luminous_intensity/length^2',
    'luminous_flux'             : 'luminous_intensity*angle^2',
    'luminous_intensity'        : 'luminous_intensity',
    'magnetic_flux'             : 'electric_potential*time',
    'magnetic_flux_density'     : 'electric_potential*time/length^2',
    'mass'                      : 'mass',
    'power'                     : 'mass*length^2/time^3',
    'pressure'                  : 'mass/length*time^2',
    'radiation_absorbed_dose'   : 'radiation_absorbed_dose',
    'radiation_equivalent_dose' : 'radiation_equivalent_dose',
    'radiation_exposure'        : 'radiation_exposure',
    'radioactivity'             : 'radioactivity',
    'solid_angle'               : 'angle^2',
    'temperature'               : 'temperature',
    'time'                      : 'time',
    'velocity'                  : 'length/time',
    'volume'                    : 'length^3',
}


#//******************************************************************************
#//
#//  class UnitInfo
#//
#//******************************************************************************

class UnitInfo( ):
    def __init__( self, unitType, category, representation, plural, abbrev, aliases ):
        self.unitType = unitType
        self.category = category
        self.representation = representation
        self.plural = plural
        self.abbrev = abbrev
        self.aliases = aliases


#//******************************************************************************
#//
#//  unitOperators
#//
#//  unit name : unitType, category, representation, plural, abbrev, aliases
#//
#//******************************************************************************

unitOperators = {
    # acceleration
    'galileo' :
        UnitInfo( 'acceleration', 'CGS', 'galileo', 'galileos', '', [ ] ),

    'meter/second^2' :
        UnitInfo( 'acceleration', 'SI', 'meter/second^2', 'meters/second^2', 'm/s^2', [ ] ),

    'standard_gravity' :
        UnitInfo( 'acceleration', 'natural', 'standard_gravity', 'standard_gravities', 'G', [ ] ),

    # angle

    'arcminute' :
        UnitInfo( 'angle', 'mathematics', 'arcminute', 'arcminutes', 'arcmin', [ 'arcmins' ] ),

    'arcsecond' :
        UnitInfo( 'angle', 'mathematics', 'arcsecond', 'arcseconds', 'arcsec', [ 'arcsecs' ] ),

    'degree' :
        UnitInfo( 'angle', 'mathematics', 'degree', 'degrees', 'deg', [ ] ),

    'grad' :
        UnitInfo( 'angle', 'mathematics', 'grad', 'grads', '', [ 'gon', 'gons' ] ),

    'quadrant' :
        UnitInfo( 'angle', 'mathematics', 'quadrant', 'quadrants', '', [ ] ),

    'quintant' :
        UnitInfo( 'angle', 'mathematics', 'quintant', 'quintants', '', [ ] ),

    'octant' :
        UnitInfo( 'angle', 'mathematics', 'octant', 'octants', '', [ ] ),

    'radian' :
        UnitInfo( 'angle', 'SI', 'radian', 'radians', 'rad', [ ] ),

    'sextant' :
        UnitInfo( 'angle', 'mathematics', 'sextant', 'sextants', '', [ 'flat' ] ),

    # area

    'acre' :
        UnitInfo( 'area', 'traditional', 'acre', 'acres', 'ac', [ ] ),

    'are' :
        UnitInfo( 'area', 'SI', 'are', 'ares', 'a', [ ] ),

    'barn' :
        UnitInfo( 'area', 'science', 'barn', 'barns', '', [ ] ),

    'homestead':
        UnitInfo( 'area', 'traditional', 'homestead', 'homesteads', '', [ ] ),

    'outhouse' :
        UnitInfo( 'area', 'science', 'outhouse', 'outhouse', '', [ ] ),

    'rood' :
        UnitInfo( 'area', 'UK', 'rood', 'roods', '', [ 'farthingdale' ] ),

    'shed' :
        UnitInfo( 'area', 'science', 'shed', 'sheds', '', [ ] ),

    'square_meter' :
        UnitInfo( 'area', 'SI', 'meter^2', 'square_meters', 'm^2', [ 'meter^2', 'meters^2' ] ),

    'square_yard' :
        UnitInfo( 'area', 'traditional', 'yard^2', 'square_yards', 'sqyd', [ 'sqyd', 'yd^2', 'yard^2', 'yards^2' ] ),

    'township':
        UnitInfo( 'area', 'traditional', 'township', 'townships', '', [ ] ),

    # capacitance

    'coulomb/volt' :
        UnitInfo( 'capacitance', 'SI', 'coulomb/volt', 'coulombs/volt', 'C/V', [ 'coulomb/volts', 'coulombs/volts', 'C/volts', 'C/volt', 'coulomb/V', 'coulombs/V' ] ),

    'farad' :
        UnitInfo( 'capacitance', 'SI', 'farad', 'farads', 'F', [ ] ),

    'jar' :
        UnitInfo( 'capacitance', 'archaic', 'jar', 'jars', '', [ ] ),

    # charge

    'abcoulomb' :
        UnitInfo( 'charge', 'CGS', 'abcoulomb', 'abcoulombs', 'abC', [ ] ),

    'ampere-second' :
        UnitInfo( 'charge', 'SI', 'ampere*second', 'ampere*second', 'A/s', [ 'ampere/sec', 'ampere/s', 'amp/sec', 'amp/s', 'amps/sec', 'amps/s' ] ),

    'coulomb' :
        UnitInfo( 'charge', 'SI', 'coulomb', 'coulombs', 'C', [ ] ),

    'farad-volt' :
        UnitInfo( 'charge', 'SI', 'farad*volt', 'farad-volts', 'F*V', [ 'F/volt', 'F/volts', 'farad/volts', 'farads/volts', 'farad/V', 'farads/V' ] ),

    'franklin' :
        UnitInfo( 'charge', 'CGS', 'franklin', 'franklin', 'Fr', [ ] ),

    'electron_charge' :
        UnitInfo( 'charge', 'natural', 'electron_charge', 'electron_charges', '', [ ] ),

    'faraday' :
        UnitInfo( 'charge', 'natural', 'faraday', 'faradays', 'Fd', [ ] ),   # electron_charge * Avogradro's number!

    'planck_charge' :
        UnitInfo( 'charge', 'natural', 'planck_charge', 'planck_charges', '', [ ] ),

    'statcoulomb' :
        UnitInfo( 'charge', 'CGS', 'statcoulomb', 'statcoulombs', 'statC', [ ] ),

    # current

    'abampere' :
        UnitInfo( 'current', 'CGS', 'abampere', 'abamperes', 'abamp', [ 'abamp', 'abamps' ] ),

    'ampere' :
        UnitInfo( 'current', 'SI', 'ampere', 'amperes', 'A', [ 'amp', 'amps', 'galvat', 'galvats' ] ),

    'coulomb/second' :
        UnitInfo( 'current', 'SI', 'coulomb/second', 'coulombs/second', 'C/s', [ 'C/sec', 'coulomb/sec', 'coulombs/sec', 'coulomb/s', 'coulombs/s' ] ),

    # data_rate

    'bit/second' :
        UnitInfo( 'data_rate', 'computing', 'bit/second', 'bits/second', 'b/s', [ 'bit/s', 'bits/s', 'bit/sec', 'bits/sec' ] ),

    'byte/second' :
        UnitInfo( 'data_rate', 'computing', 'byte/second', 'bytes/second', 'B/s', [ 'byte/s', 'bytes/s' 'byte/sec', 'bytes/sec' ] ),

    # electric_potential

    'coulomb/farad' :
        UnitInfo( 'electric_potential', 'SI', 'coulomb/farad', 'coulombs/farad', 'C/F', [ 'coulomb/F', 'coulombs/F', 'C/farad', 'C/farads', 'coulombs/farads' ] ),

    'volt' :
        UnitInfo( 'electric_potential', 'SI', 'volt', 'volts', 'V', [ ] ),

    'watt/ampere' :
        UnitInfo( 'electric_potential', 'SI', 'watt/ampere', 'watts/ampere', 'W/A', [ 'watt/amp', 'watt/amps', 'watt/A', 'watts/amp', 'watts/amps', 'watts/A', 'W/amp', 'W/amps', 'W/ampere', 'W/amperes' ] ),

    # electrical_conductance

    'ampere/volt' :
        UnitInfo( 'electrical_conductance', 'SI', 'ampere/volt', 'amperes/volt', 'A/V', [ 'amp/V', 'amps/V', 'ampere/V', 'amperes/V', 'A/volt', 'amp/volt', 'amps/volt', 'A/volts', 'amp/volts', 'amps/volts', 'amperes/volts', ] ),

    'second^3-ampere^2/kilogram-meter^2':
        UnitInfo( 'electrical_conductance', 'SI', 'kilogram*meter^2/second^3*ampere^2', 'kilogram*meter^2/second^3*ampere^2', 'kg*m^2/s^3*A^2', [ ] ),

    'siemens' :
        UnitInfo( 'electrical_conductance', 'SI', 'siemens', 'siemens', 'S', [ 'mho' ] ),

    # electrical_resistance

    '1/siemens' :
        UnitInfo( 'electrical_resistance', 'SI', '1/siemens', '1/siemens', '1/S', [ '1/mho' ] ),

    'abohm' :
        UnitInfo( 'electrical_resistance', 'CGS', 'abohm', 'abohms', 'o', [ ] ),

    'german_mile' :
        UnitInfo( 'electrical_resistance', 'archaic', 'german_mile', 'german_mile', '', [ ] ),

    'jacobi' :
        UnitInfo( 'electrical_resistance', '', 'jacobi', 'jacobis', '', [ ] ),

    'joule-second/coulomb^2' :
        UnitInfo( 'electrical_resistance', 'SI', 'joule*second/coulomb^2', 'joule*second/coulomb^2', 'J*s/C^2', [ ] ),

    'joule/second-ampere^2' :
        UnitInfo( 'electrical_resistance', 'SI', 'joule/second*ampere^2', 'joule/second*ampere^2', 'J/s*A^2', [ ] ),

    'kilogram-meter^2/second^3-ampere^2' :
        UnitInfo( 'electrical_resistance', 'SI', 'kilogram*meter^2/second^3*ampere^2', 'kilogram*meter^2/second^3*ampere^2', 'kg*m^2/s^3*A^2', [ ] ),

    'matthiessen' :
        UnitInfo( 'electrical_resistance', '', 'matthiessen', 'matthiessens', '', [ ] ),

    'meter^2-kilogram/second-couloumb^2' :
        UnitInfo( 'electrical_resistance', 'SI', 'meter^2*kilogram/second*couloumb^2', 'meter^2*kilogram/second*couloumb^2', 'm^2*kg/s*C^2', [ ] ),

    'ohm' :
        UnitInfo( 'electrical_resistance', 'SI', 'ohm', 'ohms', 'O', [ ] ),

    'second/farad' :
        UnitInfo( 'electrical_resistance', 'SI', 'second/farad', 'second/farad', 's/F', [ ] ),

    'varley' :
        UnitInfo( 'electrical_resistance', '', 'varley', 'varleys', '', [ ] ),

    'volt/ampere' :
        UnitInfo( 'electrical_resistance', 'SI', 'volt/ampere', 'volts/ampere', 'V/A', [ 'volt/amp', 'volt/amps', 'volt/A', 'volts/amp', 'volts/amps', 'volts/A', 'V/amp', 'V/amps', 'V/ampere', 'V/amperes' ] ),

    'watt/ampere^2' :
        UnitInfo( 'electrical_resistance', 'SI', 'watt/ampere^2', 'watt/ampere^2', 'W/A^2', [ ] ),

    # energy

    'btu' :
        UnitInfo( 'energy', 'UK', 'btu', 'btus', '', [ 'BTU', 'BTUs' ] ),

    'calorie' :
        UnitInfo( 'energy', 'CGS', 'calorie', 'calories', 'cal', [ ] ),

    'electronvolt' :
        UnitInfo( 'energy', 'science', 'electronvolt', 'electronvolts', 'eV', [ 'electron-volt', 'electron-volts' ] ),

    'erg' :
        UnitInfo( 'energy', 'CGS', 'erg', 'ergs', '', [ ] ),

    'hartree' :
        UnitInfo( 'energy', 'science', 'hartree', 'hartrees', 'Ha', [ ] ),

    'horsepower-second' :
        UnitInfo( 'energy', '', 'horsepower*second', 'horsepower-seconds', 'hps', [ ] ),

    'joule' :
        UnitInfo( 'energy', 'SI', 'joule', 'joules', 'J', [ ] ),

    'kilogram-meter^2/second^2' :
        UnitInfo( 'energy', 'SI', 'kilogram*meter^2/second^2', 'kilogram*meter^2/second^2', 'kg*m^2/s^2', [ ] ),

    'newton-meter' :
        UnitInfo( 'energy', 'SI', 'newton*meter', 'newton-meters', 'N*m', [ ] ),

    'planck_energy' :
        UnitInfo( 'energy', 'natural', 'planck_energy', 'planck_energy', 'EP', [ ] ),

    'rydberg' :
        UnitInfo( 'energy', 'science', 'rydberg', 'rydbergs', 'Ry', [ ] ),

    'ton_of_TNT' :
        UnitInfo( 'energy', 'informal', 'ton_of_TNT', 'tons_of_TNT', 'tTNT', [ ] ),

    'watt-second' :
        UnitInfo( 'energy', 'SI', 'watt*second', 'watt-seconds', 'Ws', [ ] ),

    # force

    'dyne' :
        UnitInfo( 'force', 'CGS', 'dyne', 'dyne', 'dyn', [ ] ),

    'gram-force' :
        UnitInfo( 'force', 'CGS', 'gram-force', 'grams-force', 'g-m', [ ] ),

    'joule/meter' :
        UnitInfo( 'force', 'SI', 'joule/meter', 'joule/meter', 'J/m', [ ] ),

    'newton' :
        UnitInfo( 'force', 'SI', 'newton', 'newton', 'N', [ ] ),

    'pond' :
        UnitInfo( 'force', 'metric', 'pond', 'ponds', 'p', [ ] ),  # metric but not SI <shrug>

    'pound-foot/second^2' :
        UnitInfo( 'force', 'FPS', 'pound*foot/second^2', 'pound*foot/second^2', 'lb*ft/sec^2', [ ] ),

    'poundal' :
        UnitInfo( 'force', 'UK', 'poundal', 'poundals', 'pdl', [ ] ),

    'sthene' :
        UnitInfo( 'force', 'MTS', 'sthene', 'sthenes', 'sn', [ 'funal' ] ),

    # illuminance

    'footcandle' :
        UnitInfo( 'illuminance', 'FPS', 'footcandle', 'footcandles', 'fc', [ ] ),

    'lux' :
        UnitInfo( 'illuminance', 'SI', 'lux', 'lux', 'lx', [ ] ),

    'lumen/meter^2' :
        UnitInfo( 'illuminance', 'SI', 'lumen/meter^2', 'lumens/meter^2', 'lm/m^2', [ 'lm/square_meter', 'lumen/square_meter', 'lumens/square_meter', 'lumen/m^2', 'lumens/m^2' ] ),

    'lumen/foot^2' :
        UnitInfo( 'illuminance', 'FPS', 'lumen/foot^2', 'lumens/foot^2', 'lm/ft^2', [ 'lm/square_foot', 'lumen/square_foot', 'lumens/square_foot', 'lumen/ft^2', 'lumens/ft^2' ] ),

    'nox' :
        UnitInfo( 'illuminance', 'informal', 'nox', 'nox', '', [ ] ),

    'phot' :
        UnitInfo( 'illuminance', 'CGS', 'phot', 'phots', 'ph', [ ] ),   # CGS unit

    # inductance

    'henry' :
        UnitInfo( 'inductance', 'SI', 'henry', 'henries', 'H', [ ] ),

    'weber/ampere' :
        UnitInfo( 'inductance', 'SI', 'weber/ampere', 'webers/ampere', 'Wb/A', [ 'Wb/ampere', 'Wb/ampere', 'weber/A', 'webers/A', 'Wb/amp', 'weber/amp', 'webers/amp' ] ),

    # information_entropy

    'ban' :
        UnitInfo( 'information_entropy', 'IEC', 'ban', 'bans', '', [ 'hartley', 'hartleys', 'dit', 'dits' ] ),

    'bit' :
        UnitInfo( 'information_entropy', 'computing', 'bit', 'bits', 'b', [ 'shannon', 'shannons' ] ),

    'byte' :
        UnitInfo( 'information_entropy', 'computing', 'byte', 'bytes', 'B', [ 'octet', 'octets' ] ),

    'clausius' :
        UnitInfo( 'information_entropy', 'CGS', 'clausius', 'clausius', '', [ ] ),

    'dword' :
        UnitInfo( 'information_entropy', 'computing', 'dword', 'dwords', '', [ 'double_word', 'double_words', 'long_integer', 'long_integers' ] ),

    'joule/kelvin' :
        UnitInfo( 'information_entropy', 'SI', 'joule/kelvin', 'joules/kelvin', 'J/K', [ 'joule/K', 'joules/K' ] ),

    'nibble' :
        UnitInfo( 'information_entropy', 'computing', 'nibble', 'nibbles', '', [ 'nybble', 'nybbles' ] ),

    'nat' :
        UnitInfo( 'information_entropy', 'IEC', 'nat', 'nats', '', [ 'nip', 'nips', 'nepit', 'nepits' ] ),

    'nyp' :
        UnitInfo( 'information_entropy', 'computing', 'nyp', 'nyps', '', [ ] ),   # suggested by Donald Knuth

    'oword' :
        UnitInfo( 'information_entropy', 'computing', 'oword', 'owords', '', [ 'octaword', 'octawords' ] ),

    'qword' :
        UnitInfo( 'information_entropy', 'computing', 'qword', 'qwords', '', [ 'quad_word', 'quad_words', 'longlong_integer', 'longlong_integers' ] ),

    'trit' :
        UnitInfo( 'information_entropy', 'computing', 'trit', 'trits', '', [ ] ),

    'tryte' :
        UnitInfo( 'information_entropy', 'computing', 'tryte', 'trytes', '', [ ] ),

    'word' :
        UnitInfo( 'information_entropy', 'computing', 'word', 'words', '', [ 'short_integer', 'short_integers', 'wyde' ] ),  # 'wyde' suggested by Knuth

    # length

    'aln' :
        UnitInfo( 'length', 'archaic', 'aln', 'aln', '', [ ] ),

    'arpent' :
        UnitInfo( 'length', 'archaic', 'arpent', 'arpent', '', [ ] ),

    'angstrom' :
        UnitInfo( 'length', 'science', 'angstrom', 'angstroms', 'A', [ ] ),

    'astronomical_unit' :
        UnitInfo( 'length', 'science', 'astronomical_unit', 'astronomical_units', 'au', [ ] ),

    'barleycorn' :
        UnitInfo( 'length', 'UK', 'barleycorn', 'barleycorns', '', [ ] ),

    'caliber' :
        UnitInfo( 'length', 'US', 'caliber', 'caliber', '', [ 'calibre' ] ),

    'chain' :
        UnitInfo( 'length', 'UK', 'chain', 'chains', '', [ ] ),

    'cubit' :
        UnitInfo( 'length', 'UK', 'cubit', 'cubits', '', [ ] ),

    'ell' :
        UnitInfo( 'length', 'UK', 'ell', 'ell', '', [ ] ),

    'famn' :
        UnitInfo( 'length', 'archaic', 'famn', 'famn', '', [ ] ),

    'farshimmelt_potrzebie' :
        UnitInfo( 'length', 'Potrzebie', 'farshimmelt_potrzebie', 'farshimmelt potrzebies', 'fpz', [ 'far-potrzebie' ] ),

    'fathom' :
        UnitInfo( 'length', 'traditional', 'fathom', 'fathom', 'fath', [ ] ),

    'finger' :
        UnitInfo( 'length', 'traditional', 'finger', 'finger', '', [ ] ),

    'fingerbreadth' :
        UnitInfo( 'length', 'archaic', 'fingerbreadth', 'fingerbreadths', '', [ 'fingersbreadth' ] ),

    'foot' :
        UnitInfo( 'length', 'traditional', 'foot', 'feet', 'ft', [ ] ),

    'furlong' :
        UnitInfo( 'length', 'traditional', 'furlong', 'furlongs', '', [ ] ),

    'furshlugginer_potrzebie' :
        UnitInfo( 'length', 'Potrzebie', 'furshlugginer_potrzebie', 'furshlugginer potrzebies', 'Fpz', [ 'Fur-potrzebie' ] ),

    'greek_cubit' :
        UnitInfo( 'length', 'archaic', 'greek_cubit', 'greek_cubits', '', [ ] ),

    'gutenberg' :
        UnitInfo( 'length', 'typography', 'gutenberg', 'gutenbergs', '', [ ] ),

    'hand' :
        UnitInfo( 'length', 'traditional', 'hand', 'hands', '', [ ] ),

    'handbreadth' :
        UnitInfo( 'length', 'archaic', 'handbreadth', 'handbreadths', '', [ 'handsbreadth' ] ),

    'inch' :
        UnitInfo( 'length', 'traditional', 'inch', 'inches', 'in', [ ] ),

    'long_reed' :
        UnitInfo( 'length', 'archaic', 'long_reed', 'long_reeds', '', [ ] ),

    'long_cubit' :
        UnitInfo( 'length', 'archaic', 'long_cubit', 'long_cubits', '', [ ] ),

    'ken' :
        UnitInfo( 'length', 'archaic', 'ken', 'ken', '', [ ] ),

    'kyu' :
        UnitInfo( 'length', 'typography', 'kyu', 'kyus', '', [ 'Q' ] ),

    'league' :
        UnitInfo( 'length', 'traditional', 'league', 'leagues', '', [ ] ),

    'light-second' :
        UnitInfo( 'length', 'science', 'light*second', 'light-seconds', '', [ 'light-second' ] ),

    'light-year' :
        UnitInfo( 'length', 'science', 'light-year', 'light-years', 'ly', [ ] ),

    'link' :
        UnitInfo( 'length', 'traditional', 'link', 'link', '', [ ] ),

    'marathon' :
        UnitInfo( 'length', 'archaic', 'marathon', 'marathons', '', [ ] ),

    'meter' :
        UnitInfo( 'length', 'SI', 'meter', 'meters', 'm', [ ] ),

    'micron' :
        UnitInfo( 'length', 'US', 'micron', 'microns', '', [ ] ),

    'mil' :
        UnitInfo( 'length', 'traditional', 'mil', 'mils', '', [ 'thou' ] ),

    'mile' :
        UnitInfo( 'length', 'traditional', 'mile', 'miles', 'mi', [ ] ),

    'nail' :
        UnitInfo( 'length', 'archaic', 'nail', 'nail', '', [ ] ),

    'nautical_mile' :
        UnitInfo( 'length', 'nautical', 'nautical_mile', 'nautical_miles', '', [ ] ),

    'parsec' :
        UnitInfo( 'length', 'science', 'parsec', 'parsec', 'pc', [ ] ),

    'perch' :
        UnitInfo( 'length', 'archaic', 'perch', 'perches', '', [ 'pole', 'poles' ] ),

    'pica' :
        UnitInfo( 'length', 'typography', 'pica', 'pica', '', [ 'cicero' ] ),

    'planck_length' :
        UnitInfo( 'length', 'science', 'planck_length', 'planck_length', 'lP', [ ] ),

    'point' :
        UnitInfo( 'length', 'typography', 'point', 'points', '', [ ] ),

    'poppyseed' :
        UnitInfo( 'length', 'traditional', 'poppyseed', 'poppyseeds', '', [ ] ),

    'reed' :
        UnitInfo( 'length', 'archaic', 'reed', 'reeds', '', [ ] ),

    'rod' :
        UnitInfo( 'length', 'traditional', 'rod', 'rods', 'rd', [ ] ),

    'rope' :
        UnitInfo( 'length', 'archaic', 'rope', 'ropes', '', [ ] ),

    'potrzebie' :
        UnitInfo( 'length', 'Potrzebie', 'potrzebie', 'potrzebies', 'pz', [ ] ),

    'smoot' :
        UnitInfo( 'length', 'informal', 'smoot', 'smoots', '', [ ] ),

    'span' :
        UnitInfo( 'length', 'traditional', 'span', 'spans', '', [ 'breadth' ] ),

    'twip' :
        UnitInfo( 'length', 'computing', 'twip', 'twips', '', [ ] ),

    'yard' :
        UnitInfo( 'length', 'traditional', 'yard', 'yards', 'yd', [ ] ),

    # luminance

    'apostilb' :
        UnitInfo( 'luminance', 'CGS', 'apostilb', 'apostilbs', '', [ 'blondel' ] ),

    'bril' :
        UnitInfo( 'luminance', '', 'bril', 'brils', '', [ ] ),

    'candela/meter^2' :
        UnitInfo( 'luminance', 'SI', 'candela/meter^2', 'candelas/meter^2', 'cd/m^2', [ 'candela/m^2', 'candelas/m^2', 'candela/square_meter', 'candelas/square_meter', 'cd/square_meter' ] ),

    'footlambert' :
        UnitInfo( 'luminance', '', 'footlambert', 'footlamberts', 'fL', [ 'foot-lambert' ] ),

    'lambert' :
        UnitInfo( 'luminance', 'CGS', 'lambert', 'lamberts', 'L', [ ] ),

    'nit' :
        UnitInfo( 'luminance', '', 'nit', 'nit', '', [ 'meterlambert', 'meter-lambert', 'meterlamberts', 'meter-lamberts' ] ),

    'skot' :
        UnitInfo( 'luminance', '', 'skot', 'skots', '', [ ] ),

    'stilb' :
        UnitInfo( 'luminance', 'CGS', 'stilb', 'stilbs', 'sb', [ ] ),

    # luminous_flux

    'lumen' :
        UnitInfo( 'luminous_flux', 'SI', 'lumen', 'lumens', 'lm', [ ] ),

    'candela-steradian' :
        UnitInfo( 'luminous_flux', 'SI', 'lumen', 'lumens', 'lm', [ ] ),

    # luminous_intensity

    'candela' :
        UnitInfo( 'luminous_intensity', 'SI', 'candela', 'candelas', 'cd', [ ] ),

    'hefnerkerze' :
        UnitInfo( 'luminous_intensity', 'archaic', 'hefnerkerze', 'hefnerkerze', 'HK', [ ] ),

    # magnetic_flux

    'maxwell' :
        UnitInfo( 'magnetic_flux', 'CGS', 'maxwell', 'maxwells', 'Mx', [ 'line' ] ),

    'volt-second' :
        UnitInfo( 'magnetic_flux', 'SI', 'volt*second', 'volts*seconds', 'V*s', [ ] ),

    'weber' :
        UnitInfo( 'magnetic_flux', 'SI', 'weber', 'webers', 'Wb', [ ] ),

    # magnetic_flux_density

    'gauss' :
        UnitInfo( 'magnetic_flux_density', 'CGS', 'gauss', 'gauss', '', [ ] ),

    'kilogram/ampere-second^2' :
        UnitInfo( 'magnetic_flux_density', 'SI', 'kilogram/ampere*second^2', 'kilogram/ampere*second^2', 'kg/A*s^2', [ ] ),

    'maxwell/centimeter^2' :
        UnitInfo( 'magnetic_flux_density', 'CGS', 'maxwell/centimeter^2', 'maxwells/centimeter^2', 'Mx/cm^2', [ 'maxwell/cm^2', 'maxwells/cm^2', 'Mx/centimeter^2', 'Mx/square_centimeter', 'Mx/square_cm', 'maxwell/square_centimeter', 'maxwells/square_centimeter', 'maxwell/square_cm', 'maxwells/square_cm' ] ),  # CGS

    'tesla' :
        UnitInfo( 'magnetic_flux_density', 'SI', 'tesla', 'teslas', 'T', [ ] ),

    'weber/meter^2' :
        UnitInfo( 'magnetic_flux_density', 'SI', 'weber/meter^2', 'webers/meter^2', 'Wb/m^2', [ ] ),

    # mass

    'blintz' :
        UnitInfo( 'mass', 'Potrzebie', 'blintz', 'blintzes', 'b', [ ] ),

    'carat' :
        UnitInfo( 'mass', '', 'carat', 'carats', 'kt', [ 'karat', 'karats' ] ),

    'farshimmelt_blintz' :
        UnitInfo( 'mass', 'Potrzebie', 'farshimmelt_blintz', 'farshimmelt blintzes', 'fb', [ 'far-blintz' ] ),

    'furshlugginer_blintz' :
        UnitInfo( 'mass', 'Potrzebie', 'furshlugginer_blintz', 'furshlugginer blintzes', 'Fb', [ 'Fur-blintz' ] ),

    'grain' :
        UnitInfo( 'mass', 'traditional', 'grain', 'grains', 'gr', [ ] ),

    'gram' :
        UnitInfo( 'mass', 'SI', 'gram', 'grams', 'g', [ ] ),

    'ounce' :
        UnitInfo( 'mass', 'traditional', 'ounce', 'ounces', 'oz', [ ] ),

    'pennyweight' :
        UnitInfo( 'mass', 'UK', 'pennyweight', 'pennyweights', 'dwt', [ ] ),

    'planck_mass' :
        UnitInfo( 'mass', 'science', 'planck_mass', 'planck_masses', 'mP', [ ] ),

    'pound' :
        UnitInfo( 'mass', 'US', 'pound', 'pounds', 'lb', [ ] ),

    'quintal' :
        UnitInfo( 'mass', '', 'quintal', 'quintals', 'q', [ ] ),

    'sheet' :
        UnitInfo( 'mass', '', 'sheet', 'sheet', '', [ ] ),

    'slug' :
        UnitInfo( 'mass', 'FPS', 'slug', 'slug', '', [ 'geepound', 'gee-pound', 'geepounds', 'gee-pounds' ] ),

    'stone' :
        UnitInfo( 'mass', 'UK', 'stone', 'stone', '', [ ] ),

    'ton' :
        UnitInfo( 'mass', 'traditional', 'ton', 'tons', '', [ ] ),

    'tonne' :
        UnitInfo( 'mass', 'MTS', 'tonne', 'tonnes', '', [ ] ),

    'troy_ounce' :
        UnitInfo( 'mass', '', 'troy_ounce', 'troy_ounces', '', [ ] ),

    'troy_pound' :
        UnitInfo( 'mass', '', 'troy_pound', 'troy_pounds', '', [ ] ),

    'wey' :
        UnitInfo( 'mass', 'archaic', 'wey', 'weys', '', [ ] ),   # UK

    # power

    'erg/second' :
        UnitInfo( 'power', 'CGS', 'erg/second', 'ergs/second', 'erg/s', [ 'ergs/s' ] ),

    'horsepower' :
        UnitInfo( 'power', '', 'horsepower', 'horsepower', 'hp', [ ] ),

    'joule/second' :
        UnitInfo( 'power', 'SI', 'joule/second', 'joules/second', 'J/s', [ ] ),

    'kilogram-meter^2/second^3' :
        UnitInfo( 'power', 'SI', 'kilogram*meter^2/second^3', 'kilogram*meter^2/second^3', 'kg*m^2/s^3', [ ] ),

    'newton-meter/second' :
        UnitInfo( 'power', 'SI', 'newton*meter/second', 'newton*meter/second', 'N*m/s', [ ] ),

    'poncelet' :
        UnitInfo( 'power', '', 'poncelet', 'poncelets', 'p', [ ] ),

    'watt' :
        UnitInfo( 'power', 'SI', 'watt', 'watts', 'W', [ ] ),

    # pressure

    'atmosphere' :
        UnitInfo( 'pressure', 'natural', 'atmosphere', 'atmospheres', 'atm', [ ] ),

    'bar' :
        UnitInfo( 'pressure', '', 'bar', 'bar', '', [ ] ),

    'barye' :
        UnitInfo( 'pressure', 'CGS', 'barye', 'baryes', '', [ ] ),

    'mmHg' :
        UnitInfo( 'pressure', '', 'mmHg', 'mmHg', '', [ ] ),

    'newton/meter^2' :
        UnitInfo( 'pressure', 'SI', 'newton/meter^2', 'newtons/meter^2', 'N/m^2', [ ] ),

    'pascal' :
        UnitInfo( 'pressure', 'SI', 'pascal', 'pascal', 'Pa', [ ] ),

    'pieze' :
        UnitInfo( 'pressure', 'MTS', 'pieze', 'pieze', '', [ ] ),

    'psi' :
        UnitInfo( 'pressure', 'FPS', 'pound/inch^2', 'pounds/inch^2', 'psi', [ 'lb/in^2' ] ),

    'torr' :
        UnitInfo( 'pressure', '', 'torr', 'torr', '', [ ] ),

    # radioactivity

    'becquerel' :
        UnitInfo( 'radioactivity', 'SI', 'becquerel', 'becquerels', 'Bq', [ ] ),

    'curie' :
        UnitInfo( 'radioactivity', 'obsolete', 'curie', 'curie', 'Ci', [ ] ),

    'rutherford' :
        UnitInfo( 'radioactivity', 'obsolete', 'rutherford', 'rutherfords', 'rd', [ ] ),

    # radiation_absorbed_dose
    'gray' :
        UnitInfo( 'radiation_absorbed_dose', 'SI', 'gray', 'grays', 'Gy', [ ] ),

    'rad' :
        UnitInfo( 'radiation_absorbed_dose', 'CGS', 'rad', 'rads', '', [ ] ),

    # radiation_exposure
    'coulomb/kilogram' :
        UnitInfo( 'radiation_exposure', 'SI', 'coulomb/kilogram', 'coulombs/kilogram', 'C/kg', [ ] ),

    'roentgen' :
        UnitInfo( 'radiation_exposure', '', 'roentgen', 'roentgens', 'R', [ ] ),

    # solid_angle
    'square_arcminute' :
        UnitInfo( 'solid_angle', 'mathematics', 'arcminute^2', 'arcminutes^2', 'arcmin^2', [ 'square_arcminutes', 'sqarcmin', 'sqarcmins', 'arcmins^2' ] ),

    'square_arcsecond' :
        UnitInfo( 'solid_angle', 'mathematics', 'arcsecond^2', 'arcseconds^2', 'arcsec^2', [ 'square_arcseconds', 'sqarcsec', 'sqarcsecs', 'arcsecs^2' ] ),

    'square_degree' :
        UnitInfo( 'solid_angle', 'mathematics', 'degree^2', 'degrees^2', 'deg^2', [ 'square_degrees', 'sqdeg' ] ),

    'square_octant' :
        UnitInfo( 'solid_angle', 'mathematics', 'octant^2', 'octants^2', '', [ 'square_octants', 'sqoctant', 'sqoctants' ] ),

    'square_quadrant' :
        UnitInfo( 'solid_angle', 'mathematics', 'quadrant^2', 'quadrants^2', '', [ 'square_quadrants', 'sqquadrant', 'sqquadrants' ] ),

    'square_quintant' :
        UnitInfo( 'solid_angle', 'mathematics', 'quintant^2', 'quintants^2', '', [ 'square_quintants', 'sqquintant', 'sqquintants' ] ),

    'square_sextant' :
        UnitInfo( 'solid_angle', 'mathematics', 'sextant^2', 'sextants^2', '', [ 'square_sextants', 'sqsextant', 'sqsextants' ] ),

    'square_grad' :
        UnitInfo( 'solid_angle', 'mathematics', 'grad^2', 'grads^2', '', [ 'square_grads', 'sqgrad', 'square_gon', 'square_gons', 'grad^2', 'grads^2', 'gon^2', 'gons^2' ] ),

    'steradian' :
        UnitInfo( 'solid_angle', 'SI', 'steradian', 'steradian', '', [ 'square_radian', 'square_radians', 'radian^2', 'radians^2', 'rad^2' ] ),

    # temperature

    'celsius' :
        UnitInfo( 'temperature', 'SI', 'celsius', 'degrees celsius', '', [ 'centigrade', 'degC' ] ),

    'degrees_newton' :
        UnitInfo( 'temperature', 'archaic', 'degrees_newton', 'degrees newton', '', [ 'newton_degree', 'newton_degrees', 'degN' ] ),

    'delisle' :
        UnitInfo( 'temperature', 'archaic', 'delisle', 'degrees delisle', 'De', [ 'degDe' ] ),

    'fahrenheit' :
        UnitInfo( 'temperature', 'US', 'fahrenheit', 'degrees fahrenheit', '', [ 'fahr', 'degF' ] ),

    'kelvin' :
        UnitInfo( 'temperature', 'SI', 'kelvin', 'degrees kelvin', 'K', [ 'degK' ] ),

    'rankine' :
        UnitInfo( 'temperature', 'archaic', 'rankine', 'degrees rankine', 'R', [ 'degR' ] ),

    'reaumur' :
        UnitInfo( 'temperature', 'archaic', 'reaumur', 'degrees reaumur', 'Re', [ 'degRe' ] ),

    'romer' :
        UnitInfo( 'temperature', 'archaic', 'romer', 'degrees romer', 'Ro', [ 'defRo' ] ),

    # time
    'century' :
        UnitInfo( 'time', 'traditional', 'century', 'centuries', '', [ ] ),

    'clarke' :
        UnitInfo( 'time', 'Potrzebie', 'clarke', 'clarkes', '', [ ] ),

    'cowznofski' :
        UnitInfo( 'time', 'Potrzebie', 'cowznofski', 'cowznofskis', '', [ ] ),

    'day' :
        UnitInfo( 'time', 'traditional', 'day', 'days', '', [ ] ),

    'decade' :
        UnitInfo( 'time', 'traditional', 'decade', 'decades', '', [ ] ),

    'fortnight' :
        UnitInfo( 'time', 'traditional', 'fortnight', 'fortnights', '', [ ] ),

    'gregorian_year' :
        UnitInfo( 'time', 'traditional', 'gregorian_year', 'gregorian_years', '', [ '' ] ),

    'hour' :
        UnitInfo( 'time', 'traditional', 'hour', 'hours', 'hr', [ ] ),

    'kovac' :
        UnitInfo( 'time', 'Potrzebie', 'kovac', 'kovacs', '', [ ] ),

    'jiffy' :
        UnitInfo( 'time', 'computing', 'jiffy', 'jiffies', '', [ ] ),

    'lunar-day' :
        UnitInfo( 'time', 'science', 'lunar-day', 'lunar-days', '', [ 'tidal-day', 'tidal-days' ] ),

    'martin' :
        UnitInfo( 'time', 'Potrzebie', 'martin', 'martins', '', [ ] ),

    'microcentury' :
        UnitInfo( 'time', 'computing', 'microcentury', 'microcenturies', '', [ ] ),

    'microfortnight' :
        UnitInfo( 'time', 'computing', 'microfortnight', 'microfortnights', '', [ ] ),

    'mingo' :
        UnitInfo( 'time', 'Potrzebie', 'mingo', 'mingoes', '', [ ] ),

    'minute' :
        UnitInfo( 'time', 'traditional', 'minute', 'minutes', '', [ ] ),   # 'min' is already an operator

    'nanocentury' :
        UnitInfo( 'time', 'computing', 'nanocentury', 'nanocenturies', '', [ ] ),

    'planck_time' :
        UnitInfo( 'time', 'science', 'planck_time', 'x planck_time', 'tP', [ ] ),

    'second' :
        UnitInfo( 'time', 'SI', 'second', 'seconds', '', [ ] ),   # 'sec' is already an operator

    'shake' :
        UnitInfo( 'time', 'science', 'shake', 'shakes', '', [ ] ),

    'sigma' :
        UnitInfo( 'time', '', 'sigma', 'sigmas', '', [ ] ),

    'siderial_day' :
        UnitInfo( 'time', 'science', 'siderial_day', 'siderial_days', '', [ ] ),

    'siderial_year' :
        UnitInfo( 'time', 'science', 'siderial_year', 'siderial_years', '', [ ] ),

    'svedberg' :
        UnitInfo( 'time', 'non=SI', 'svedberg', 'svedbergs', '', [ ] ),

    'tropical_year' :
        UnitInfo( 'time', 'science', 'tropical_year', 'tropical_years', '', [ 'solar_year', 'solar_years' ] ),

    'week' :
        UnitInfo( 'time', 'traditional', 'week', 'weeks', 'wk', [ 'sennight' ] ),

    'wolverton' :
        UnitInfo( 'time', 'Potrzebie', 'wolverton', 'wolvertons', '', [ ] ),

    'wood' :
        UnitInfo( 'time', 'Potrzebie', 'wood', 'woods', '', [ ] ),

    'year' :
        UnitInfo( 'time', 'traditional', 'year', 'years', '', [ 'julian_year', 'julian_years' ] ),

    # velocity

    'meter/second' :
        UnitInfo( 'velocity', 'SI', 'meter/second', 'meters per second', 'm/s', [ ] ),

    'knot' :
        UnitInfo( 'velocity', 'nautical', 'knot', 'knots', 'kt', [ ] ),

    'light' :
        UnitInfo( 'velocity', 'natural', 'light', 'x_speed_of_light', 'c', [ 'speed_of_light' ] ),

    'mach' :
        UnitInfo( 'velocity', '', 'mach', 'mach', '', [ ] ),

    # volume

    'acre-foot' :
        UnitInfo( 'volume', 'US', 'acre*foot', 'acre_feet', 'ac*ft', [ ] ),

    'balthazar' :
        UnitInfo( 'volume', 'wine', 'balthazar', 'balthazars', '', [ ] ),

    'barrel' :
        UnitInfo( 'volume', '', 'barrel', 'barrels', '', [ ] ),

    'bucket' :
        UnitInfo( 'volume', 'imperial', 'bucket', 'buckets', '', [ ] ),

    'bushel' :
        UnitInfo( 'volume', 'imperial', 'bushel', 'bushels', 'bu', [ ] ),

    'butt' :
        UnitInfo( 'volume', 'wine', 'butt', 'butts', '', [ ] ),

    'chopine' :
        UnitInfo( 'volume', 'wine', 'chopine', 'chopines', '', [ ] ),

    'clavelin' :
        UnitInfo( 'volume', 'wine', 'clavelin', 'clavelins', '', [ ] ),

    'cord' :
        UnitInfo( 'volume', 'traditional', 'cord', 'cord', '', [ ] ),

    'cubic_inch' :
        UnitInfo( 'volume', 'traditional', 'inch^3', 'cubic_inches', 'cuin', [ 'in^3', 'inch^3', 'inches^3' ] ),

    'cubic_foot' :
        UnitInfo( 'volume', 'traditional', 'foot^3', 'cubic_feet', 'cuft', [ 'ft^3', 'foot^3', 'feet^3' ] ),

    'cubic_meter' :
        UnitInfo( 'volume', 'SI', 'meter^3', 'cubic_meters', 'm^3', [ 'meter^3', 'meters^3' ] ),

    'cup' :
        UnitInfo( 'volume', 'cooking', 'cup', 'cups', '', [ ] ),

    'dash' :
        UnitInfo( 'volume', 'cooking', 'dash', 'dashes', '', [ ] ),

    'demi' :
        UnitInfo( 'volume', 'wine', 'demi', 'demis', '', [ ] ),

    'dessertspoon' :
        UnitInfo( 'volume', 'cooking', 'dessertspoon', 'dessertspoons', '', [ ] ),

    'dram' :
        UnitInfo( 'volume', 'UK', 'dram', 'drams', '', [ ] ),

    'dry_barrel' :
        UnitInfo( 'volume', 'US', 'dry_barrel', 'dry_barrels', '', [ ] ),

    'dry_gallon' :
        UnitInfo( 'volume', 'US', 'dry_gallon', 'dry_gallons', '', [ ] ),

    'dry_pint' :
        UnitInfo( 'volume', 'US', 'dry_pint', 'dry_pints', '', [ ] ),

    'dry_quart' :
        UnitInfo( 'volume', 'US', 'dry_quart', 'dry_quarts', '', [ ] ),

    'fifth' :
        UnitInfo( 'volume', 'wine', 'fifth', 'fifths', '', [ ] ),

    'firkin' :
        UnitInfo( 'volume', 'UK', 'firkin', 'firkins', '', [ ] ),

    'fluid_dram' :
        UnitInfo( 'volume', '', 'fluid_dram', 'fluid_drams', '', [ 'fluidram', 'fluidrams', 'fluid_drachm', 'fluid_drachms' ] ),

    'fluid_ounce' :
        UnitInfo( 'volume', '', 'fluid_ounce', 'fluid_ounces', '', [ ] ),

    'fluid_scruple' :
        UnitInfo( 'volume', '', 'fluid_scruple', 'fluid_scruples', '', [ 'scruple', 'scruples' ] ),

    'farshimmelt_ngogn' :
        UnitInfo( 'volume', 'Potrzebie', 'farshimmelt_ngogn', 'farshimmelt ngogns', 'fn', [ 'far-ngogn' ] ),

    'furshlugginer_ngogn' :
        UnitInfo( 'volume', 'Potrzebie', 'furshlugginer_ngogn', 'furshlugginer ngogns', 'Fn', [ 'Fur-ngogn' ] ),

    'gallon' :
        UnitInfo( 'volume', 'traditional', 'gallon', 'gallons', 'gal', [ ] ),

    'gill' :
        UnitInfo( 'volume', 'traditional', 'gill', 'gills', '', [ ] ),

    'goliath' :
        UnitInfo( 'volume', 'wine', 'goliath', 'goliaths', '', [ 'primat' ] ),

    'hogshead' :
        UnitInfo( 'volume', 'traditional', 'hogshead', 'hogsheads', '', [ ] ),

    'imperial' :
        UnitInfo( 'volume', 'wine', 'imperial', 'imperials', '', [ ] ),

    'jennie' :
        UnitInfo( 'volume', 'wine', 'jennie', 'jennies', '', [ ] ),

    'jeroboam' :
        UnitInfo( 'volume', 'wine', 'jeroboam', 'jeroboams', '', [ 'double_magnum' ] ),

    'liter' :
        UnitInfo( 'volume', 'SI', 'liter', 'liters', 'l', [ ] ),

    'magnum' :
        UnitInfo( 'volume', 'wine', 'magnum', 'magnums', '', [ ] ),

    'marie_jeanne' :
        UnitInfo( 'volume', 'wine', 'marie_jeanne', 'marie_jeannes', '', [ ] ),

    'melchior' :
        UnitInfo( 'volume', 'wine', 'melchior', 'melchiors', '', [ ] ),

    'melchizedek' :
        UnitInfo( 'volume', 'wine', 'melchizedek', 'melchizedeks', '', [ ] ),

    'methuselah' :
        UnitInfo( 'volume', 'wine', 'methuselah', 'methuselahs', '', [ ] ),

    'minim':
        UnitInfo( 'volume', '', 'minim', 'minims', 'gtt', [ 'drop' ] ),

    'mordechai' :
        UnitInfo( 'volume', 'wine', 'mordechai', 'mordechais', '', [ ] ),

    'nebuchadnezzar' :
        UnitInfo( 'volume', 'wine', 'nebuchadnezzar', 'nebuchadnezzars', '', [ ] ),

    'ngogn' :
        UnitInfo( 'volume', 'Potrzebie', 'ngogn', 'ngogns', 'n', [ ] ),

    'oil_barrel' :
        UnitInfo( 'volume', '', 'oil_barrel', 'oil_barrels', 'bbl', [ ] ),

    'peck' :
        UnitInfo( 'volume', 'imperial', 'peck', 'pecks', 'pk', [ ] ),

    'piccolo' :
        UnitInfo( 'volume', 'wine', 'piccolo', 'piccolos', '', [ ] ),

    'pinch' :
        UnitInfo( 'volume', 'US', 'pinch', 'pinches', '', [ ] ),

    'pint' :
        UnitInfo( 'volume', 'US', 'pint', 'pints', 'pt', [ ] ),

    'quart' :
        UnitInfo( 'volume', 'US', 'quart', 'quarts', 'qt', [ ] ),

    'rehoboam' :
        UnitInfo( 'volume', 'wine', 'rehoboam', 'rehoboams', '', [ ] ),

    'salmanazar' :
        UnitInfo( 'volume', 'wine', 'salmanazar', 'salmanazars', '', [ ] ),

    'smidgen' :
        UnitInfo( 'volume', 'cooking', 'smidgen', 'smidgens', '', [ ] ),

    'solomon' :
        UnitInfo( 'volume', 'wine', 'solomon', 'solomons', '', [ ] ),

    'sovereign' :
        UnitInfo( 'volume', 'wine', 'sovereign', 'sovereigns', '', [ ] ),

    'standard' :
        UnitInfo( 'volume', 'wine', 'standard', 'standards', '', [ ] ),

    'stere' :
        UnitInfo( 'volume', '', 'stere', 'steres', 'st', [ ] ),

    'tablespoon' :
        UnitInfo( 'volume', 'US', 'tablespoon', 'tablespoons', 'tbsp', [ ] ),

    'teaspoon' :
        UnitInfo( 'volume', 'US', 'teaspoon', 'teaspoons', 'tsp', [ ] ),

    'tenth' :
        UnitInfo( 'volume', 'wine', 'tenth', 'tenths', '', [ ] ),

    'tun' :
        UnitInfo( 'volume', '', 'tun', 'tuns', '', [ ] ),
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
    ( 'ampere',         'amperes',          'A',    [ 'amp' ], [ 'amps' ] ),
    ( 'are',            'ares',             'a',    [ ], [ ] ),
    ( 'becquerel',      'becquerels',       'Bq',   [ ], [ ] ),
    ( 'blintz',         'blintzes',         'bl',   [ ], [ ] ),
    ( 'coulomb',        'coulombs',         'C',    [ ], [ ] ),
    ( 'calorie',        'calories',         'cal',  [ ], [ ] ),
    ( 'electronvolt',   'electronvolts',    'eV',   [ ], [ ] ),
    ( 'farad',          'farad',            'F',    [ ], [ ] ),
    ( 'gram',           'grams',            'g',    [ 'gramme' ], [ 'grammes' ] ),
    ( 'gram-force',     'grams-force',      'gf',   [ 'gramme-force' ], [ 'grammes-force' ] ),
    ( 'henry',          'henries',          'H',    [ ], [ ] ),
    ( 'joule',          'joules',           'J',    [ ], [ ] ),
    ( 'kelvin',         'kelvins',          'K',    [ ], [ ] ),
    ( 'liter',          'liters',           'l',    [ 'litre' ], [ 'litres' ] ),
    ( 'light-year',     'light-years',      'ly',   [ ], [ ] ),
    ( 'lux',            'lux',              'lx',   [ ], [ ] ),
    ( 'meter',          'meters',           'm',    [ 'metre' ], [ 'metres' ] ),
    ( 'newton',         'newtons',          'N',    [ ], [ ] ),
    ( 'ngogn',          'ngogns',           'n',    [ ], [ ] ),
    ( 'ohm',            'ohms',             'O',    [ ], [ ] ),
    ( 'parsec',         'parsecs',          'pc',   [ ], [ ] ),
    ( 'pascal',         'pascals',          'Pa',   [ ], [ ] ),
    ( 'pond',           'ponds',            'p',    [ ], [ ] ),
    ( 'potrzebie',      'potrzebies',       'pz',   [ ], [ ] ),
    ( 'second',         'seconds',          's',    [ ], [ ] ),
    ( 'stere',          'steres',           'st',   [ ], [ ] ),
    ( 'tesla',          'teslas',           'T',    [ ], [ ] ),
    ( 'ton_of_TNT',     'tons_of_TNT',      'tTNT', [ ], [ ] ),
    ( 'volt',           'volt',             'V',    [ ], [ ] ),
    ( 'watt',           'watts',            'W',    [ ], [ ] ),
    ( 'watt-second',    'watt-seconds',     'Ws',   [ ], [ ] ),
]


#//******************************************************************************
#//
#//  dataUnits
#//
#//  ... or any units that should get the SI prefixes (positive powers of 10)
#//  and the binary prefixes
#//
#//  ( name, plural name, abbreviation, aliases, plural aliases )
#//
#//******************************************************************************

dataUnits = [
    ( 'bit',            'bits',             'b',    [ ], [ ] ),
    ( 'bit/second',     'bits/second',      'bps',  [ ], [ ] ),
    ( 'byte',           'bytes',            'B',    [ ], [ ] ),
    ( 'byte/second',    'bytes/second',     'Bps',  [ ], [ ] ),
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
    ( 'year',       'years',        'y',        '31557600' ),   # Julian year == 365.25 days
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
    ( 'micro',      'u',      '-6' ),  # it's really a mu
    ( 'nano',       'n',      '-9' ),
    ( 'pico',       'p',      '-12' ),
    ( 'femto',      'f',      '-15' ),
    ( 'atto',       'a',      '-18' ),
    ( 'zepto',      'z',      '-21' ),
    ( 'yocto',      'y',      '-24' ),
]


#//******************************************************************************
#//
#//  dataPrefixes
#//
#//  ( name, abbreviation, power of 10 )
#//
#//******************************************************************************

dataPrefixes = [
    ( 'yotta',      'Y',      '24' ),
    ( 'zetta',      'Z',      '21' ),
    ( 'exa',        'E',      '18' ),
    ( 'peta',       'P',      '15' ),
    ( 'tera',       'T',      '12' ),
    ( 'giga',       'G',      '9' ),
    ( 'mega',       'M',      '6' ),
    ( 'kilo',       'k',      '3' ),
]


#//******************************************************************************
#//
#//  binaryPrefixes
#//
#//  ( name, abbreviation, power of 2 )
#//
#//******************************************************************************

binaryPrefixes = [
    ( 'yobi',       'Yi',     '80' ),
    ( 'zebi',       'Zi',     '70' ),
    ( 'exi',        'Ei',     '60' ),
    ( 'pebi',       'Pi',     '50' ),
    ( 'tebi',       'Ti',     '40' ),
    ( 'gibi',       'Gi',     '30' ),
    ( 'mebi',       'Mi',     '20' ),
    ( 'kibi',       'ki',     '10' ),
]


#//******************************************************************************
#//
#//  unitConversionMatrix
#//
#//  ( first unit, second unit, conversion factor )
#//
#//******************************************************************************

unitConversionMatrix = {
    ( 'abampere',              'ampere' )                               : '10',
    ( 'abcoulomb',             'coulomb' )                              : '10',
    ( 'acre',                  'square_yard' )                          : '4840',
    ( 'acre-foot',             'cubic_foot' )                           : '43560',
    ( 'aln',                   'inch' )                                 : '23.377077865',
    ( 'ampere',                'coulomb/second' )                       : '1',
    ( 'arcminute',             'arcsecond' )                            : '60',
    ( 'are',                   'square_meter' )                         : '100',
    ( 'arpent',                'foot' )                                 : '192',
    ( 'astronomical_unit',     'meter' )                                : '149597870700',
    ( 'atmosphere',            'pascal' )                               : '101325',
    ( 'balthazar',             'liter' )                                : '12.0',
    ( 'ban',                   'nat' )                                  : '2.30258509299404568402',  # ln(10)
    ( 'bar',                   'pascal' )                               : '100000',
    ( 'barleycorn',            'poppyseed' )                            : '4',
    ( 'barrel',                'gallon' )                               : '31.5',
    ( 'becquerel',             'curie' )                                : '3.7e10',
    ( 'bit',                   'nat' )                                  : '0.69314718055994530942',  # ln(2)
    ( 'blintz',                'farshimmelt_blintz' )                   : '100000',
    ( 'blintz',                'gram' )                                 : '36.42538631',
    ( 'btu',                   'joule' )                                : '1054.5',
    ( 'bucket',                'gallon' )                               : '4',
    ( 'bushel',                'peck' )                                 : '4',
    ( 'butt',                  'gallon' )                               : '126',
    ( 'byte',                  'bit' )                                  : '8',
    ( 'calorie',               'joule' )                                : '4.184',
    ( 'carat',                 'grain' )                                : '3.1666666666666666666666',
    ( 'century',               'microcentury' )                         : '1.0e6',
    ( 'century',               'nanocentury' )                          : '1.0e9',
    ( 'century',               'year' )                                 : '100',
    ( 'chain',                 'yard' )                                 : '22',
    ( 'chopine',               'liter' )                                : '0.25',
    ( 'clarke',                'day' )                                  : '1',
    ( 'clarke',                'wolverton' )                            : '1000000',
    ( 'clausius',              'joule/kelvin' )                         : '4186.8',
    ( 'clavelin',              'liter' )                                : '0.62',
    ( 'cord',                  'cubic_foot' )                           : '128',
    ( 'coulomb',               'ampere-second' )                        : '1',
    ( 'coulomb',               'electron_charge' )                      : '6.24150965e18',
    ( 'coulomb',               'farad-volt' )                           : '1',
    ( 'coulomb/farad',         'volt' )                                 : '1',
    ( 'coulomb/kilogram',      'roentgen' )                             : '3876',
    ( 'coulomb/volt',          'farad' )                                : '1',
    ( 'cowznofski',            'mingo' )                                : '10',
    ( 'cubic_meter',           'liter' )                                : '1000',
    ( 'cubit',                 'inch' )                                 : '18',
    ( 'cup',                   'dram' )                                 : '64',
    ( 'cup',                   'fluid_ounce' )                          : '8',
    ( 'cup',                   'gill' )                                 : '2',
    ( 'day',                   'hour' )                                 : '24',
    ( 'decade',                'year' )                                 : '10',
    ( 'degree',                'arcminute' )                            : '60',
    ( 'demi',                  'liter' )                                : '0.375',
    ( 'dessertspoon',          'teaspoon' )                             : '2',
    ( 'dry_barrel',            'cubic_inch' )                           : '7056',
    ( 'dry_gallon',            'dry_quart' )                            : '4',
    ( 'dry_pint',              'cubic_inch' )                           : '33.6003125',
    ( 'dry_quart',             'dry_pint' )                             : '2',
    ( 'dword',                 'bit' )                                  : '32',
    ( 'ell',                   'inch' )                                 : '45',
    ( 'famn',                  'aln' )                                  : '3',
    ( 'farad',                 'jar' )                                  : '9.0e8',
    ( 'faraday',               'coulomb' )                              : '96485.3383',
    ( 'fathom',                'foot' )                                 : '6',
    ( 'finger',                'inch' )                                 : '4.5',
    ( 'fingerbreadth',         'inch' )                                 : '0.75',
    ( 'firkin',                'gallon' )                               : '9',
    ( 'fluid_dram',            'fluid_scruple' )                        : '3',
    ( 'fluid_ounce',           'fluid_dram' )                           : '8',
    ( 'fluid_ounce',           'tablespoon' )                           : '2',
    ( 'fluid_scruple',         'minim' )                                : '20',
    ( 'foot',                  'inch' )                                 : '12',
    ( 'footcandle',            'lumen/foot^2' )                         : '1',
    ( 'footcandle',            'lux' )                                  : '10.763910417',  # (m/ft)^2
    ( 'footlambert',           'candela/meter^2' )                      : '3.42625909963539052691',  # 1/pi cd/ft^2
    ( 'fortnight',             'day' )                                  : '14',
    ( 'fortnight',             'microfortnight' )                       : '1000000',
    ( 'furlong',               'yard' )                                 : '220',
    ( 'furshlugginer_blintz',  'blintz' )                               : '1000000',
    ( 'furshlugginer_ngogn',   'ngogn' )                                : '1000000',
    ( 'furshlugginer_potrzebie', 'potrzebie' )                          : '1000000',
    ( 'gallon',                'fifth' )                                : '5',
    ( 'gallon',                'quart' )                                : '4',
    ( 'gauss',                 'maxwell/centimeter^2' )                 : '1',
    ( 'goliath',               'liter' )                                : '27.0',
    ( 'grad',                  'degree' )                               : '0.9',
    ( 'gram',                  'planck_mass' )                          : '45940.892447777',
    ( 'gray',                  'rad' )                                  : '100',
    ( 'greek_cubit',           'inch' )                                 : '18.22',
    ( 'gregorian_year',        'day' )                                  : '365.2425',
    ( 'handbreadth',           'inch' )                                 : '3',
    ( 'hartree',               'rydberg' )                              : '2',
    ( 'hefnerkerze',           'candela' )                              : '0.920',  # approx.
    ( 'henry',                 'weber/ampere' )                         : '1',
    ( 'hogshead',              'gallon' )                               : '63',
    ( 'homestead',             'acre' )                                 : '160',
    ( 'horsepower',            'watt' )                                 : '745.69987158227022',
    ( 'horsepower-second',     'joule' )                                : '745.69987158227022',
    ( 'hour',                  'minute' )                               : '60',
    ( 'inch',                  'barleycorn' )                           : '3',
    ( 'inch',                  'caliber' )                              : '100',
    ( 'inch',                  'gutenberg' )                            : '7200',
    ( 'inch',                  'meter' )                                : '0.0254',
    ( 'inch',                  'mil' )                                  : '1000',
    ( 'inch',                  'pica' )                                 : '6',
    ( 'inch',                  'point' )                                : '72',
    ( 'inch',                  'twip' )                                 : '1440',
    ( 'jennie',                'liter' )                                : '0.5',
    ( 'jeroboam',              'liter' )                                : '3.0',  # some French regions use 4.5
    ( 'joule',                 'electronvolt' )                         : '6.24150974e18',
    ( 'joule',                 'erg' )                                  : '10000000',
    ( 'joule',                 'kilogram-meter^2/second^2' )            : '1',
    ( 'joule/second',          'watt' )                                 : '1',
    ( 'ken',                   'inch' )                                 : '83.4',
    ( 'kovac',                 'wolverton' )                            : '10',
    ( 'lambert',               'candela/meter^2' )                      : '3183.098861837906715378',  # 10000/pi
    ( 'league',                'mile' )                                 : '3',
    ( 'light',                 'meter/second' )                         : '299792458',
    ( 'light-second',          'meter' )                                : '299792458',
    ( 'light-year',            'light-second' )                         : '31557600',
    ( 'link',                  'inch' )                                 : '7.92',
    ( 'liter',                 'ngogn' )                                : '86.2477899004',
    ( 'long_cubit',            'inch' )                                 : '21',
    ( 'long_reed',             'foot' )                                 : '10.5',
    ( 'lunar-day',             'minute' )                               : '1490',
    ( 'lux',                   'lumen/meter^2' )                        : '1',
    ( 'lux',                   'nox' )                                  : '1000',
    ( 'mach',                  'meter/second' )                         : '295.0464',
    ( 'magnum',                'liter' )                                : '1.5',
    ( 'marathon',              'yard' )                                 : '46145',
    ( 'marie_jeanne',          'liter' )                                : '2.25',
    ( 'martin',                'kovac' )                                : '100',
    ( 'melchior',              'liter' )                                : '18.0',
    ( 'melchizedek',           'liter' )                                : '30.0',
    ( 'meter',                 'angstrom' )                             : '10000000000',
    ( 'meter',                 'kyu' )                                  : '4000',
    ( 'meter',                 'micron' )                               : '1000000',
    ( 'meter/second',          'knot' )                                 : '1.943844492',
    ( 'methuselah',            'liter' )                                : '6.0',
    ( 'mile',                  'foot' )                                 : '5280',
    ( 'mingo',                 'clarke' )                               : '10',
    ( 'minute',                'second' )                               : '60',
    ( 'mmHg',                  'pascal' )                               : '133.3224',        # approx.
    ( 'mordechai',             'liter' )                                : '9.0',
    ( 'nail',                  'inch' )                                 : '2.25',
    ( 'nat',                   'joule/kelvin' )                         : '1.380650e-23',
    ( 'nautical_mile',         'meter' )                                : '1852',
    ( 'nebuchadnezzar',        'liter' )                                : '15.0',
    ( 'newton',                'dyne' )                                 : '100000',
    ( 'newton',                'joule/meter' )                          : '1',
    ( 'newton',                'pond' )                                 : '101.97161298',
    ( 'newton',                'poundal' )                              : '7.233013851',
    ( 'newton/meter^2',        'pascal' )                               : '1',
    ( 'ngogn',                 'farshimmelt_ngogn' )                    : '100000',
    ( 'nibble',                'bit' )                                  : '4',
    ( 'nit',                   'apostilb' )                             : '3.141592653589793',  # pi
    ( 'nit',                   'candela/meter^2' )                      : '1',
    ( 'nit',                   'lambert' )                              : '0.0003141592653589793',  # pi/10000
    ( 'nyp',                   'bit' )                                  : '2',
    ( 'octant',                'degree' )                               : '45',
    ( 'ohm',                   '1/siemens' )                            : '1',
    ( 'ohm',                   'abohm' )                                : '1e9',
    ( 'ohm',                   'german_mile' )                          : '57.44',
    ( 'ohm',                   'jacobi' )                               : '0.6367',
    ( 'ohm',                   'joule-second/coulomb^2' )               : '1',
    ( 'ohm',                   'joule/second-ampere^2' )                : '1',
    ( 'ohm',                   'kilogram-meter^2/second^3-ampere^2' )   : '1',
    ( 'ohm',                   'matthiessen' )                          : '13.59',
    ( 'ohm',                   'meter^2-kilogram/second-couloumb^2' )   : '1',
    ( 'ohm',                   'second/farad' )                         : '1',
    ( 'ohm',                   'varley' )                               : '25.61',
    ( 'ohm',                   'volt/ampere' )                          : '1',
    ( 'ohm',                   'watt/ampere^2' )                        : '1',
    ( 'oil_barrel',            'gallon' )                               : '42',
    ( 'ounce',                 'gram' )                                 : '28.349523125',
    ( 'oword',                 'bit' )                                  : '128',
    ( 'parsec',                'light-year' )                           : '3.261563776971',
    ( 'pascal',                'barye' )                                : '10',
    ( 'peck',                  'dry_gallon' )                           : '2',
    ( 'perch',                 'foot' )                                 : '16.5',
    ( 'phot',                  'lux' )                                  : '10000',
    ( 'piccolo',               'liter' )                                : '0.1875',
    ( 'pieze',                 'pascal' )                               : '1000',
    ( 'planck_charge',         'coulomb' )                              : '1.875545956e-18',
    ( 'planck_energy',         'joule' )                                : '1.956e9',
    ( 'planck_length',         'meter' )                                : '1.616199e-35',
    ( 'planck_time',           'second' )                               : '5.39106e-44',
    ( 'poncelet',              'watt' )                                 : '980.665',
    ( 'potrzebie',             'farshimmelt_potrzebie' )                : '100000',
    ( 'potrzebie',             'meter' )                                : '0.002263348517438173216473',  # see Mad #33
    ( 'pound',                 'grain' )                                : '7000',
    ( 'pound',                 'ounce' )                                : '16',
    ( 'pound',                 'sheet' )                                : '700',
    ( 'psi',                   'pascal' )                               : '6894.757',        # approx.
    ( 'quadrant',              'degree' )                               : '90',
    ( 'quart',                 'cup' )                                  : '4',
    ( 'quart',                 'liter' )                                : '0.946352946',
    ( 'quart',                 'pint' )                                 : '2',
    ( 'quintant',              'degree' )                               : '72',
    ( 'qword',                 'bit' )                                  : '64',
    ( 'radian',                'degree' )                               : '57.2957795130823208768',   # 180/pi
    ( 'reed',                  'foot' )                                 : '9',
    ( 'rehoboam',              'liter' )                                : '4.5',
    ( 'rod',                   'foot' )                                 : '16.5',
    ( 'rood',                  'square_yard' )                          : '1210',
    ( 'rope',                  'foot' )                                 : '20',
    ( 'rutherford',            'becquerel' )                            : '1000000',
    ( 'rydberg',               'joule' )                                : '2.179872e-18',
    ( 'salmanazar',            'liter' )                                : '9.0',
    ( 'second',                'jiffy' )                                : '100',
    ( 'second',                'shake' )                                : '1.0e8',
    ( 'second',                'sigma' )                                : '1.0e6',
    ( 'second',                'svedberg' )                             : '1.0e13',
    ( 'sextant',               'degree' )                               : '60',
    ( 'siderial_day',          'second' )                               : '86164.1',
    ( 'siderial_year',         'day' )                                  : '365.256363',
    ( 'siemens',               'ampere/volt' )                          : '1',
    ( 'siemens',               'kilogram-meter^2/second^3-ampere^2' )   : '1',
    ( 'skot',                  'bril' )                                 : '1.0e4',
    ( 'skot',                  'lambert' )                              : '1.0e7',
    ( 'slug',                  'pound' )                                : '32.174048556',
    ( 'smoot',                 'inch' )                                 : '67',
    ( 'solomon',               'liter' )                                : '20.0',
    ( 'sovereign',             'liter' )                                : '25.0',
    ( 'span',                  'inch' )                                 : '9',
    ( 'square_arcminute',      'square_arcsecond' )                     : '3600',
    ( 'square_degree',         'square_arcminute' )                     : '3600',
    ( 'square_meter',          'barn' )                                 : '1.0e28',
    ( 'square_meter',          'outhouse' )                             : '1.0e34',
    ( 'square_meter',          'shed' )                                 : '1.0e52',
    ( 'square_octant',         'square_degree' )                        : '2025',
    ( 'square_quadrant',       'square_degree' )                        : '8100',
    ( 'square_sextant',        'square_degree' )                        : '3600',
    ( 'standard',              'liter' )                                : '0.75',
    ( 'standard_gravity',      'galileo' )                              : '980.6650',
    ( 'standard_gravity',      'meter/second^2' )                       : '9.80665',
    ( 'statcoulomb',           'coulomb' )                              : '3.335641e-10',  # 0.1A*m/c, approx.
    ( 'statcoulomb',           'franklin' )                             : '1',
    ( 'steradian',             'square_degree' )                        : '0.000304617419786708510', # (pi/180)^2
    ( 'steradian',             'square_grad' )                          : '0.00024674011002723397',  # (pi/200)^2
    ( 'sthene',                'newton' )                               : '1000',
    ( 'stilb',                 'candela/meter^2' )                      : '10000',
    ( 'stone',                 'pound' )                                : '14',
    ( 'tablespoon',            'teaspoon' )                             : '3',
    ( 'teaspoon',              'dash' )                                 : '8',
    ( 'teaspoon',              'pinch' )                                : '16',
    ( 'teaspoon',              'smidgen' )                              : '32',
    ( 'tenth',                 'liter' )                                : '0.378',
    ( 'tesla',                 'gauss' )                                : '10000',
    ( 'tesla',                 'kilogram/ampere-second^2' )             : '1',
    ( 'tesla',                 'weber/meter^2' )                        : '1',
    ( 'ton',                   'pound' )                                : '2000',
    ( 'tonne',                 'gram' )                                 : '1000000',
    ( 'ton_of_TNT',            'joule' )                                : '4184000000',
    ( 'torr',                  'mmHg' )                                 : '1',
    ( 'township',              'acre' )                                 : '23040',
    ( 'trit',                  'nat' )                                  : '1.098612288668109691310',  # ln(3)
    ( 'tropical_year',         'day' )                                  : '365.24219',
    ( 'troy_ounce',            'gram' )                                 : '31.1034768',
    ( 'troy_pound',            'pound' )                                : '12',
    ( 'tryte',                 'trit' )                                 : '6',   # as defined by the Setun computer
    ( 'tun',                   'gallon' )                               : '252',
    ( 'watt',                  'erg/second' )                           : '1.0e7',
    ( 'watt',                  'kilogram-meter^2/second^3' )            : '1',
    ( 'watt',                  'newton-meter/second' )                  : '1',
    ( 'watt-second',           'joule' )                                : '1',
    ( 'weber',                 'maxwell' )                              : '1.0e8',
    ( 'weber',                 'volt-second' )                          : '1',
    ( 'week',                  'day' )                                  : '7',
    ( 'wey',                   'pound' )                                : '252',
    ( 'wood',                  'martin' )                               : '100',
    ( 'word',                  'bit' )                                  : '16',
    ( 'yard',                  'foot' )                                 : '3',
    ( 'year',                  'day' )                                  : '365.25',
}


#//******************************************************************************
#//
#//  makeMetricUnit
#//
#//******************************************************************************

def makeMetricUnit( prefix, unit ):
    # special case because the standard is inconsistent
    if ( unit == 'ohm' ) and ( prefix == 'giga' ):
        return 'gigaohm'
    elif ( unit[ 0 ] == 'o' ) and ( prefix[ -1 ] in 'oa' ):
        return prefix[ : -1 ] + unit
    elif unit[ 0 ] == 'a' and ( ( prefix[ -1 ] == 'a' ) or ( prefix[ -3 : ] == 'cto' ) ):
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

    for dataUnit in dataUnits:
        newAliases[ dataUnit[ 2 ] ] = dataUnit[ 0 ]

        for prefix in dataPrefixes:
            unit = prefix[ 0 ] + dataUnit[ 0 ]
            pluralUnit = prefix[ 0 ] + dataUnit[ 1 ]
            newAliases[ pluralUnit ] = unit                     # add plural alias

            newAliases[ prefix[ 1 ] + dataUnit[ 2 ] ] = unit   # add SI abbreviation alias

            for alternateUnit in dataUnit[ 3 ]:                # add alternate spelling alias
                newAliases[ prefix[ 0 ] + alternateUnit ] = unit

            for alternateUnit in dataUnit[ 4 ]:                # add alternate spelling plural alias
                newAliases[ prefix[ 0 ] + alternateUnit ] = unit

        for prefix in binaryPrefixes:
            unit = prefix[ 0 ] + dataUnit[ 0 ]
            pluralUnit = prefix[ 0 ] + dataUnit[ 1 ]
            newAliases[ pluralUnit ] = unit                     # add plural alias

            newAliases[ prefix[ 1 ] + dataUnit[ 2 ] ] = unit   # add SI abbreviation alias

            for alternateUnit in dataUnit[ 3 ]:                # add alternate spelling alias
                newAliases[ prefix[ 0 ] + alternateUnit ] = unit

            for alternateUnit in dataUnit[ 4 ]:                # add alternate spelling plural alias
                newAliases[ prefix[ 0 ] + alternateUnit ] = unit

    for unit in unitOperators:
        unitInfo = unitOperators[ unit ]
        newAliases[ unitInfo.plural ] = unit

        for alias in unitInfo.aliases:
            newAliases[ alias ] = unit

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
                UnitInfo( unitOperators[ metricUnit[ 0 ] ].unitType, 'SI', newName, newPlural,
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
#//  expandDataUnits
#//
#//  Every data unit needs to be permuted for all positive SI power types and
#//  the binary power types.  We need to create conversions for each new type,
#//  as well as aliases.
#//
#//******************************************************************************

def expandDataUnits( newAliases ):
    # expand data measurements for all prefixes
    newConversions = { }

    for dataUnit in dataUnits:
        for prefix in dataPrefixes:
            newName = prefix[ 0 ] + dataUnit[ 0 ]
            newPlural = prefix[ 0 ] + dataUnit[ 1 ]

            # constuct unit operator info
            unitOperators[ newName ] = \
                UnitInfo( unitOperators[ dataUnit[ 0 ] ].unitType, unitOperators[ dataUnit[ 0 ] ].category,
                                         newName, newPlural, prefix[ 1 ] + dataUnit[ 2 ], [ ] )

            newConversion = power( 10, mpmathify( prefix[ 2 ] ) )
            unitConversionMatrix[ ( newName, dataUnit[ 0 ] ) ] = str( newConversion )
            newConversion = fdiv( 1, newConversion )
            unitConversionMatrix[ ( dataUnit[ 0 ], newName ) ] = str( newConversion )

            for op1, op2 in unitConversionMatrix:
                if ( op1 == dataUnit[ 0 ] ) or ( op2 == dataUnit[ 0 ] ):
                    oldConversion = mpmathify( unitConversionMatrix[ ( op1, op2 ) ] )

                    if op1 == dataUnit[ 0 ] and newName != op2:
                        newConversions[ ( newName, op2 ) ] = str( fdiv( oldConversion, newConversion ) )
                        #print( '(', newName, op2, ')', str( fdiv( oldConversion, newConversion ) ) )
                    elif op2 == dataUnit[ 0 ] and newName != op1:
                        newConversions[ ( op1, newName ) ] = str( fmul( oldConversion, newConversion ) )
                        #print( '(', op1, newName, ')', str( fmul( oldConversion, newConversion ) ) )

        for prefix in binaryPrefixes:
            newName = prefix[ 0 ] + dataUnit[ 0 ]
            newPlural = prefix[ 0 ] + dataUnit[ 1 ]

            # constuct unit operator info
            unitOperators[ newName ] = \
                UnitInfo( unitOperators[ dataUnit[ 0 ] ].unitType, unitOperators[ dataUnit[ 0 ] ].category,
                                         newName, newPlural, prefix[ 1 ] + dataUnit[ 2 ], [ ] )

            newConversion = power( 2, mpmathify( prefix[ 2 ] ) )
            unitConversionMatrix[ ( newName, dataUnit[ 0 ] ) ] = str( newConversion )
            newConversion = fdiv( 1, newConversion )
            unitConversionMatrix[ ( dataUnit[ 0 ], newName ) ] = str( newConversion )

            for op1, op2 in unitConversionMatrix:
                if ( op1 == dataUnit[ 0 ] ) or ( op2 == dataUnit[ 0 ] ):
                    oldConversion = mpmathify( unitConversionMatrix[ ( op1, op2 ) ] )

                    if op1 == dataUnit[ 0 ] and newName != op2:
                        newConversions[ ( newName, op2 ) ] = str( fdiv( oldConversion, newConversion ) )
                    elif op2 == dataUnit[ 0 ] and newName != op1:
                        newConversions[ ( op1, newName ) ] = str( fmul( oldConversion, newConversion ) )

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

    newUnitInfo = UnitInfo( 'area', unitInfo.category, unit + '^2', 'square_' + unitPlural, abbrev, [ ] )

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

    newUnitInfo = UnitInfo( 'volume', unitInfo.category, unit + '^3', 'cubic_' + unitPlural, abbrev, [ ] )

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
    print( 'Mapping compound units...' )

    compoundUnits = { }

    for unit1, unit2 in unitConversionMatrix:
        chars = set( '*/^' )

        if any( ( c in chars ) for c in unit2 ):
            compoundUnits[ unit1 ] = unit2
            #print( '    compound unit: ', unit1, '(', unit2, ')' )

    # create area and volume units from all of the length units
    #print( )
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

                compoundUnits[ unit + '*' + unit ] = newUnit

            newUnit = 'cubic_'+ unit

            if newUnit not in unitOperators:
                newUnitInfo, newUnitAliases = makeVolumeOperator( unit, unitOperators[ unit ].plural )

                newAliases.update( newUnitAliases )
                newOperators[ newUnit ] = newUnitInfo

                compoundUnits[ unit + '*' + unit + '*' + unit ] = newUnit

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

    for unitType in sorted( basicUnitTypes ):
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

    # the second pass allows the full permuation of conversions between base types of the same unit type
    # (e.g., it's necessary to get a conversion between 'megameter' and 'megapotrzebie' )
    print( 'Expanding metric units (second pass)...' )
    unitConversionMatrix.update( expandMetricUnits( newAliases ) )

    print( 'Expanding data units against the list of SI and binary prefixes...' )

    unitConversionMatrix.update( expandDataUnits( newAliases ) )

    print( 'Expanding data units (second pass)...' )
    unitConversionMatrix.update( expandDataUnits( newAliases ) )

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
                    UnitInfo( unitInfo.unitType, unitInfo.category, unitRoot + '*' + timeUnit[ 0 ], newPlural, '', [ ] )

                conversion = mpmathify( timeUnit[ 3 ] )
                unitConversionMatrix[ ( newUnit, unit ) ] = str( conversion )
                unitConversionMatrix[ ( unit, newUnit ) ] = str( fdiv( 1, conversion ) )

    unitOperators.update( newUnitOperators )

    newUnitOperators = { }

    for unit in unitOperators:
        if unit[ -7 : ] == '/second' and unit[ : 7 ] != 'square_' and unit[ : 6 ] != 'cubic_':
            unitRoot = unit[ : -7 ]

            unitInfo = unitOperators[ unit ]
            rootUnitInfo = unitOperators[ unitRoot ]

            for timeUnit in timeUnits:
                newUnit = unitRoot + '/' + timeUnit[ 0 ]
                newPlural = unitRoot + '/' + timeUnit[ 1 ]
                newAliases[ newPlural ] = newUnit
                newAliases[ unitRoot + '/' + timeUnit[ 1 ] ] = newUnit

                # We assume the abbrev ends with an s for second
                if unitInfo.abbrev != '':
                    newAbbrev = unitInfo.abbrev[ : -1 ] + timeUnit[ 2 ]
                    newAliases[ newAbbrev ] = newUnit

                for alias in rootUnitInfo.aliases:
                    newAliases[ alias + '/' + timeUnit[ 0 ] ] = newUnit
                    newAliases[ alias + '/' + timeUnit[ 1 ] ] = newUnit

                newUnitOperators[ newUnit ] = \
                    UnitInfo( unitInfo.unitType, unitInfo.category, unitRoot + '*' + timeUnit[ 0 ], newPlural, '', [ ] )

                conversion = mpmathify( timeUnit[ 3 ] )
                unitConversionMatrix[ ( newUnit, unit ) ] = str( fdiv( 1, conversion ) )
                unitConversionMatrix[ ( unit, newUnit ) ] = str( conversion )

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

