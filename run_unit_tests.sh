#!/bin/bash
#run the unit tests
cd UnitTest
nosetests --with-xunit --xunit-file testresults.xml
cd ..

# echo -----------------
# echo runnign pyflakes
# pyflakes *.py