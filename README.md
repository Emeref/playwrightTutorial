# playwrightTutorial
 This is my playwright tutorial

#### For system to works fine we have to install few packages:
 * pytest-playwritght
 * pytest-reporter-html1
 * pytest-xdist

#### command to run tests:
    pytest --template=html1/index.html --report=report.html -n 3 --maxfail=1 -m smoke --browser=chromium --device="iPhone 14" 

* **report**: name of report file.
* **n**: 'auto' allows to check bow many are available, and with numbers 1-auto we can select how many will 
                     not make using computer hard...
* **maxfail**: sets amount of fails after which we will stop the run
* **m**: will allow to test only TC that are marked with specific way (available markers are described in pytest.ini, 
   and each test has marker set before test definition
* **browser**: there are three options: 'chromium','firefox','webkit'. If there will be more than one selected (ex. 
   '--webkit=chromium --webkit=firefox' means that all tests will be run 2 times on selected browsers.
* **device**: allows to run tests as specific device: 'iPhone 14'. This runs only on chromium
