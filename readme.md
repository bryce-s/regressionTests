# regressionTests

Executes all test cases, compares with correct output files (where avaliable) and displays issues in a termianl popup.


# Todo:
log issues reported by ``runRegressionTests,py`` to ``failureLog.txt``, parse and display using ``reportResults.py``

# Usage
clone directory to project folder, then
```
sh regressionTests/install.sh
sh regressionTests/runRegressionTests.sh # could put this in vscode
```

# Contains:
```
.
├── install.sh
├── openTerminalAndPrint.sh
├── reportResults.py
└── runRegressionTests.sh
```
