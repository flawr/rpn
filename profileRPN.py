# //******************************************************************************
# //
# //  profileRPN
# //
# //  main test script for RPN
# //  copyright (c) 2016, Rick Gutleber (rickg@his.com)
# //
# //  License: GNU GPL 3.0 (see <http://www.gnu.org/licenses/gpl.html> for more
# //  information).
# //
# //******************************************************************************

from testRPN import runTests


# //******************************************************************************
# //
# //  __main__
# //
# //******************************************************************************

if __name__ == '__main__':
    import profile
    profile.run( 'runTests( sys.argv[ 1 : ] )' )

