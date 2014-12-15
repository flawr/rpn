from cx_Freeze import setup, Executable
from rpnVersion import PROGRAM_VERSION

# Dependencies are automatically detected, but it might need fine tuning.
buildOptions = \
    dict(
        packages = [ 'gmpy2', 'matplotlib', 'numpy', 'pylab' ],

        include_files = [
            'rpndata/help.pckl.bz2',
            'rpndata/small_primes.pckl.bz2',
            'rpndata/units.pckl.bz2',
            'rpndata/unit_conversions.pckl.bz2',
            'rpndata/unit_help.pckl.bz2',
            'rpndata/balanced_primes.pckl.bz2',
            'rpndata/cousin_primes.pckl.bz2',
            'rpndata/double_balanced_primes.pckl.bz2',
            'rpndata/isolated_primes.pckl.bz2',
            'rpndata/large_primes.pckl.bz2',
            'rpndata/quad_primes.pckl.bz2',
            'rpndata/quint_primes.pckl.bz2',
            'rpndata/sext_primes.pckl.bz2',
            'rpndata/sexy_primes.pckl.bz2',
            'rpndata/sexy_quadruplets.pckl.bz2',
            'rpndata/sexy_triplets.pckl.bz2',
            'rpndata/sophie_primes.pckl.bz2',
            'rpndata/super_primes.pckl.bz2',
            'rpndata/triplet_primes.pckl.bz2',
            'rpndata/triple_balanced_primes.pckl.bz2',
            'rpndata/twin_primes.pckl.bz2'
        ],

        include_msvcr = 1,
        optimize = 2,
    )

executables = [
    Executable( script = 'rpn.py',
                base = None,
                icon = 'rpn.ico',
                initScript = None,
                shortcutName = 'rpn ' + PROGRAM_VERSION,
                targetName = 'rpn.exe'
    )
]

setup( name='rpn',
       version = PROGRAM_VERSION,
       author = 'Rick Gutleber',
       author_email = 'rickg@his.com',
       description = 'command-line RPN calculator',
       options = dict( build_exe = buildOptions ),
       executables = executables
)

