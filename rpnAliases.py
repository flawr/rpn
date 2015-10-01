#!/usr/bin/env python

# //******************************************************************************
# //
# //  rpnAliases.py
# //
# //  RPN command-line calculator alias declarations
# //  copyright (c) 2015 (1988), Rick Gutleber (rickg@his.com)
# //
# //  License: GNU GPL 3.0 (see <http://www.gnu.org/licenses/gpl.html> for more
# //  information).
# //
# //******************************************************************************

# //******************************************************************************
# //
# //  operatorAliases
# //
# //******************************************************************************

operatorAliases = {
    '!!'                : 'double_factorial',
    '!'                 : 'factorial',
    '!='                : 'not_equal',
    '%'                 : 'modulo',
    '*'                 : 'multiply',
    '**'                : 'power',
    '***'               : 'tetrate',
    '+'                 : 'add',
    '-'                 : 'subtract',
    '-c'                : 'comma_mode',
    '-i'                : 'identify_mode',
    '-o'                : 'octal_mode',
    '-t'                : 'timer_mode',
    '-x'                : 'hex_mode',
    '-z'                : 'leading_zero_mode',
    '/'                 : 'divide',
    '//'                : 'root',
    '1/x'               : 'reciprocal',
    '2-nacci'           : 'fibonacci',
    '3-nacci'           : 'tribonacci',
    '4-nacci'           : 'tetranacci',
    '5-nacci'           : 'pentanacci',
    '6-nacci'           : 'hexanacci',
    '7-nacci'           : 'heptanacci',
    '<'                 : 'less',
    '<<'                : 'shift_left',
    '<='                : 'not_greater',
    '=='                : 'equal',
    '>'                 : 'greater',
    '>='                : 'not_less',
    '>>'                : 'shift_right',
    '?'                 : 'help',
    'add_dig'           : 'add_digits',
    'add_digit'         : 'add_digits',
    'altfac'            : 'alternating_factorial',
    'altsign'           : 'alternate_signs',
    'altsign2'          : 'alternate_signs_2',
    'alt_fac'           : 'alternating_factorial',
    'alt_sign'          : 'alternate_signs',
    'alt_sign2'         : 'alternate_signs_2',
    'aperynum'          : 'nth_apery',
    'arccosecant'       : 'acsc',
    'arcosine'          : 'acos',
    'arcotangent'       : 'acot',
    'arcsecant'         : 'asec',
    'arcsine'           : 'asin',
    'arctangent'        : 'atan',
    'arg'               : 'argument',
    'args'              : 'arguments',
    'arithmean'         : 'mean',
    'ashwed'            : 'ash_wednesday',
    'ashwednesday'      : 'ash_wednesday',
    'ash_wed'           : 'ash_wednesday',
    'astro_dawn'        : 'astronomical_dawn',
    'astro_dusk'        : 'astronomical_dusk',
    'autumn'            : 'autumnal_equinox',
    'autumnal'          : 'autumnal_equinox',
    'average'           : 'mean',
    'avg'               : 'mean',
    'bal'               : 'balanced_prime',
    'bal?'              : 'balanced_prime?',
    'balanced'          : 'balanced_prime',
    'balanced?'         : 'balanced_prime?',
    'balanced_'         : 'balanced_prime_',
    'bal_'              : 'balanced_prime_',
    'bellpoly'          : 'bell_polynomial',
    'bits'              : 'count_bits',
    'cal'               : 'calendar',
    'cbrt'              : 'root3',
    'cc'                : 'cubic_centimeter',
    'ccube'             : 'centered_cube',
    'cdec'              : 'centered_decagonal',
    'cdec?'             : 'centered_decagonal?',
    'cdecagonal'        : 'centered_decagonal',
    'cdecagonal?'       : 'centered_decagonal?',
    'ceil'              : 'ceiling',
    'centeredcube'      : 'centered_cube',
    'champ'             : 'champernowne',
    'chept'             : 'centered_heptagonal',
    'chept?'            : 'centered_heptagonal?',
    'cheptagonal'       : 'centered_heptagonal',
    'cheptagonal?'      : 'centered_heptagonal?',
    'chex'              : 'centered_hexagonal',
    'chex?'             : 'centered_hexagonal?',
    'chexagonal'        : 'centered_hexagonal',
    'chexagonal?'       : 'centered_hexagonal?',
    'civil_dawn'        : 'dawn',
    'civil_dusk'        : 'dusk',
    'click'             : 'kilometer',
    'cnon'              : 'centered_nonagonal',
    'cnon?'             : 'centered_nonagonal?',
    'cnonagonal'        : 'centered_nonagonal',
    'cnonagonal?'       : 'centered_nonagonal?',
    'coct'              : 'coctagonal',
    'coct?'             : 'coctagonal?',
    'coctagonal'        : 'centered_octagonal',
    'coctagonal?'       : 'centered_octagonal?',
    'combine_dig'       : 'combine_digits',
    'comb_dig'          : 'combine_digits',
    'composition'       : 'compositions',
    'conj'              : 'conjugate',
    'cosecant'          : 'csc',
    'cosine'            : 'cos',
    'cotangent'         : 'cot',
    'countbits'         : 'count_bits',
    'cousin'            : 'cousin_prime',
    'cousin?'           : 'cousin_prime?',
    'cousinprime'       : 'cousin_prime',
    'cousinprime?'      : 'cousin_prime?',
    'cousinprime_'      : 'cousin_prime_',
    'cousin_'           : 'cousin_prime_',
    'cpent'             : 'centered_pentagonal',
    'cpent?'            : 'centered_pentagonal?',
    'cpentagonal'       : 'centered_pentagonal',
    'cpentagonal?'      : 'centered_pentagonal?',
    'cpoly'             : 'centered_polygonal',
    'cpoly?'            : 'centered_polygonal?',
    'cpolygonal'        : 'centered_polygonal',
    'cpolygonal?'       : 'centered_polygonal?',
    'csqr'              : 'centered_square',
    'csqr?'             : 'centered_square?',
    'csquare'           : 'centered_square',
    'csquare?'          : 'centered_square?',
    'ctri'              : 'centered_triangular',
    'ctri?'             : 'centered_triangular?',
    'ctriangular'       : 'centered_triangular',
    'ctriangular'       : 'centered_triangular',
    'ctriangular?'      : 'centered_triangular?',
    'cuberoot'          : 'root3',
    'cube_root'         : 'root3',
    'c_cube'            : 'centered_cube',
    'c_dec'             : 'centered_decagonal',
    'c_dec?'            : 'centered_decagonal?',
    'c_decagonal'       : 'centered_decagonal',
    'c_decagonal?'      : 'centered_decagonal?',
    'c_hept'            : 'centered_heptagonal',
    'c_hept?'           : 'centered_heptagonal?',
    'c_heptagonal'      : 'centered_heptagonal',
    'c_heptagonal?'     : 'centered_heptagonal?',
    'c_hexagonal'       : 'centered_hexagonal',
    'c_hexagonal?'      : 'centered_hexagonal?',
    'c_non'             : 'centered_nonagonal',
    'c_non?'            : 'centered_nonagonal?',
    'c_nonagonal'       : 'centered_nonagonal',
    'c_nonagonal?'      : 'centered_nonagonal?',
    'c_oct'             : 'coctagonal',
    'c_oct?'            : 'coctagonal?',
    'c_octagonal'       : 'centered_octagonal',
    'c_octagonal?'      : 'centered_octagonal?',
    'c_pent'            : 'centered_pentagonal',
    'c_pent?'           : 'centered_pentagonal?',
    'c_pentagonal'      : 'centered_pentagonal',
    'c_pentagonal?'     : 'centered_pentagonal?',
    'c_poly'            : 'centered_polygonal',
    'c_poly?'           : 'centered_polygonal?',
    'c_polygonal'       : 'centered_polygonal',
    'c_polygonal?'      : 'centered_polygonal?',
    'c_sqr'             : 'centered_square',
    'c_sqr?'            : 'centered_square?',
    'c_square'          : 'centered_square',
    'c_square?'         : 'centered_square?',
    'c_tri'             : 'centered_triangular',
    'c_tri?'            : 'centered_triangular?',
    'c_triangular'      : 'centered_triangular',
    'c_triangular'      : 'centered_triangular',
    'deca'              : 'decagonal',
    'deca?'             : 'decagonal?',
    'diff'              : 'diffs',
    'divcount'          : 'count_divisors',
    'divides'           : 'isdivisible',
    'doublebal'         : 'double_balanced',
    'doublebal_'        : 'double_balanced_',
    'doublefac'         : 'double_factorial',
    'double_bal'        : 'double_balanced',
    'double_bal_'       : 'double_balanced_',
    'dup'               : 'dup_term',
    'dupop'             : 'dup_operator',
    'dup_dig'           : 'dup_digits',
    'dup_op'            : 'dup_operator',
    'eddington'         : 'eddington_number',
    'election'          : 'election_day',
    'equal'             : 'is_equal',
    'eulerbrick'        : 'euler_brick',
    'eulerphi'          : 'euler_phi',
    'eulers_number'     : 'e',
    'exprange'          : 'exponential_range',
    'f!'                : 'fibonorial',
    'fac'               : 'factorial',
    'fac2'              : 'double_factorial',
    'factors'           : 'factor',
    'fall'              : 'autumnal_equinox',
    'fermi'             : 'femtometer',
    'fib'               : 'fibonacci',
    'frac'              : 'fraction',
    'free_space'        : 'magnetic_constant',
    'frob'              : 'frobenius',
    'fromunix'          : 'from_unix_time',
    'fromunixtime'      : 'from_unix_time',
    'from_unix'         : 'from_unix_time',
    'gammaflux'         : 'nanotesla',
    'gamma_flux'        : 'nanotesla',
    'gemmho'            : 'micromho',
    'geomean'           : 'geometric_mean',
    'geomrange'         : 'geometric_range',
    'georange'          : 'geometric_range',
    'geo_mean'          : 'geometric_mean',
    'geo_range'         : 'geometric_range',
    'gigohm'            : 'gigaohm',
    'golden'            : 'phi',
    'golden_ratio'      : 'phi',
    'greater'           : 'is_greater',
    'group'             : 'group_elements',
    'harm'              : 'harmonic',
    'hept'              : 'heptagonal',
    'hept?'             : 'heptagonal?',
    'hepthex'           : 'heptagonal_hexagonal',
    'heptpent'          : 'heptagonal_pentagonal',
    'heptsqr'           : 'heptagonal_square',
    'heptsquare'        : 'heptagonal_square',
    'hepttri'           : 'heptagonal_triangular',
    'hept_hex'          : 'heptagonal_hexagonal',
    'hept_pent'         : 'heptagonal_pentagonal',
    'hept_sqr'          : 'heptagonal_square',
    'hept_square'       : 'heptagonal_square',
    'hept_tri'          : 'heptagonal_triangular',
    'hex'               : 'hexagonal',
    'hex?'              : 'hexagonal?',
    'hexpent'           : 'hexagonal_pentagonal',
    'hexsqr'            : 'hexagonal_square',
    'hexsquare'         : 'hexagonal_square',
    'hextri'            : 'hexagonal',
    'hex_pent'          : 'hexagonal_pentagonal',
    'hex_sqr'           : 'hexagonal_square',
    'hex_square'        : 'hexagonal_square',
    'hex_tri'           : 'hexagonal',
    'hyper4'            : 'tetrate',
    'hyperfac'          : 'hyperfactorial',
    'hypot'             : 'hypotenuse',
    'im'                : 'imaginary',
    'inf'               : 'infinity',
    'int'               : 'long',
    'int16'             : 'short',
    'int32'             : 'long',
    'int64'             : 'longlong',
    'int8'              : 'char',
    'intersect'         : 'intersection',
    'invert'            : 'invert_units',
    'isdiv'             : 'is_divisible',
    'isoday'            : 'iso_day',
    'isolated'          : 'isolated_prime',
    'isprime'           : 'is_prime',
    'issqr'             : 'is_square',
    'issquare'          : 'is_square',
    'is_div'            : 'is_divisible',
    'is_more'           : 'is_greater',
    'is_nonequal'       : 'not_equal',
    'is_not_more'       : 'is_not_greater',
    'is_sqr'            : 'is_square',
    'julianday'         : 'julian_day',
    'klick'             : 'kilometer',
    'len'               : 'count',
    'length'            : 'count',
    'less'              : 'is_less',
    'linear'            : 'linear_recur',
    'linearrecur'       : 'linear_recur',
    'll_nac'            : 'latlong_to_nac',
    'll_to_nac'         : 'latlong_to_nac',
    'log'               : 'ln',
    'makecf'            : 'make_cf',
    'makeiso'           : 'make_iso_time',
    'makeisotime'       : 'make_iso_time',
    'makejulian'        : 'make_julian_time',
    'makejuliantime'    : 'make_julian_time',
    'makepyth'          : 'make_pyth_3',
    'makepyth3'         : 'make_pyth_3',
    'makepyth4'         : 'make_pyth_4',
    'maketime'          : 'make_time',
    'make_iso'          : 'make_iso_time',
    'make_julian'       : 'make_julian_time',
    'make_pyth3'        : 'make_pyth_3',
    'make_pyth4'        : 'make_pyth_4',
    'math'              : 'arithmetic',
    'maxdouble'         : 'max_double',
    'maxfloat'          : 'max_float',
    'maxint'            : 'max_long',
    'maxint128'         : 'max_quadlong',
    'maxint16'          : 'max_short',
    'maxint32'          : 'max_long',
    'maxint64'          : 'max_longlong',
    'maxint8'           : 'max_char',
    'maxlong'           : 'max_long',
    'maxlonglong'       : 'max_longlong',
    'maxquad'           : 'max_quadlong',
    'maxquadlong'       : 'max_quadlong',
    'maxshort'          : 'max_short',
    'maxuchar'          : 'max_uchar',
    'maxuint'           : 'max_ulong',
    'maxuint128'        : 'max_uquadlong',
    'maxuint16'         : 'max_ushort',
    'maxuint32'         : 'max_ulong',
    'maxuint64'         : 'max_ulonglong',
    'maxuint8'          : 'max_uchar',
    'maxulong'          : 'max_ulong',
    'maxulonglong'      : 'max_ulonglong',
    'maxuquadlong'      : 'max_uquadlong',
    'maxushort'         : 'max_ushort',
    'max_char'          : 'max_char',
    'max_int'           : 'max_long',
    'max_int128'        : 'max_quadlong',
    'max_int16'         : 'max_short',
    'max_int32'         : 'max_long',
    'max_int64'         : 'max_longlong',
    'max_int8'          : 'max_char',
    'max_quad'          : 'max_quadlong',
    'max_uint'          : 'max_ulong',
    'max_uint128'       : 'max_uquadlong',
    'max_uint16'        : 'max_ushort',
    'max_uint32'        : 'max_ulong',
    'max_uint64'        : 'max_ulonglong',
    'max_uint8'         : 'max_uchar',
    'mcg'               : 'microgram',
    'megalerg'          : 'megaerg',
    'megaohm'           : 'megohm',
    'members'           : 'use_members',
    'metre'             : 'meter',
    'metres'            : 'meter',
    'minchar'           : 'min_char',
    'mindouble'         : 'min_double',
    'minfloat'          : 'min_float',
    'minint'            : 'min_long',
    'minint128'         : 'min_quadlong',
    'minint16'          : 'min_short',
    'minint32'          : 'min_long',
    'minint64'          : 'min_longlong',
    'minint8'           : 'min_char',
    'minlong'           : 'min_long',
    'minlonglong'       : 'min_longlong',
    'minquad'           : 'min_quadlong',
    'minquadlong'       : 'min_quadlong',
    'minshort'          : 'min_short',
    'minuchar'          : 'min_uchar',
    'minuint'           : 'min_ulong',
    'minuint128'        : 'min_uquadlong',
    'minuint16'         : 'min_ushort',
    'minuint32'         : 'min_ulong',
    'minuint64'         : 'min_ulonglong',
    'minuint8'          : 'min_uchar',
    'minulong'          : 'min_ulong',
    'minulonglong'      : 'min_ulonglong',
    'minuquadlong'      : 'min_uquadlong',
    'minushort'         : 'min_ushort',
    'min_int'           : 'min_long',
    'min_int128'        : 'min_quadlong',
    'min_int16'         : 'min_short',
    'min_int32'         : 'min_long',
    'min_int64'         : 'min_longlong',
    'min_int8'          : 'min_char',
    'min_quad'          : 'min_quadlong',
    'min_uint'          : 'min_ulong',
    'min_uint128'       : 'min_uquadlong',
    'min_uint16'        : 'min_ushort',
    'min_uint32'        : 'min_ulong',
    'min_uint64'        : 'min_ulonglong',
    'min_uint8'         : 'min_uchar',
    'mod'               : 'modulo',
    'more'              : 'is_greater',
    'mu0'               : 'magnetic_constant',
    'mult'              : 'multiply',
    'multifac'          : 'multifactorial',
    'mult_dig'          : 'multiply_digits',
    'mult_digits'       : 'multiply_digits',
    'n'                 : 'x',
    'napiers_constant'  : 'e',
    'neg'               : 'negative',
    'ninf'              : 'negative_infinity',
    'non'               : 'nonagonal',
    'non?'              : 'nonagonal?',
    'nonahept'          : 'nonagonal_heptagonal',
    'nonahex'           : 'nonagonal_hexagonal',
    'nonaoct'           : 'nonagonal_octagonal',
    'nonapent'          : 'nonagonal_pentagonal',
    'nonasqr'           : 'nonagonal_square',
    'nonasquare'        : 'nonagonal_square',
    'nonatri'           : 'nonagonal_triangular',
    'nona_hept'         : 'nonagonal_heptagonal',
    'nona_hex'          : 'nonagonal_hexagonal',
    'nona_oct'          : 'nonagonal_octagonal',
    'nona_pent'         : 'nonagonal_pentagonal',
    'nona_sqr'          : 'nonagonal_square',
    'nona_square'       : 'nonagonal_square',
    'nona_tri'          : 'nonagonal_triangular',
    'nonzeroes'         : 'nonzero',
    'not_greater'       : 'is_not_greater',
    'nspherearea'       : 'n_sphere_area',
    'nsphereradius'     : 'n_sphere_radius',
    'nspherevolume'     : 'n_sphere_volume',
    'nsphere_area'       : 'n_sphere_area',
    'nsphere_radius'     : 'n_sphere_radius',
    'nsphere_volume'     : 'n_sphere_volume',
    'nthday'            : 'nth_weekday',
    'nthdayofyear'      : 'nth_weekday_of_year',
    'nthprime'          : 'prime',
    'nthprime?'         : 'nth_prime?',
    'nthquad?'          : 'nth_quad?',
    'nthweekday'        : 'nth_weekday',
    'nthweekdayofyear'  : 'nth_weekday_of_year',
    'nth_prime'         : 'nth_prime?',
    'octa'              : 'octagonal',
    'octa?'             : 'octagonal?',
    'octhept'           : 'octagonal_heptagonal',
    'octhex'            : 'octagonal_hexagonal',
    'octpent'           : 'octagonal_pentagonal',
    'octsqr'            : 'octagonal_square',
    'octsquare'         : 'octagonal_square',
    'octtri'            : 'octagonal_triangular',
    'oct_hept'          : 'octagonal_heptagonal',
    'oct_hex'           : 'octagonal_hexagonal',
    'oct_pent'          : 'octagonal_pentagonal',
    'oct_sqr'           : 'octagonal_square',
    'oct_square'        : 'octagonal_square',
    'oct_tri'           : 'octagonal_triangular',
    'oeiscomment'       : 'oeis_comment',
    'oeisex'            : 'oeis_ex',
    'oeisname'          : 'oeis_name',
    'p!'                : 'primorial',
    'partition'         : 'partitions',
    'pascaltri'         : 'pascal_triangle',
    'pascal_tri'        : 'pascal_triangle',
    'pent'              : 'pentagonal',
    'pent?'             : 'pentagonal?',
    'pentsqr'           : 'pentagonal_square',
    'pentsquare'        : 'pentagonal_square',
    'penttri'           : 'pentagonal_triangular',
    'pent_sqr'          : 'pentagonal_square',
    'pent_square'       : 'pentagonal_square',
    'pent_tri'          : 'pentagonal_triangular',
    'poly'              : 'polygonal',
    'poly?'             : 'polygonal?',
    'polyarea'          : 'polygon_area',
    'polyeval'          : 'eval_poly',
    'polyval'           : 'eval_poly',
    'poly_4_3'          : 'squaretri',
    'poly_5_3'          : 'pentagonal_triangular',
    'poly_5_4'          : 'pentagonal_square',
    'poly_6_3'          : 'hexagonal',
    'poly_6_3'          : 'hexagonal',
    'poly_6_4'          : 'hexagonal_square',
    'poly_6_4'          : 'hexagonal_square',
    'poly_6_5'          : 'hexagonal_pentagonal',
    'poly_6_5'          : 'hexagonal_pentagonal',
    'poly_7_3'          : 'heptagonal_triangular',
    'poly_7_4'          : 'heptagonal_square',
    'poly_7_5'          : 'heptagonal_pentagonal',
    'poly_7_6'          : 'heptagonal_hexagonal',
    'poly_8_3'          : 'octagonal_triangular',
    'poly_8_4'          : 'octagonal_square',
    'poly_8_5'          : 'octagonal_pentagonal',
    'poly_8_6'          : 'octagonal_hexagonal',
    'poly_8_7'          : 'octagonal_heptagonal',
    'poly_9_3'          : 'nonagonal_triangular',
    'poly_9_4'          : 'nonagonal_square',
    'poly_9_5'          : 'nonagonal_pentagonal',
    'poly_9_6'          : 'nonagonal_hexagonal',
    'poly_9_7'          : 'nonagonal_heptagonal',
    'poly_9_8'          : 'nonagonal_octagonal',
    'prev'              : 'previous',
    'prod'              : 'product',
    'puff'              : 'picofarad',
    'pyr'               : 'pyramid',
    'quad'              : 'quadruplet_prime',
    'quad?'             : 'quadruplet_prime?',
    'quadprime'         : 'quadruplet_prime',
    'quadprime?'        : 'quadruplet_prime?',
    'quadprime_'        : 'quadruplet_prime_',
    'quad_'             : 'quadruplet_prime_',
    'quad_prime'        : 'quadruplet_prime',
    'quad_prime?'       : 'quadruplet_prime?',
    'quad_prime_'       : 'quadruplet_prime_',
    'quint'             : 'quintuplet_prime',
    'quint?'            : 'quintuplet_prime?',
    'quintprime'        : 'quintuplet_prime',
    'quintprime?'       : 'quintuplet_prime?',
    'quintprime_'       : 'quintuplet_prime_',
    'quint_'            : 'quintuplet_prime_',
    'quint_prime'       : 'quintuplet_prime',
    'quint_prime?'      : 'quintuplet_prime?',
    'quint_prime_'      : 'quintuplet_prime_',
    'rand'              : 'random',
    'randint'           : 'random_integer',
    'randint_'          : 'random_integer_',
    'random_int'        : 'random_integer',
    'random_int_'       : 'random_integer_',
    're'                : 'real',
    'rev_add'           : 'reversal_addition',
    'rev_dig'           : 'reverse_digits',
    'rev_digits'        : 'reverse_digits',
    'rsort'             : 'sort_descending',
    'safe'              : 'safe_prime',
    'safe?'             : 'safe_prime?',
    'safeprime'         : 'safe_prime',
    'safeprime?'        : 'safe_prime?',
    'secant'            : 'sec',
    'sext'              : 'sextuplet_prime',
    'sext?'             : 'sextuplet_prime?',
    'sextprime'         : 'sextuplet_prime',
    'sextprime?'        : 'sextuplet_prime?',
    'sextprime_'        : 'sextuplet_prime_',
    'sext_'             : 'sextuplet_prime_',
    'sext_prime'        : 'sextuplet_prime',
    'sext_prime?'       : 'sextuplet_prime?',
    'sext_prime_'       : 'sextuplet_prime_',
    'sexy'              : 'sexy_prime',
    'sexy3'             : 'sexy_triplet',
    'sexy3?'            : 'sexy_triplet?',
    'sexy3_'            : 'sexy_triplet_',
    'sexy4'             : 'sexy_quadruplet',
    'sexy4?'            : 'sexy_quadruplet?',
    'sexy4_'            : 'sexy_quadruplet_',
    'sexy?'             : 'sexy_prime?',
    'sexyprime'         : 'sexy_prime',
    'sexyprime'         : 'sexy_prime',
    'sexyprime?'        : 'sexy_prime?',
    'sexyprime_'        : 'sexy_prime',
    'sexyquad'          : 'sexy_quadruplet',
    'sexyquad?'         : 'sexy_quadruplet?',
    'sexyquad_'         : 'sexy_quadruplet_',
    'sexytriplet'       : 'sexy_triplet',
    'sexytriplet?'      : 'sexy_triplet?',
    'sexytriplet_'      : 'sexy_triplet_',
    'sexy_'             : 'sexy_prime',
    'sexy_quad'         : 'sexy_quadruplet',
    'sexy_quad?'        : 'sexy_quadruplet?',
    'sexy_quad_'        : 'sexy_quadruplet_',
    'shiftleft'         : 'shift_left',
    'shiftright'        : 'shift_right',
    'silver'            : 'silver_ratio',
    'sine'              : 'sin',
    'sleft'             : 'shift_left',
    'sophie'            : 'sophie_prime',
    'sophie?'           : 'sophie_prime?',
    'sophieprime'       : 'sophie_prime',
    'sophieprime?'      : 'sophie_prime?',
    'sortdesc'          : 'sort_descending',
    'sort_desc'         : 'sort_descending',
    'spherearea'        : 'sphere_area',
    'sphereradius'      : 'sphere_radius',
    'spherevolume'      : 'sphere_volume',
    'split'             : 'unpack',
    'spring'            : 'vernal_equinox',
    'sqr'               : 'square',
    'sqrt'              : 'root2',
    'sqrtri'            : 'squaretri',
    'sqr_tri'           : 'squaretri',
    'squareroot'        : 'root2',
    'squaretri'         : 'square_triangular',
    'square_root'       : 'root2',
    'square_tri'        : 'square_triangular',
    'sright'            : 'shift_right',
    'stelloct'          : 'stella_octagula',
    'subfac'            : 'subfactorial',
    'sum_dig'           : 'sum_digits',
    'summer'            : 'summer_solstice',
    'superfac'          : 'superfactorial',
    'syl'               : 'sylvester',
    'tangent'           : 'tan',
    'thurs'             : 'thursday',
    'totient'           : 'euler_phi',
    'tounix'            : 'to_unix_time',
    'tounixtime'        : 'to_unix_time',
    'to_unix'           : 'to_unix_time',
    'tri'               : 'triangular',
    'tri?'              : 'triangular?',
    'trianglearea'      : 'triangle_area',
    'triarea'           : 'triangle_area',
    'trib'              : 'tribonacci',
    'triplet'           : 'triplet_prime',
    'triplet?'          : 'triplet_prime?',
    'tripletprime'      : 'triplet_prime',
    'tripletprime?'     : 'triplet_prime?',
    'tripletprime_'     : 'triplet_prime_',
    'triplet_'          : 'triplet_prime_',
    'triple_bal'        : 'triple_balanced',
    'triple_bal_'       : 'triple_balanced_',
    'trisqr'            : 'square_triangular',
    'tri_area'          : 'triangle_area',
    'tri_sqr'           : 'square_triangular',
    'truncoct'          : 'truncated_octahedral',
    'trunctet'          : 'truncated_tetrahedral',
    'trunc_oct'         : 'truncated_octahedral',
    'trunc_tet'         : 'truncated_tetrahedral',
    'twin'              : 'twin_prime',
    'twin?'             : 'twin_prime?',
    'twinprime'         : 'twin_prime',
    'twinprime?'        : 'twin_prime?',
    'twinprime_'        : 'twin_prime_',
    'twin_'             : 'twin_prime_',
    'uint'              : 'ulong',
    'uint16'            : 'ushort',
    'uint32'            : 'ulong',
    'uint64'            : 'ulonglong',
    'uint8'             : 'uchar',
    'unitroots'         : 'uint_roots',
    'units'             : 'unit_types',
    'unsigned'          : 'uinteger',
    'vernal'            : 'vernal_equinox',
    'winter'            : 'winter_solstice',
    'woodall'           : 'riesel',
    'yearcal'           : 'year_calendar',
    'yearcalendar'      : 'year_calendar',
    'zeroes'            : 'zero',
    'zero_mode'         : 'leading_zero_mode',
    '^'                 : 'power',
    '_dumpalias'        : '_dump_aliases',
    '_dumpops'          : '_dump_operators',
    '|'                 : 'is_divisible',
    '~'                 : 'not',
}


