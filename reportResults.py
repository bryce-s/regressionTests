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
        exit(1)  # exits with 'error,' ha


preCheck()


class IssueLog(object):
    def __init__(self):
        self.loops = list()
        self.diffs = list()

    def addLoopReport(self, lhs: str, rhs: str):
        self.loops.append([lhs, rhs])

    def addDiffReport(self, lhs: str, rhs: str):
        self.diffs.append([lhs, rhs])

    def getDiffTargetField(self, target: int, index: int):
        return self.diffs[index][target]

    def quickPrintDiffs(self):
        if len(self.diffs) == 0:
            return
        print(bcolors.HEADER)
        print("Diff issues found:")
        counter = int(0)
        for lists in self.diffs:
            print(str(counter) + " " + lists[0] + " differs from " + lists[1])
            counter = counter + 1

    def quickPrintLoops(self):
        if len(self.loops) == 0:
            return
        print(bcolors.WARNING)
        print("Infinite Loops Found")
        counter = 0
        for lists in self.loops:
            print(str(counter) + " " + lists[0] + " looped forever.")
            counter = counter + 1


if os.path.exists("regressionTests/failureLog.txt"):
    print(bcolors.FAIL + "Warning: defects have been detected\n---------------")
    log = IssueLog()
    with open("regressionTests/failureLog.txt", 'r') as infile:
        for line in infile:
            lineArray = line.split()
            if lineArray[0] == "diff":
                log.addDiffReport(lineArray[1], lineArray[2])
            else:
                log.addLoopReport(lineArray[1], lineArray[2])
        log.quickPrintDiffs()
        log.quickPrintLoops()
    print(bcolors.OKBLUE)
    print("Would you like to view a diff? Enter a number, or anything else to exit\n")
    target = input()
    while True:
        try:
            val = int(target)
            os.system("vimdiff " + str(log.getDiffTargetField(0, val)
                                       ) + " " + str(log.getDiffTargetField(1, val)))
            target = input()
        except ValueError:
            print("Exiting.")
            exit(0)

print(bcolors.OKBLUE)
