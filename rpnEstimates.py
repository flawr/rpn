#!/usr/bin/env python

#//******************************************************************************
#//
#//  rpnEstimates.py
#//
#//  RPN command-line calculator, estimate table declarations
#//  copyright (c) 2014 (1988), Rick Gutleber (rickg@his.com)
#//
#//  License: GNU GPL 3.0 (see <http://www.gnu.org/licenses/gpl.html> for more
#//  information).
#//
#//******************************************************************************

from mpmath import *

#// Can we stick this in somewhere?
#//
#// https://en.wikipedia.org/wiki/Orders_of_magnitude_%28density%29

#//******************************************************************************
#//
#//  accelerationTable
#//
#//  meters/second^2 : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28acceleration%29
#//
#//******************************************************************************

accelerationTable = {
    mpf( '0.0058' )     : 'the acceleration of the Earth due to the Sun\'s gravity',
    mpf( '1.62' )       : 'the Moon\'s gravity at its equator',
    mpf( '4.3' )        : 'the acceleration going from 0-60 mph in 6.4 seconds (Saab 9-5 Hirsch)',
    mpf( '9.80665' )    : 'the Earth\'s gravity',
    mpf( '15.2' )       : 'the acceleration going from 0-100 kph in 2.4 seconds (Bugatti Veyron)',
    mpf( '29' )         : 'the maximum acceleration during launch and re-entry of the Space Shuttle',
    mpf( '70.6' )       : 'the maximum acceleration of Apollo 6 during re-entry',
    mpf( '79' )         : 'the acceleration of an F-16 aircraft pulling out of a dive',
    mpf( '147' )        : 'the acceleration of an explosive seat ejection from an aircraft',
    mpf( '2946' )       : 'the acceleration of a soccer ball being kicked',
    mpf( '29460' )      : 'the acceleration of a baseball struck by a bat',
    mpf( '3.8e6' )      : 'the surface gravity of white dwarf Sirius B',
    mpf( '1.9e9' )      : 'the mean acceleration of a proton in the Large Hadron Collider',
    mpf( '7.0e12' )     : 'the maximum surface gravity of a neutron star',
}


#//******************************************************************************
#//
#//  angleTable
#//
#//  radians : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28angular_velocity%29
#//
#//******************************************************************************

angleTable = {
    mpf( '8.405e-16' )  : 'the angle the Sun revolves around the galactic core in a second',
    mpf( '8.03e-10' )   : 'the angle Pluto revolves around the Sun in a second',
    mpf( '1.68e-8' )    : 'the angle Jupiter revolves around the Sun in a second',
    mpf( '1.99e-7' )    : 'the angle the Earth revolves around the Sun in a second',
    mpf( '7.27e-5' )    : 'the angle the Earth rotates in a second',
    mpf( '0.0001454' )  : 'the angle a clock hour hand moves in a second',
    mpf( '0.0017453' )  : 'the angle a clock minute hand moves in a second',
    mpf( '0.10471976' ) : 'the angle a clock second hand moves in a second',
    mpf( '3.4906585' )  : 'the angle a long-playing record rotates in one second',
    mpf( '94' )         : 'the angle the spin cycle of washing machine rotates in one second',
    mpf( '753.982237' ) : 'the angle a 7200-rpm harddrive rotates in a second',
}


#//******************************************************************************
#//
#//  areaTable
#//
#//  meters^2 : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28area%29
#//
#//******************************************************************************

areaTable = {
    mpf( '2.6121e-70' ) : 'the Planck area',
    mpf( '1.0e-52' )    : 'one shed',
    mpf( '1.0e-48' )    : 'one square yoctometer',
    mpf( '1.0e-42' )    : 'one square zeptometer',
    mpf( '1.0e-36' )    : 'one square attometer',
    mpf( '1.0e-28' )    : 'one barn, roughly the cross-sectional area of a uranium nucleus',
    mpf( '1.0e-24' )    : 'one square picometer',
    mpf( '1.0e-18' )    : 'one square nanometer',
    mpf( '1.0e-12' )    : 'one square micron, the surface area of an E. coli bacterium',
    mpf( '1.0e-10' )    : 'the surface area of a human red blood cell',
    mpf( '7.0e-9' )     : 'the surface area of a human red blood cell',
    mpf( '7.1684e-9' )  : 'the area of a single pixel at 300 dpi resolution',
    mpf( '6.4516e-8' )  : 'the area of a single pixel at 100 dpi resolution',
    mpf( '1.9635e-7' )  : 'the cross-sectional area of a 0.5mm pencil lead',
    mpf( '2.9e-4' )     : 'the area of one side of a U.S. penny',
    mpf( '4.6e-3' )     : 'the area of the face of a credit card',
    mpf( '0.009677' )   : 'the area of a 3x5 inch index card',
    mpf( '0.06032246' ) : 'American letter size paper (8.5x11")',
    mpf( '1.73' )       : 'the average body surface area of a human',
    mpf( '261' )        : 'the size of a standard tennis court',
    mpf( '1250' )       : 'the surface area of an Olympic-size swimming pool',
    mpf( '4046.856' )   : 'one acre',
    mpf( '22074' )      : 'area of a Manhattan city block',
    mpf( '440000' )     : 'Vatican City',
    mpf( '2589988.11' ) : 'one square mile',
    mpf( '5.95e7' )     : 'the surface area of Manhattan Island',
}


#//******************************************************************************
#//
#//  capacitanceTable
#//
#//  farads : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28capacitance%29
#//
#//******************************************************************************

