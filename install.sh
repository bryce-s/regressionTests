set -e
set -x
brew install coreutils
# make scripts executable by sys calls
chmod +x regressionTests/openTerminalAndPrint.sh
chmod +x regressionTests/reportResults.py
chmod +x regressionTests/openTerminalAndPrint.sh
mkdir tests
mkdir tests/assemblerOutput
mkdir tests/correct
mkdir tests/rawAssembly
mkdir tests/simulatorOutput
echo "to execute, call sh regressionTests/buildDebug.sh (or whatever I rename it to) from project root"
