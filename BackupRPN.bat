rem //******************************************************************************
rem //
rem //  BackupRPN
rem //
rem //  This TCC script is used to backup RPN.   It assumes Cygwin is installed.
rem //
rem //******************************************************************************

setlocal

iff "%1" == "" then
    echo usage:  BackupRPN target_dir_list [versioned_target_dir_list]
	quit
endiff

set VERSION=%@execstr[grep "VERSION " rpnVersion.py | cut -d' ' -f3  | tr -d -c 01234567890.]
set RPN_FILES=rpn*.py;makeHelp.py;makeRPNPrimes.py;makeUnits.py;makeConstants.py;setup_rpn.py;test*.py;profile*.py;rpnTest.txt;rpn.ico;rpn32.iss;rpn64.iss;BuildRPN.bat;BuildRPNInstaller.bat;pyecm.py;requirements.txt;setup.cfg;MANIFEST.in;setup.py;unpickle.py;preparePrimeData.py;BackupRPN.bat;rpnConstants.txt

for /t; %TARGET_DIR in (%1) if exist %TARGET_DIR .and. isdir %TARGET_DIR for %FILE in (%RPN_FILES) copy %FILE %TARGET_DIR
for /t; %TARGET_DIR in (%2) if exist %TARGET_DIR .and. isdir %TARGET_DIR for %FILE in (%RPN_FILES) copy %FILE %TARGET_DIR%\%@NAME[%FILE].%VERSION.%@EXT[%FILE]

endlocal