capacitanceTable = {
    mpf( '2.0e-15' )    : 'the gate capacitance of a MOS transistor, per micron of gate width',
    mpf( '3.0e-14' )    : 'a DRAM cell',
    mpf( '1.0e-13' )    : 'a small ceramic capacitor (100 fF)',
    mpf( '1.0e-12' )    : 'a small mica and PTFE capacitor (1 pF)',
    mpf( '4.0e-12' )    : 'the capacitive sensing of air-water-snow-ice (4 pF)',
    mpf( '5.0e-12' )    : 'a low condenser microphone (5 pF)',
    mpf( '4.5e-11' )    : 'a variable capacitor (45 pF)',
    mpf( '4.9e-11' )    : 'a yoga mat of TPE with relative permittivity of 4.5 and 8 mm thick sandwiched between two 1 dm^2 electrodes (49 pF)',
    mpf( '5.0e-11' )    : '1 m of Cat 5 network cable (between the two conductors of a twisted pair) (50 pF)',
    mpf( '1.0e-10' )    : 'the capacitance of the standard human body model (100 pF)',
    mpf( '1.0e-10' )    : '1 m of 50 ohm coaxial cable (between the inner and outer conductors) (100 pF)',
    mpf( '1.0e-10' )    : 'a high condenser microphone (100 pF)',
    mpf( '3.3e-10' )    : 'a variable capacitor (330 pF)',
    mpf( '1.0e-9' )     : 'a typical leyden jar (1 nF)',
    mpf( '1.0e-7' )     : 'a small aluminum electrolytic capacitor (100 nF)',
    mpf( '8.2e-7' )     : 'a large mica and PTFE capacitor (820 nF)',
    mpf( '1.0e-4' )     : 'a large ceramic capacitor (100 uF)',
    mpf( '6.8e-3' )     : 'a small electric double layer supercapacitor (6.8 mF)',
    mpf( '1.0' )        : 'the Earth-ionosphere capacitance (1 F)',
    mpf( '1.5' )        : 'a large aluminum electrolytic capacitor (1.5 F)',
    mpf( '5.0e3' )      : 'a large electric double layer supercapacitor (5000 F)',
}


#//******************************************************************************
#//
#//  chargeTable
#//
#//  coulombs : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28charge%29
#//
#//******************************************************************************

chargeTable = {
    mpf( '-5.34e-20' )  : '-1/3 e - the charge of down, strange and bottom quarks',
    mpf( '1.068e-19' )  : '2/3 e - the charge of up, charm and top quarks',
    mpf( '1.602e-19' )  : 'the elementary charge e, i.e. the negative charge on a single electron or the positive charge on a single proton',
    mpf( '1.9e-18' )    : 'the Planck charge',
    mpf( '1.473e-17' )  : '92 e - positive charge on a uranium nucleus',
    mpf( '1e-15' )      : 'the charge on a typical dust particle',
    mpf( '1e-12' )      : 'the charge in typical microwave frequency capacitors',
    mpf( '1e-9' )       : 'the charge in typical radio frequency capacitors',
    mpf( '1e-6' )       : 'the charge in typical audio frequency capacitors, and the static electricity from rubbing materials together',
    mpf( '1.0e-3' )     : 'the charge in typical power supply capacitors',
    mpf( '1' )          : 'two negative point charges of 1 C, placed one meter apart, would experience a repulsive force of 9 GN',
    mpf( '26' )         : 'the charge in a typical thundercloud (15 - 350 C)',
    mpf( '5.0e3' )      : 'the typical alkaline AA battery is about 5000 C, or ~ 1.4 Ah',
    mpf( '9.64e4' )     : 'the charge on one mole of electrons (Faraday constant)',
    mpf( '2.16e5' )     : 'a car battery charge',
    mpf( '1.07e7' )     : 'the charge needed to produce 1 kg of aluminum from bauxite in an electrolytic cell',
    mpf( '5.9e8' )      : 'the charge in the worl\'s largest battery bank (36 MWh), assuming 220VAC output',
}


#//******************************************************************************
#//
#//  constantTable
#//
#//  unities : description
#//
#//******************************************************************************

constantTable = {
}


#//******************************************************************************
#//
#//  currentTable
#//
#//  amperes : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28current%29
#//
#//******************************************************************************

currentTable = {
    mpf( '1.0e-5' )     : 'the minimum current necessary to cause death (by ventricular fibrillation when applied directly across the human heart)',
    mpf( '7.0e-3' )     : 'a portable hearing aid (typically 1 mW at 1.4 V)',
    mpf( '3.0e-3' )     : 'a cathode ray tube electron gun beam current (1-5 mA)',
    mpf( '1.0e-2' )     : 'a charge which through the hand to foot may cause a person to freeze and be unable to let go (10 mA)',
    mpf( '2.0e-2' )     : 'a common light-emitting diode (constant current), also deadly limit for skin contact (at 120-230 V)',
    mpf( '1.5e-1' )     : 'a 230 V AC, 22-inch/56-centimeter portable television (35 W)',
    mpf( '1.66e-1' )    : 'a typical 12 V motor vehicle instrument panel light',
    mpf( '2.9e-1' )     : 'a 120 V AC, 22-inch/56-centimeter portable television (35 W)',
    mpf( '1.35' )       : 'a Tesla coil, 0.76 meters (2 ft 6 in) high, at 200 kV and 270 kV peak',
    mpf( '2.1' )        : 'a high power LED current (peak 2.7 A)',
    mpf( '5' )          : 'a typical 12 V motor vehicle headlight (typically 60 W)',
    mpf( '16.67' )      : 'a 120 V AC, Toaster, kettle (2 kW)',
    mpf( '38.33' )      : 'a 120 V AC, Immersion heater (4.6 kW)',
    mpf( '120' )        : 'a typical 12 V motor vehicle starter motor (typically 1-2 kW)',
    mpf( '166' )        : 'a 400 V low voltage secondary side distribution transformer with primary 12 kV ; 200 kVA (up to 1000 kVA also common)',
    mpf( '2.0e3' )      : 'a 10.5 kV secondary side from an electrical substation with primary 115 kV ; 63 MVA',
    mpf( '2.5e4' )      : 'the charge used by a Lorentz force can crusher pinch',
    mpf( '1.00e5' )     : 'the low range of Birkeland current which creates Earth\'s aurorae',
    mpf( '1.40e5' )     : 'the "Sq" current of one daytime vortex within the ionospheric dynamo region',
    mpf( '1.0e6' )      : 'the high range of Birkeland current which creates Earth\'s aurorae',
    mpf( '5.0e6' )      : 'the current of the flux tube between Jupiter and Io',
    mpf( '2.7e7' )      : 'the Sandia National Laboratories, Z machine firing current since 2007',
    mpf( '2.56e8' )     : 'the current produced in explosive flux compression generator (VNIIEF laboratories, Russia)',
    mpf( '3.0e9' )      : 'the total current in the Sun\'s heliospheric current sheet',
    mpf( '3.0e18' )     : 'the current of a 2 kpc segment of the 50 kpc-long radio jet of the Seyfert galaxy 3C 303',
    mpf( '3.479e25' )   : 'the Planck current',
}


