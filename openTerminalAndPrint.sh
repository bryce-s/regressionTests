
echo Regression Results:
echo $0
cd $0/../.. # we launch this script, we're
            # not in scope with our target python script. So cd up 2.
python regressionTests/reportResults.py
