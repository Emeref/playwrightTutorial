# playwrightTutorial
 This is my playwright tutorial

#### For system to works fine we have to install few packages:
 * pytest-playwritght
 * pytest-reporter-html1
 * pytest-xdist

#### command to run tests:
    pytest --template=html1/index.html --report=report.html -n _number of cores used for testing_ --maxfail=1 -m smoke

* **report**: name of report file.
* **for number of cores**: 'auto' allows to check bow many are available, and with numbers 1-auto we can select how many will 
                     not make using computer hard...
* **maxfail**: sets amount of fails after which we will stop the run
* **m**: will allow to test only TC that are marked with specific way (available markers are described in pytest.ini, 
   and each test has marker set before test definition