#//******************************************************************************
#//
#//  dataRateTable
#//
#//  bits/second : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28bit_rate%29
#//
#//******************************************************************************

dataRateTable = {
    mpf( '5.0e-2' )     : 'the Project ELF bit rate for transmitting 3-letter codes to US nuclear submarines',
    mpf( '5.0e1' )      : 'the data rate for transmissions from GPS satellites',
    mpf( '5.6e1' )      : 'the data rate for a skilled operator in Morse code',
    mpf( '4.0e3' )      : 'the minimum data rate achieved for encoding recognizable speech (using special-purpose speech codecs)',
    mpf( '8.0e3' )      : 'the data rate of low-bitrate telephone quality',
    mpf( '3.2e4' )      : 'the data rate of MW quality and ADPCM voice in telephony',
    mpf( '5.6e4' )      : 'the data rate of 56kbit modem',
    mpf( '6.4e4' )      : 'the data rate of an ISDN B channel or best quality, uncompressed telephone line',
    mpf( '1.92e5' )     : 'the data rate for "nearly CD quality" for a file compressed in the MP3 format',
    mpf( '1.4112e6' )   : 'the data rate of CD audio (uncompressed, 16-bit samples x 44.1 kHz x 2 channels)',
    mpf( '1.536e6' )    : 'the data rate of 24 channels of telephone in the US, or a good VTC T1',
    mpf( '2e6' )        : 'the data rate of 30 channels of telephone audio or a Video Tele-Conference at VHS quality',
    mpf( '8e6' )        : 'the data rate of DVD quality video',
    mpf( '1e7' )        : 'the data rate of classic Ethernet: 10BASE2, 10BASE5, 10BASE-T',
    mpf( '1e7' )        : 'the data rate that the human retina transmits data to the brain, according to research',
    mpf( '2.7e7' )      : 'the data rate of HDTV quality video',
    mpf( '4.8e8' )      : 'the data rate of USB 2.0 High-Speed (interface signalling rate)',
    mpf( '7.86e8' )     : 'the data rate of FireWire IEEE 1394b-2002 S800',
    mpf( '9.5e8' )      : 'the data rate of a harddrive read, Samsung SpinPoint F1 HD103Uj',
    mpf( '1e9' )        : 'the data rate of Gigabit Ethernet',
    mpf( '1.067e9' )    : 'the data rate of Parallel ATA UDMA 6; conventional PCI 32 bit 33 MHz - 133 MB/s',
    mpf( '1.244e9' )    : 'the data rate of OC-24, a 1.244 Gbit/s SONET data channel',
    mpf( '1.5e9' )      : 'the data rate of SATA 1.5Gbit/s - First generation (interface signaling rate)',
    mpf( '3e9' )        : 'the data rate of SATA 3Gbit/s - Second generation (interface signaling rate)',
    mpf( '5e9' )        : 'the data rate of USB 3.0 SuperSpeed',
    mpf( '6e9' )        : 'the data rate of SATA 6Gbit/s - Third generation (interface signaling rate)',
    mpf( '8.533e9' )    : 'the data rate of PCI-X 64 bit 133 MHz - 1,067 MB/s',
    mpf( '9.953e9' )    : 'the data rate of OC-192, a 9.953 Gbit/s SONET data channel',
    mpf( '1.0e10' )     : 'the data rate of the Thunderbolt interface standard',
    mpf( '1.0e10' )     : 'the data rate of 10 Gigabit Ethernet',
    mpf( '1.0e10' )     : 'the data rate of USB 3.1 SuperSpeed 10 Gbit/s',
    mpf( '3.9813e10' )  : 'the data rate of OC-768, a 39.813 Gbit/s SONET data channel, the fastest in current use',
    mpf( '4.0e10' )     : 'the data rate of 40 Gigabit Ethernet',
    mpf( '8e10' )       : 'the data rate of PCI Express x16 v2.0',
    mpf( '9.6e10' )     : 'the data rate of InfiniBand 12X QDR',
    mpf( '1.0e11' )     : 'the data rate of 100 Gigabit Ethernet',
    mpf( '1.28e11' )    : 'the data rate for PCI Express x16 v3.0',
    mpf( '1.28e12' )    : 'a SEA-ME-WE 4 submarine communications cable - 1.28 terabits per second',
    mpf( '3.84e12' )    : 'a I-ME-WE submarine communications cable - design capacity of 3.84 terabits per second',
    mpf( '2.45e14' )    : 'the projected average global internet traffic in 2015 according to Cisco\'s 2011 VNI IP traffic forecast',
    mpf( '1.050e15' )   : 'the data rate over a 14 transmission core optical fiber developed by NEC and Corning researchers',
}


#//******************************************************************************
#//
#//  electricalConductanceTable
#//
#//  mhos : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28resistance%29
#//
#//******************************************************************************

electricalConductanceTable = {
}


#//******************************************************************************
#//
#//  electricalPotentialTable
#//
#//  volts : description
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28voltage%29
#//
#//******************************************************************************

