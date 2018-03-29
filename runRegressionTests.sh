set -e
set -x
clang-format -i -style=WebKit *.c 

assembleTests() {
    for asfile in tests/rawAssembly/*.as.*
    do
        asfilename=$(echo $asfile | cut -d '.' -f-1)
        outfilename=$(echo $asfilename | cut -d '/' -f3)
        postfix=$(echo $asfile | cut -d '.' -f 3,4,5)
        gtimeout 2 ./assem $asfile tests/assemblerOutput/$outfilename.mc.$postfix
        if [ $? -eq 124 ]; then # $? accepts return val from gtimeout, if took >= 2 seconds,
                                # iff return val == 124; it timed out.
            echo "the command timed out"
            # do something
        fi
    done
}

simulateOutput() {
    for mcfile in tests/assemblerOutput/*.mc.*
    do
        mcfilename=$(echo $mcfile | cut -d '/' -f3)
        blockSizeInWords=$(echo $mcfile | cut -d '.' -f3)
        numberOfSets=$(echo $mcfile | cut -d '.' -f4)
        blockPerSet=$(echo $mcfile | cut -d '.' -f5) 
        gtimeout 2 ./simDebug $mcfile $blockSizeInWords $numberOfSets $blockPerSet > tests/simulatorOutput/$mcfilename.sim
        if [ $? -eq 124 ]; then
            echo "the command timed out"
            # do something here
        fi
    done
}

diffResults() {
    for correctFile in tests/correct/*
    do
        correctFilename=$(echo $correctFile | cut -d '/' -f3)
        targetName=$(echo $correctFilename | cut -d '.' -f 1,2,3,4,5).sim
        vimdiff $correctFile tests/simulatorOutput/$targetName
    done
}


runOutput() {
    assembleTests
    simulateOutput
    diffResults
}

reportResults() {
    if python regressionTests/reportResults.py 1; then
       open -a Terminal.app ./regressionTests/openTerminalAndPrint.sh --args .
    fi
}

compileAndCheckStatus() {
  if gcc -g -o simDebug simulator.c && gcc -o assem assembler.c; then
    echo "compiled!"
    else 
    echo "gcc failed. exiting"
    return 1
   fi
}


reportResults
