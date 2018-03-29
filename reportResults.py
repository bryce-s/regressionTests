import sys
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def preCheck():
    if len(sys.argv) > 1:
        """we return to shell script if we have issues."""
        if os.path.exists("regressionTests/failureLog.txt"):
            exit(0)
        exit(1) # exits with 'error,' ha
preCheck()


if os.path.exists("regressionTests/failureLog.txt"):
    print(bcolors.FAIL + "Warning: defects have been detected")
    

print(bcolors.OKBLUE)