electricPotentialTable = {
    mpf( '5.0e-7' )     : 'the change in nerve cell potential caused by opening a single acetylcholine receptor channel (500 nV)',
    mpf( '2.0e-6' )     : 'the voltage of noise in an EEG taken at the scalp (2 uV)',
    mpf( '1.0e-5' )     : 'the minimum peak-to-peak amplitude of an average EEG taken at the scalp (10 uV)',
    mpf( '1.5e-5' )     : 'the minimum terrestrial digital-TV RF antenna signal (-85 dBm over 75 ohms)',
    mpf( '5.6e-5' )     : 'the minimum terrestrial analog-TV RF antenna signal (35 dB[uV])',
    mpf( '1.0e-4' )     : 'the maximum peak-to-peak amplitude of an average EEG taken at the scalp (100 uV)',
    mpf( '7.5e-2' )     : 'the nerve cell resting potential (75 mV)',
    mpf( '0.316' )      : 'the typical voltage reference level in consumer audio electronics (0.316 V rms)',
    mpf( '0.9' )        : 'the voltage of a lemon battery cell (made with copper and zinc electrodes)',
    mpf( '1.5' )        : 'the voltage of an alkaline AA, AAA, C or D battery',
    mpf( '5' )          : 'the voltage of USB power, used for example to charge a cell phone or a digital camera',
    mpf( '6' )          : 'a common voltage for medium-size electric lanterns (6 V)',
    mpf( '12' )         : 'the typical car battery (12 V)',
    mpf( '110' )        : 'the typical domestic wall socket voltage (110 V)',
    mpf( '600' )        : 'the voltage an electric eel sends in an average attack',
    mpf( '630' )        : 'the voltage in London Underground railway tracks',
    mpf( '2450' )       : 'the voltage used for electric chair execution in Nebraska',
    mpf( '3300 ' )      : 'a common early urban distribution voltage for grid electricity in the UK (3.3 kV)',
    mpf( '1.0e4' )      : 'an electric fence (10kV)',
    mpf( '1.5e4' )      : '15 kV AC railway electrification overhead lines, 162/3 Hz',
    mpf( '2.5e4' )      : 'European high-speed train overhead power lines (25 kV)',
    mpf( '3.45e4' )     : 'the voltage in North America for power distribution to end users (34.5 kV)',
    mpf( '2.3e5' )      : 'the highest voltage used in North American power high-voltage transmission substations (230 kV)',
    mpf( '3.45e5' )     : 'the lowest voltage used in EHV power transmission systems (345 kV)',
    mpf( '8.0e5' )      : 'the lowest voltage used by ultra-high voltage (UHV) power transmission systems (800 kV)',
    mpf( '3.0e6' )      : 'the voltage used by the ultra-high voltage electron microscope at Osaka University',
    mpf( '2.55e7' )     : 'the largest man-made voltage - produced in a Van de Graaff generator at Oak Ridge National Laboratory',
    mpf( '1.0e8' )      : 'the potential difference between the ends of a typical lightning bolt',
    mpf( '7.0e15' )     : 'the voltage around a particular energetic highly magnetized rotating neutron star',
    mpf( '1.04e27' )    : 'the Planck voltage',
}


#//******************************************************************************
#//
#//  electricalResistanceTable
#//
#//  ohms : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28resistance%29
#//
#//******************************************************************************

electricalResistanceTable = {
}


#//******************************************************************************
#//
#//  energyTable
#//
#//  joules : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28energy%29
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28specific_energy%29
#//  https://en.wikipedia.org/wiki/Energy_density
#//
#//******************************************************************************

energyTable = {
}


#//******************************************************************************
#//
#//  forceTable
#//
#//  newtons : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28force%29
#//
#//******************************************************************************

forceTable = {
}


#//******************************************************************************
#//
#//  illuminanceTable
#//
#//  lux : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28illuminance%29
#//
#//******************************************************************************

illuminanceTable = {
    mpf( '1.0e-4' )     : 'starlight on an overcast, moonless night sky',
    mpf( '1.4e-4' )     : 'Venus at its brightest',
    mpf( '2.0e-4' )     : 'starlight on a clear, moonless night sky, excluding airglow',
    mpf( '2.0e-3' )     : 'starlight on a clear, moonless night sky, including airglow',
    mpf( '1.0e-2' )     : 'the quarter Moon',
    mpf( '2.5e-2' )     : 'the full Moon on a clear night',
    mpf( '1' )          : 'the extreme of darkest storm clouds at sunset/sunrise',
    mpf( '40' )         : 'a fully overcast sky at sunset/sunrise',
    mpf( '200' )        : 'the extreme of darkest storm clouds at midday',
    mpf( '400' )        : 'sunrise or sunset on a clear day',
    mpf( '25000' )      : 'typical overcast day at midday',
    mpf( '120000' )     : 'the brightest sunlight',
}


#//******************************************************************************
#//
#//  inductanceTable
#//
#//  henries : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28inductance%29
#//
#//******************************************************************************

inductanceTable = {
    mpf( '1.0e-9' )     : 'a thin film chip inductor, 1.6x0.8 mm with a typical power rating of 0.1 W (range: 1-100 nH)',
    mpf( '5.25e-7' )    : 'the inductance of one meter of Cat-5 cable pair',
    mpf( '5.0e-5' )     : 'a coil with 99 turns, 0.635 cm long with a diameter of 0.635 cm',
    mpf( '1.0e-3' )     : 'a coil 2.2 cm long with a diameter of 1.6 cm with 800 mA capability, used in kW amplifiers',
    mpf( '1.0' )        : 'an inductor a few cm long and a few cm in diameter with many turns of wire on a ferrite core',
    mpf( '11' )         : 'a mains electricity transformer primary at 120 V (range: 8-11 H)',
    mpf( '1.326e3' )    : '500 kV, 3000 MW power line transformer primary winding',
}


#//******************************************************************************
#//
#//  informationEntropyTable
#//
#//  bits : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28data%29
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28entropy%29
#//
#//******************************************************************************

informationEntropyTable = {
}


#//******************************************************************************
#//
#//  lengthTable
#//
#//  meters : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28length%29
#//  https://en.wikipedia.org/wiki/List_of_examples_of_lengths
#//
#//******************************************************************************

lengthTable = {
    mpf( '1.78' )       : 'the height of a typical adult male human',
    mpf( '91.44' )      : 'the length of a football field',
    mpf( '42194.988' )  : 'a marathon',
    mpf( '3983126.34' ) : 'the distance from New York to Los Angeles',
    mpf( '12756272' )   : 'the diameter of the Earth',
    mpf( '142984000' )  : 'the diameter of Jupiter',
    mpf( '1391980000' ) : 'the diameter of the Sun',
    mpf( '1.49598e11' ) : 'the distance from the Earth to the Sun',
    mpf( '4.01135e16' ) : 'the distance to the closest star, Proxima Centauri',
}


#//******************************************************************************
#//
#//  luminanceTable
#//
#//  candelas/meter^2 : description
#//
#//  https://en.wikipedia.org/wiki/Luminance
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28luminance%29
#//
#//******************************************************************************

luminanceTable = {
    mpf( '1.0e-6' ) : 'the absolute threshold of human vision',
    mpf( '4.0e-4' ) : 'the darkest sky',
    mpf( '1.0e-3' ) : 'a typical night sky',
    mpf( '1.4e-3' ) : 'a typical photographic scene lit by full moon',
    mpf( '5.0e-3' ) : 'the approximate scotopic/mesopic threshold',
    mpf( '4.0e-2' ) : 'the phosphorescent markings on a watch dial after 1 h in the dark',
    mpf( '2' )      : 'floodlit buildings, monuments, and fountains',
    mpf( '5' )      : 'the approximate mesopic/photopic threshold',
    mpf( '25' )     : 'a typical photographic scene at sunrise or sunset',
    mpf( '30' )     : 'a green electroluminescent source',
    mpf( '55' )     : 'the standard SMPTE cinema screen luminance',
    mpf( '80' )     : 'the monitor white in the sRGB reference viewing environment',
    mpf( '250' )    : 'the peak luminance of a typical LCD monitor',
    mpf( '700' )    : 'a typical photographic scene on overcast day',
    mpf( '2000' )   : 'an average cloudy sky',
    mpf( '2500' )   : 'the Moon\'s surface',
    mpf( '5000' )   : 'a typical photographic scene in full sunlight',
    mpf( '7000' )   : 'an average clear sky',
    mpf( '1.0e4' )  : 'a white illuminated cloud',
    mpf( '1.2e4' )  : 'a fluorescent lamp',
    mpf( '7.5e4' )  : 'a low pressure sodium-vapor lamp',
    mpf( '1.3e5' )  : 'a frosted incandescent light bulb',
    mpf( '6.0e5' )  : 'the solar disk at the horizon',
    mpf( '7.0e6' )  : 'the filament of a clear incandescent lamp',
    mpf( '1.0e8' )  : 'brightness which can cause retinal damage',
    mpf( '1.6e9' )  : 'the solar disk at noon',
}


#//******************************************************************************
#//
#//  luminousFluxTable
#//
#//  lumens : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28luminous_flux%29
#//
#//******************************************************************************

luminousFluxTable = {
    mpf( '0.025' )      : 'the light of a firefly',
    mpf( '12.57' )      : 'the light of a candle',
    mpf( '780' )        : 'a 60 W incandescent light bulb',
    mpf( '930' )        : 'a 75 W incandescent light bulb',
    mpf( '2990' )       : 'a 200 W incandescent light bulb',
    mpf( '6.0e5' )      : 'an IMAX projector bulb',
    mpf( '4.23e10' )    : 'the Luxor Sky Beam spotlight array in Las Vegas',
    mpf( '4.6e24' )     : 'the dimmest class of red dwarf star',
    mpf( '3.0768e28' )  : 'the Sun',
    mpf( '1.382e38' )   : 'a Type 1a supernova',
    mpf( '1.26e41' )    : 'Quasar 3C 273',
}


#//******************************************************************************
#//
#//  luminousIntensityTable
#//
#//  candelas : description
#//
#//  https://en.wikipedia.org/wiki/Candela#Examples
#//
#//******************************************************************************

luminousIntensityTable = {
}


#//******************************************************************************
#//
#//  magneticFieldStrengthTable
#//
#//  amperes/meter : description
#//
#//******************************************************************************

magneticFieldStrengthTable = {
}


#//******************************************************************************
#//
#//  magneticFluxTable
#//
#//  webers : description
#//
#//******************************************************************************

magneticFluxTable = {
}


#//******************************************************************************
#//
#//  magneticFluxDensityTable
#//
#//  teslas : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28magnetic_field%29
#//
#//******************************************************************************

magneticFluxDensityTable = {
    mpf( '5e-18' )      : 'the precision attained for Gravity Probe B',
    mpf( '3.1869e-5' )  : 'the Earth\'s magnetic field at 0 degrees long., 0 degrees lat.',
    mpf( '5.0e-3' )     : 'a typical refrigerator magnet',
    mpf( '0.3' )        : 'the strength of solar sunspots',
    mpf( '3' )          : 'the maximum strength of a common magnetic resonance imaging system',
    mpf( '16' )         : 'a magnetic field strong enough to levitate a frog',
    mpf( '2800' )       : 'the largest magnetic field produced in a laboratory',
    mpf( '1.0e8' )      : 'the lower range for the magnetic field strength in a magnetar',
    mpf( '1.0e11' )     : 'the upper range for the magnetic field strength in a magnetar',
}


#//******************************************************************************
#//
#//  massTable
#//
#//  grams : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28mass%29
#//
#//******************************************************************************

massTable = {
    mpf( '0.003' )      : 'an average ant',
    mpf( '17.5' )       : 'a typical mouse',
    mpf( '7.0e4' )      : 'an average human',
    mpf( '5.5e6' )      : 'an average male African bush elephant',
    mpf( '4.39985e8' )  : 'the takeoff weight of a Boeing 747-8',
    mpf( '5.9742e27' )  : 'the Earth',
}


#//******************************************************************************
#//
#//  powerTable
#//
#//  watts : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28power%29
#//
#//******************************************************************************

powerTable = {
}


#//******************************************************************************
#//
#//  pressureTable
#//
#//  pascals : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28pressure%29
#//  https://en.wikipedia.org/wiki/Sound_pressure
#//
#//******************************************************************************

pressureTable = {

    mpf( '1.0e-17' )    : 'the estimated pressure in outer space in intergalactic voids',
    mpf( '5.0e-15' )    : 'typical pressure in outer space between stars in the Milky Way',
    mpf( '1.0e-12' )    : 'the lowest pressure obtained in laboratory conditions (1 picopascal)',
    mpf( '4.0e-11' )    : 'the atmosphere pressure of the Moon at lunar day, very approximately (40 picopascals)',
    mpf( '1.0e-10' )    : 'the atmospheric pressure of Mercury, very approximately (100 pPa)',
    mpf( '8.0e-10' )    : 'the atmospheric pressure of the Moon at lunar night, very approximately (800 pPa)',
    mpf( '1.0e-9' )     : 'the vacuum expected in the beam pipe of the Large Hadron Collider\'s Atlas experiment (< 1 nPa)',
    mpf( '1.0e-9' )     : 'the approximate solar wind pressure at Earth\'s distance from the Sun',
    mpf( '1.0e-8' )     : 'the pressure inside a vacuum chamber for laser cooling of atoms (magneto-optical trap, 10 nPa)',
    mpf( '1.0e-7' )     : 'the highest pressure still considered ultra high vacuum (100 nPa)',
    mpf( '1.0e-6' )     : 'the pressure inside a vacuum tube, very approximate, (1 uPa)',
    mpf( '1.0e-6' )     : 'the radiation pressure of sunlight on a perfectly reflecting surface at the distance of the Earth',
    mpf( '2.0e-5' )     : 'the reference pressure for sound in air, and the threshold of human hearing (0 dB)',
    mpf( '1.0e-1' )     : 'the upper limit of high vacuum (100 mPa)',
    mpf( '2.0e-1' )     : 'the atmospheric pressure on Pluto (1988 figure; very roughly, 200 mPa)',
    mpf( '1' )          : 'the pressure exerted by a US dollar bill resting flat on a surface',
    mpf( '10' )         : 'the pressure increase per millimeter of a water column at Earth mean sea level',
    mpf( '10' )         : 'the pressure due to direct impact of a gentle breeze (~9 mph or 14 km/h)',
    mpf( '86' )         : 'the pressure from the weight of a U.S. penny lying flat',
    mpf( '100' )        : 'the pressure due to direct impact of a strong breeze (~28 mph or 45 km/h)',
    mpf( '120' )        : 'the pressure from the weight of a U.S. quarter lying flat',
    mpf( '133.3224' )   : '1 torr ~= 1 mmHg (133.3224 pascals)',
    mpf( '300' )        : 'the lung air pressure difference moving the normal breaths of a person (only 0.3% of standard atmospheric pressure)',
    mpf( '610' )        : 'the partial vapour pressure at the triple point of water (611.73 Pa)',
    mpf( '650' )        : 'a typical atmospheric pressure on Mars, < 1% of atmospheric sea-level pressure on Earth',
    mpf( '2.0e3' )      : 'the pressure of popping popcorn (very approximate)',
    mpf( '2.6e3' )      : 'the pressure to make water boil at room temperature (22 degrees C) (0.38 psi, 20 mmHg)',
    mpf( '5.0e3' )      : 'the blood pressure fluctuation (40 mmHg) between heartbeats for a typical healthy adult (0.8 psi)',
    mpf( '6.3e3' )      : 'the pressure where water boils at normal human body temperature (37 degrees C), the pressure below which humans absolutely cannot survive (Armstrong Limit), 0.9 psi',
    mpf( '9.8e3' )      : 'the lung pressure that a typical person can exert (74 mmHg, 1.4 psi)',
    mpf( '1.0e4' )      : 'the pressure increase per meter of a water column',
    mpf( '1.0e4' )      : 'the decrease in air pressure when going from Earth sea level to 1000 m elevation',
    mpf( '1.3e4' )      : 'the pressure for human lung, measured for trumpet player making staccato high notes (1.9 psi)',
    mpf( '1.6e4' )      : 'the systolic blood pressure in a healthy adult while at rest (< 120 mmHg gauge pressure)',
    mpf( '1.93e4' )     : 'the high end of lung pressure, exertable without injury by a healthy person for brief times (2.8 psi)',
    mpf( '3.4e4' )      : 'the level of long-duration blast overpressure (from a large-scale explosion) that would cause most buildings to collapse (5 psi)',
    mpf( '7.0e4' )      : 'the pressure inside an incandescent light bulb',
    mpf( '8.0e4' )      : 'the pressure inside vacuum cleaner at sea level on Earth (80% of standard atmospheric pressure, 11.6 psi)',
    mpf( '8.7e4' )      : 'the record low atmospheric pressure for typhoon/hurricane (Typhoon Tip in 1979) (only 86% of standard atmospheric pressure, 12.6 psi)',
    mpf( '1.0e5' )      : '1 bar (14.5 psi), approximately equal to the weight of one kilogram (1 kilopond) acting on one square centimeter',
    mpf( '3.5e5 ' )     : 'typical impact pressure of a fist punch (approximate)',
    mpf( '2.0e5' )      : 'typical air pressure in an automobile tire relative to atmosphere (30 psi gauge pressure)',
    mpf( '3.0e5' )      : 'the water pressure of a garden hose (50 psi)',
    mpf( '5.17e5' )     : 'the carbon dioxide pressure in a champagne bottle',
    mpf( '5.2e5' )      : 'the partial vapour pressure at the triple point of carbon dioxide (75 psi)',
    mpf( '7.6e5' )      : 'the air pressure in a heavy truck/bus tire relative to atmosphere (110 psi gauge pressure)',
    mpf( '8.0e5' )      : 'the vapor pressure of water in a kernel of popcorn when the kernel ruptures',
    mpf( '1.1e6' )      : 'pressure of an average human bite (162 psi)',
    mpf( '2.0e6' )      : 'maximum typical pressure used in boilers of steam locomotives (290 psi)',
    mpf( '5.0e6' )      : 'the maximum rated pressure for the Seawold class military nuclear submarine (estimated), at a depth of 500 m (700 psi)',
    mpf( '9.2e6' )      : 'the atmospheric pressure of Venus (92 bar, 1,300 psi)',
    mpf( '1.0e7' )      : 'the pressure exerted by a 45 kg woman wearing stiletto heels when a heel hits the floor (1,450 psi)',
    mpf( '1.5e7' )      : 'the power stroke maximum pressure in diesel truck engine when burning fuel (2,200 psi)',
    mpf( '2.0e7' )      : 'the typical pressure used for hydrogenolysis reactions (2,900 psi)',
    mpf( '2.1e7' )      : 'the pressure of a typical aluminium scuba tank of pressurized air (210 bar, 3,000 psi)',
    mpf( '2.8e7' )      : 'the Overpressure caused by the bomb explosion during the Oklahoma City bombing',
    mpf( '6.9e7' )      : 'the water pressure withstood by the DSV Shinkai 6500 in visiting ocean depths of > 6500 meters (10,000 psi)',
    mpf( '1.1e8' )      : 'the pressure at bottom of Mariana Trench, about 11 km below ocean surface (1,100 bar, 16,000 psi)',
    mpf( '2.0e8' )      : 'the approximate pressure inside a reactor for the synthesis of high-pressure polyethylene (HPPE)',
    mpf( '2.8e8' )      : 'the maximum chamber pressure during a pistol firing (40,000 psi)',
    mpf( '4.0e8' )      : 'the chamber pressure of a late 1910s .50 Browning Machine Gun discharge (58,000 psi)',
    mpf( '6.2e8' )      : 'the water pressure used in a water jet cutter (90,000 psi)',
    mpf( '1.0e9' )      : 'the pressure of extremely high-pressure chemical reactors (10 kbar)',
    mpf( '1.5e9' )      : 'the pressure at which diamond melts using a 3 kJ laser without turning into graphite first',
    mpf( '1.5e9' )      : 'the tensile strength of Inconel 625 according to Aircraft metal strength tables and the Mil-Hdbk-5 (220,000 psi)',
    mpf( '5.8e9' )      : 'the ultimate tensile strength of the polymer Zylon (840,000 psi)',
    mpf( '1.0e10' )     : 'the pressure at which octaoxygen forms at room temperature (100,000 bar)',
    mpf( '1.8e10' )     : 'the pressure needed for the first commercially successful synthesis of diamond',
    mpf( '2.4e10' )     : 'the lower range of stability for enstatite in its perovskite-structured polymorph, possibly the most common mineral inside the Earth',
    mpf( '1.1e11' )     : 'the upper range of stability for enstatite in its perovskite-structured polymorph, possibly the most common mineral inside the Earth',
    mpf( '4.0e10' )     : 'the quantum mechanical electron degeneracy pressure in a block of copper',
    mpf( '4.8e10' )     : 'the detonation pressure of pure CL-20, the most powerful high explosive in mass production',
    mpf( '6.9e10' )     : 'the highest water jet pressure made in research lab (approx. 1 million psi)',
    mpf( '9.6e10' )     : 'the pressure at which metallic oxygen forms (960,000 bar)',
    mpf( '1.0e11' )     : 'the theoretical tensile strength of a carbon nanotube (CNT)',
    mpf( '1.3e11' )     : 'the intrinsic strength of monolayer graphene',
    mpf( '3.0e11' )     : 'the pressure attainable with a diamond anvil cell',
    mpf( '3.6e11' )     : 'the pressure inside the core of the Earth (3.64 million bar)',
    mpf( '5.4e14' )     : 'the pressure inside an Ivy Mike-like nuclear bomb detonation (5.3 billion bar)',
    mpf( '6.5e15' )     : 'the pressure inside a W80 nuclear warhead detonation (64 billion bar)',
    mpf( '2.5e16' )     : 'the pressure inside the core of the Sun (250 billion bar)',
    mpf( '5.7e16' )     : 'the pressure inside a uranium nucleus (8 MeV in a sphere of radius 175 pm)',
    mpf( '1.0e34' )     : 'the Pressure range inside a neutron star (0.3 to 1.6 x 10^34)',
    mpf( '4.6e113' )    : 'the Planck pressure',
}\


#//******************************************************************************
#//
#//  radiationAbsorbedDoseTable
#//
#//  grays : description
#//
#//******************************************************************************

radiationAbsorbedDoseTable = {
}


#//******************************************************************************
#//
#//  radiationEquivalentDoseTable
#//
#//  sieverts : description
#//
#//  https://en.wikipedia.org/wiki/Sievert
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28radiation%29
#//
#//******************************************************************************

radiationEquivalentDoseTable = {
}


#//******************************************************************************
#//
#//  radiationExposureTable
#//
#//  coulombs/gram : description
#//
#//******************************************************************************

radiationExposureTable = {
}


#//******************************************************************************
#//
#//  radioactivityTable
#//
#//  becquerels : description
#//
#//  https://en.wikipedia.org/wiki/List_of_radioactive_isotopes_by_half-life
#//
#//******************************************************************************

radioactivityTable = {
}


#//******************************************************************************
#//
#//  solidAngleTable
#//
#//  steradians : description
#//
#//  https://en.wikipedia.org/wiki/Solid_angle
#//
#//******************************************************************************

solidAngleTable = {
}


#//******************************************************************************
#//
#//  temperatureTable
#//
#//  kelvins : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28temperature%29
#//
#//******************************************************************************

temperatureTable = {
    mpf( '1e-10' )          : 'the lowest temperature ever produced in a laboratory',
    mpf( '5e-8' )           : 'the Fermi temperature of potassium-40',
    mpf( '1e-6' )           : 'the temperature produced by nuclear demagnetrization refrigeration',
    mpf( '1.7e-3' )         : 'the temperature record for helium-3/helium-4 dliution refrigeration',
    mpf( '9.5e-1' )         : 'the melting point of helium',
    mpf( '2.725' )          : 'the temperature of the cosmic microwave background',
    mpf( '14.01' )          : 'the melting point of hydrogen',
    mpf( '44' )             : 'the mean temperature on Pluto',
    mpf( '183.9' )          : 'the coldest air recorded on Earth (Vostok Station, Antarctica)',
    mpf( '210' )            : 'the mean temperature on Mars',
    mpf( '234.3' )          : 'the melting point of mercury',
    mpf( '273.15' )         : 'the melting point of water',
    mpf( '287' )            : 'the mean temperature of Earth',
    mpf( '330' )            : 'the average body temperature for a human',
    mpf( '319.3' )          : 'the hottest temperature recorded on Earth (Death Valley)',
    mpf( '373.15' )         : 'the boiling point of water',
    mpf( '450' )            : 'the mean temperature on Mercury',
    mpf( '600.65' )         : 'the melting point of lead',
    mpf( '740' )            : 'the mean temperature on Venus',
    mpf( '933.47' )         : 'the melting point of aluminum',
    mpf( '1170' )           : 'the temperature of a wood fire',
    mpf( '1811' )           : 'the melting point of iron',
    mpf( '2022' )           : 'the boiling point of lead',
    mpf( '3683' )           : 'the melting point of tungsten',
    mpf( '5780' )           : 'the surface temperature of the Sun',
    mpf( '1.6e5' )          : 'the surface temperature of the hottest white dwarfs',
    mpf( '1.56e7' )         : 'the core temperature of the Sun',
    mpf( '2.3e7' )          : 'the temperature at which beryllium-7 can fuse',
    mpf( '2.3e8' )          : 'the temperature at which carbon-12 can fuse',
    mpf( '7.5e8' )          : 'the temperature at which oxygen can fuse',
    mpf( '1.0e10' )         : 'the temperature of a supernova',
    mpf( '7.0e11' )         : 'the temperature of a quasar\'s accretion disk',
    mpf( '6.7e13' )         : 'the temperature of gamma-ray burst from a collapsar',
    mpf( '2.8e15' )         : 'the temperature of an electroweak star',
    mpf( '1.0e21' )         : 'the temperature of dark matter in active galactic nuclei',
    mpf( '1.0e30' )         : 'the Hagedorn temperature, the highest possible temperature according to string theory',
    mpf( '1.416785e32' )    : 'the Planck temperature, at which the wavelength of black body radiation' + \
                              'reaches the Planck length',
    mpf( '1.0e33' )         : 'the Landau pole, the maximum theoretical temperature according to QED',
}


#//******************************************************************************
#//
#//  timeTable
#//
#//  seconds : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28frequency%29
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28time%29
#//
#//******************************************************************************

timeTable = {
    mpf( '5.39106e-44' )    : 'the Planck time',
    mpf( '1.35135e-6' )     : 'the clock cycle of the Intel 4004 microprocessor (1971)',
    mpf( '60' )             : 'one minute (60 seconds)',
    mpf( '3600' )           : 'one hour (60 minutes)',
    mpf( '86400' )          : 'one day (24 hours)',
    mpf( '604800' )         : 'one week (7 days)',
    mpf( '2551442.8016' )   : 'the synodic lunar month',
    mpf( '3.15576e7' )      : 'one Julian year (365.25 days)',
    mpf( '3.15576e8' )      : 'one decade (10 years)',
    mpf( '3.15576e9' )      : 'one century (100 years)',
    mpf( '3.15576e10' )     : 'one millennium (1000 years)',
}


#//******************************************************************************
#//
#//  velocityTable
#//
#//  meters/second : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28speed%29
#//
#//******************************************************************************

velocityTable = {
    mpf( '2.2e-18' )    : 'the expansion rate between 2 points in free space 1 meter apart under Hubble\'s law',
    mpf( '3.0e-9' )     : 'the upper range of the typical relative speed of continental drift',
    mpf( '1.4e-5' )     : 'the growth rate of bamboo, the fastest-growing woody plant, over 24 hours',
    mpf( '0.00275' )    : 'the world record speed of the fastest snail',
    mpf( '0.080' )      : 'the top speed of a sloth',
    mpf( '30' )         : 'the typical speed of a car on the freeway',
    mpf( '130' )        : 'the wind speed of a powerful tornado',
    mpf( '250' )        : 'the typical cruising speed of a modern jet airliner',
    mpf( '343' )        : 'the speed of sound (in dry air at sea level at 20 degrees C)',
    mpf( '981' )        : 'the top speed of the SR-71 Blackbird',
    mpf( '3373' )       : 'the speed of the X-43 rocket/scramjet plane',
    mpf( '11107' )      : 'the speed of Apollo 10, the high speed record for a manned vehicle',
    mpf( '11200' )      : 'the escape velocity from Earth',
    mpf( '29800' )      : 'the speed of the Earth in orbit around the Sun',
    mpf( '2.0e5' )      : 'the orbital speed of the Solar System in the Milky Way galaxy',
    mpf( '5.52e5' )     : 'the speed of the Milky Way, relative to the cosmic microwave background',
    mpf( '1.4e7' )      : 'the typical speed of a fast neutron',
    mpf( '3.0e7' )      : 'the typical speed of an electron in a cathode ray tube',
}


#//******************************************************************************
#//
#//  volumeTable
#//
#//  liters : description
#//
#//  https://en.wikipedia.org/wiki/Orders_of_magnitude_%28volume%29
#//
#//******************************************************************************

volumeTable = {
    mpf( '4.22419e-102' )   : 'the Planck volume',
    mpf( '9.4e-41' )        : 'the classical volume of an electron',
    mpf( '1.5e-38' )        : 'the volume of a proton',
    mpf( '6.54e-29' )       : 'the volume of a hydrogen atom',
    mpf( '9e-14' )          : 'the volume of a human red blood cell',
    mpf( '1.3e-10' )        : 'the volume of a very fine grain of sand',
    mpf( '6.2e-8' )         : 'the volume of a medium grain of sand',
    mpf( '4.0e-6' )         : 'the volume of a large grain of sand',
    mpf( '0.0049' )         : 'a teaspoon',
    mpf( '3.785' )          : 'a gallon',
    mpf( '1000' )           : 'a cubic meter',
    mpf( '11000' )          : 'the approximate volume of an elephant',
    mpf( '38500' )          : 'a 20-foot shipping container',
    mpf( '2.5e6' )          : 'an Olympic-sized swimming pool',
    mpf( '3.0e14' )         : 'the estimated volume of crude oil on Earth',
    mpf( '1.2232e16' )      : 'the volume of Lake Superior',
    mpf( '2.6e18' )         : 'the volume of Greenland ice cap',
    mpf( '1.4e21' )         : 'the volume of water in all of Earth\'s oceans',
    mpf( '1.08e24' )        : 'the volume of the Earth',
    mpf( '1.e27' )          : 'the volume of Jupiter',
    mpf( '1.e30' )          : 'the volume of the Sun',
    mpf( '2.75e38' )        : 'the volume of the star Betelgeuse',
    mpf( '3.3e64' )         : 'the volume of the Milky Way',
    mpf( '3.4e83' )         : 'the approxmimate volume of the observable universe',
}

